import os
import random
from langchain_core.messages import AIMessage, HumanMessage
# import gradio as gr
from zhconv import convert
# from LLM import LLM
# from digital_humans.ASR import WhisperASR
# from digital_humans.ASR import FunASR
# from TFG import SadTalker
# from digital_humans.TFG import SadTalker
from digital_humans.TTS import EdgeTTS
from digital_humans.src.cost_time import calculate_time
from src import init, produce_res
from configs import *
import threading

os.environ["GRADIO_TEMP_DIR"] = './temp'

description = """<p style="text-align: center; font-weight: bold;">
    <span style="font-size: 28px;">文旅问答助手——吉安市篇</span>
    <br> 
    <span>这里的问答系统基于江西省吉安市的文旅信息制作~</span>
</p>
"""

# 设定默认参数值，可修改
source_image = r'example.png'
blink_every = True
size_of_image = 256
preprocess_type = 'crop'
facerender = 'facevid2vid'
enhancer = False
is_still_mode = False
# pic_path = "final1.png"
first_coeff_path = "digital_humans/inputs/first_frame_dir_girl/girl.mat"
crop_info = (
(403, 403), (19, 30, 502, 513), [40.05956541381802, 40.17324339233366, 443.7892505041507, 443.9029284826663])

exp_weight = 1

use_ref_video = False
ref_video = None
ref_info = 'pose'
use_idle_mode = False
length_of_audio = 5

try:
    from digital_humans.TFG import Wav2Lip

    wav2lip = Wav2Lip("digital_humans/checkpoints/wav2lip_gan.pth")
except Exception as e:
    print("Wav2Lip Error: ", e)
    print("如果使用Wav2Lip，请先下载Wav2Lip模型")
# asr = WhisperASR('base')
# asr = FunASR()
tts = EdgeTTS()



@calculate_time
def Asr(audio):
    try:
        question = asr.transcribe(audio)
        question = convert(question, 'zh-cn')
    except Exception as e:
        print("ASR Error: ", e)
        question = '存在一些bug，麦克风模式有时候可能音频还未传入，请重新点击一下语音识别即可'
        st.warning(question, icon="⚠️")
    return question


@calculate_time
def LLM_response(answer, voice='zh-CN-XiaoxiaoNeural', rate=0, volume=0, pitch=0):
    print(answer)
    try:
        tts.predict(answer, voice, rate, volume, pitch, 'answer.wav', 'answer.vtt')
    except:
        os.system(f'edge-tts --text "{answer}" --voice {voice} --write-media answer.wav')
    return 'answer.wav', 'answer.vtt', answer


@calculate_time
def Talker_response(text,crop_pic_path = "digital_humans/inputs/first_frame_dir_girl/final1.png",
                    voice='zh-CN-XiaoxiaoNeural', rate=0, volume=100, pitch=0, batch_size=30):
    res = text

    print(voice)
    print(voice in tts.SUPPORTED_VOICE)
    voice = 'zh-CN-XiaoxiaoNeural' if voice not in tts.SUPPORTED_VOICE else voice
    print(voice)

    # 定义生成音频的函数
    def generate_audio():
        return LLM_response(res, voice, rate, volume, pitch)

    def generate_video():
        driven_audio, _, _ = generate_audio()
        return wav2lip.predict(crop_pic_path, driven_audio, batch_size)

    # 并行执行音频和视频生成任务
    audio_thread = threading.Thread(target=generate_audio)
    video_thread = threading.Thread(target=generate_video)

    audio_thread.start()
    video_thread.start()

    audio_thread.join()
    video_thread.join()

    # 获取音频和视频结果
    driven_audio, _, driven_vtt = generate_audio()
    video = generate_video()
    if driven_vtt:
        return video, driven_vtt
    else:
        return video


