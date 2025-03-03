import os
import random 
import gradio as gr
from zhconv import convert
# from LLM import LLM
from digital_humans.ASR import WhisperASR
from digital_humans.ASR import FunASR
# from TFG import SadTalker
# from digital_humans.TFG import SadTalker
from digital_humans.TTS import EdgeTTS
from digital_humans.src.cost_time import calculate_time
from src import init, produce_res
from configs import *
import threading
os.environ["GRADIO_TEMP_DIR"]= './temp'

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
pic_path = "final1.png"
crop_pic_path = "digital_humans/inputs/first_frame_dir_girl/final1.png"
first_coeff_path = "digital_humans/inputs/first_frame_dir_girl/girl.mat"
crop_info = ((403, 403), (19, 30, 502, 513), [40.05956541381802, 40.17324339233366, 443.7892505041507, 443.9029284826663])

exp_weight = 1

use_ref_video = False
ref_video = None
ref_info = 'pose'
use_idle_mode = False
length_of_audio = 5
def clear_session():
    # clear history
    return '', []
@calculate_time
def Asr(audio):
    try:
        question = asr.transcribe(audio)
        question = convert(question, 'zh-cn')
    except Exception as e:
        print("ASR Error: ", e)
        question = 'Gradio存在一些bug，麦克风模式有时候可能音频还未传入，请重新点击一下语音识别即可'
        gr.Warning(question)
    return question

@calculate_time
def LLM_response(answer, voice = 'zh-CN-XiaoxiaoNeural', rate = 0, volume = 0, pitch = 0):
    print(answer)
    try:
        tts.predict(answer, voice, rate, volume, pitch , 'answer.wav', 'answer.vtt')
    except:
        os.system(f'edge-tts --text "{answer}" --voice {voice} --write-media answer.wav')
    return 'answer.wav', 'answer.vtt', answer

@calculate_time
def Talker_response(text, chat_history, voice='zh-CN-XiaoxiaoNeural', rate=0, volume=100, pitch=0, batch_size=10):
    res, chat_history = produce_res(text, chat_history)

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
        return "", chat_history, video, driven_vtt
    else:
        return "", chat_history, video

def main():
    with gr.Blocks(analytics_enabled=False, title = '文旅问答助手——吉安市篇') as inference:
        gr.HTML(description)
        with gr.Row(equal_height=False):
            with gr.Column(variant='panel'): 
                with gr.Tabs(elem_id="question_audio"):
                    with gr.TabItem('对话'):
                        with gr.Column(variant='panel'):
                            chatbot = gr.Chatbot(height=400, show_copy_button=True)
                            question_audio = gr.Audio(sources=['microphone','upload'], type="filepath", label = '语音对话')
                            input_text = gr.Textbox(label="Input Text", lines=3)
                            asr_text = gr.Button('语音识别（语音对话后点击）')
                            asr_text.click(fn=Asr,inputs=[question_audio],outputs=[input_text])
                            

                            with gr.Row():
                                clear_history = gr.Button("🧹 清除历史对话")
                                # submit = gr.Button("🚀 发送", variant='primary')
                                submit = gr.Button("🚀 发送", variant='primary')
                            clear_history.click(fn=clear_session, outputs=[input_text, chatbot])
            with gr.Column(variant='panel'):
                # with gr.Tabs():
                #     with gr.TabItem('小向导'):
                gen_video = gr.Video(label="Generated video", format="mp4", scale=0.5, autoplay=True,
                                     height=500, interactive=False)
                # video_button = gr.Button("提交", variant='primary')
            # video_button.click(fn=Talker_response,inputs=[input_text],outputs=[gen_video])
            submit.click(Talker_response, inputs=[input_text, chatbot],
                         outputs=[input_text, chatbot, gen_video])

    return inference



if __name__ == "__main__":
    try:
        from digital_humans.TFG import Wav2Lip
        wav2lip = Wav2Lip("digital_humans/checkpoints/wav2lip_gan.pth")
    except Exception as e:
        print("Wav2Lip Error: ", e)
        print("如果使用Wav2Lip，请先下载Wav2Lip模型")
    asr = WhisperASR('base')
    # asr = FunASR()
    tts = EdgeTTS()
    gr.close_all()
    init()
    demo = main()
    demo.queue()
    # demo.launch()
    demo.launch(server_name=ip, # 本地端口localhost:127.0.0.1 全局端口转发:"0.0.0.0"
                server_port=port,
                # 似乎在Gradio4.0以上版本可以不使用证书也可以进行麦克风对话
                ssl_certfile=ssl_certfile,
                ssl_keyfile=ssl_keyfile,
                ssl_verify=False,
                debug=True)
