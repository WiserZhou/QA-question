from fastapi import FastAPI
import uvicorn
from fastapi.staticfiles import StaticFiles
from fastapi import Response
from src.interation import init, produce_res
# from app2 import Talker_response
from components import Talker_response
from starlette.middleware.cors import CORSMiddleware  #引入 CORS中间件模块
import json
# 创建 api 对象

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    # 允许跨域的源列表，例如 ["http://www.example.org"] 等等，["*"] 表示允许任何源
    allow_origins=["*"],
    # 跨域请求是否支持 cookie，默认是 False，如果为 True，allow_origins 必须为具体的源，不可以是 ["*"]
    allow_credentials=False,
    # 允许跨域请求的 HTTP 方法列表，默认是 ["GET"]
    allow_methods=["*"],
    # 允许跨域请求的 HTTP 请求头列表，默认是 []，可以使用 ["*"] 表示允许所有的请求头
    # 当然 Accept、Accept-Language、Content-Language 以及 Content-Type 总之被允许的
    allow_headers=["*"],
    # 可以被浏览器访问的响应头, 默认是 []，一般很少指定
    # expose_headers=["*"]
    # 设定浏览器缓存 CORS 响应的最长时间，单位是秒。默认为 600，一般也很少指定
    # max_age=1000
)
app.mount("/videos", StaticFiles(directory="results"), name="videos")


@app.post("/getResponse") # 根路由
def getResponse(request: dict):
    input_text = request.get("input_text")
    chat_history = request.get("chat_history")
    print(type(chat_history))
    print(input_text)
    response = produce_res(input_text, chat_history)
    return {
        "response": response,
    }
# @app.post("/items/")
@app.post("/getVideo1")
def getVideo1(request: dict):
    text = request.get("text")
    video = Talker_response(text)
    # 这里替换为你云端服务器上视频文件的路径
    # server_address = "Your Server Path"
    return {"video_path": video}
@app.post("/getVideo2")
def getVideo2(request: dict):
    text = request.get("text")
    video = Talker_response(text, crop_pic_path = "digital_humans/inputs/first_frame_dir_girl/final5.png")
    # 这里替换为你云端服务器上视频文件的路径
    # server_address = "Your Server Path"
    return {"video_path": video}

if __name__ == '__main__':
    init()

    uvicorn.run(app, host="127.0.0.1", port=6006)