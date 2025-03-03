import os
import random
import torch
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
# 设置 GPU 设备
try:
    from digital_humans.TFG import Wav2Lip

    wav2lip = Wav2Lip("digital_humans/checkpoints/wav2lip_gan.pth")
except Exception as e:
    print("Wav2Lip Error: ", e)
    print("如果使用Wav2Lip，请先下载Wav2Lip模型")
tts = EdgeTTS()


def set_device_for_thread(device_id):
    device = torch.device(f'cuda:{device_id}' if torch.cuda.is_available() else 'cpu')
    return device

@calculate_time
def LLM_response(answer, voice='zh-CN-XiaoxiaoNeural', rate=0, volume=0, pitch=0):
    print(answer)
    try:
        # 将模型和数据迁移到 GPU
        tts.predict(answer, voice, rate, volume, pitch, 'answer.wav', 'answer.vtt')
    except:
        os.system(f'edge-tts --text "{answer}" --voice {voice} --write-media answer.wav')
    return 'answer.wav', 'answer.vtt', answer

@calculate_time
def Talker_response(text, crop_pic_path="digital_humans/inputs/first_frame_dir_girl/final1.png",
                    voice='zh-CN-XiaoxiaoNeural', rate=0, volume=100, pitch=0, batch_size=30):
    res = text

    print(voice)
    print(voice in tts.SUPPORTED_VOICE)
    voice = 'zh-CN-XiaoxiaoNeural' if voice not in tts.SUPPORTED_VOICE else voice
    print(voice)

    # 定义生成音频的函数
    def generate_audio():
        device = set_device_for_thread(0)  # 设置为第一个 GPU
        return LLM_response(res, voice, rate, volume, pitch)

    def generate_video():
        device = set_device_for_thread(1)  # 设置为第二个 GPU
        driven_audio, _, _ = generate_audio()
        return wav2lip.predict(crop_pic_path, driven_audio, batch_size, device=device)

    # 并行执行音频和视频生成任务
    audio_thread = threading.Thread(target=generate_audio)
    video_thread = threading.Thread(target=generate_video)

    audio_thread.start()
    video_thread.start()