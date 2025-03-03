<template>
    <div>
      <el-dialog
      v-model="dialogVisible"
      title="选择其他省市"
      width="60%"
    >
      <Dialog></Dialog>
      <div class="dialog-footer">
        <button type="primary" @click="changeDistrcit">
          确认
        </button>
        <button @click="dialogVisible = false">取消</button>
      </div>
    </el-dialog>
      <!-- <div style="display: flex;justify-content: center;">
        <el-alert title="数字人视频生成较慢，如干扰测试可将其关闭。" type="warning" style="max-width: 768px;font-size: 1.5rem;" />
      </div> -->
      <div class="wholeWrapper">
        <h1 style="display: flex;align-items: center;">智能旅游助手——{{district.district[1]}}篇</h1>
        <p>这里的问答系统基于{{ district.district.join("") }}的文旅信息制作~</p>
        <button @click="dialogVisible=true;">选择其他省市</button>
        <div class="main">
          <div class="left">
            <div class="box">
              <div class="phoneShow" v-if="phone_vis">
                  <img src="../assets/final3.png" alt="图片走丢啦" class="person-phone" v-if="phone_img_show">
                  <video :src="video1_play" type="video/mp4" ref="video1" x-webkit-airplay="true"  webkit-playsinline="true"  x5-video-player-type="h5" x5-video-orientation="portraint"  controls="controls" @ended="handleEnd2()" class="person-phone" v-show="phone_video_show">
                    <!-- <source :src="video" type="video/mp4"  > -->
                  </video>
              </div>
              <div class="chatbot">
                <div v-for="(item, i) in chat_history">
                  <template v-if="i % 2 === 0">
                    <!-- 当 i 是偶数时显示第一个组件 -->
                    <Humans :content="item"></Humans>
                  </template>
                  <template v-else>
                    <!-- 当 i 是奇数时显示第二个组件 -->
                    <Assistant :content="item"></Assistant>
                  </template>
                </div>
  
              </div>
            </div>
            
            <div class="textWrapper">
              <textarea placeholder="请输入" class="text" cols="30" rows="1" v-model="input_text" :disabled="disabled" @keyup.enter="toSubmit()"></textarea>
            </div>
            <div style="display: flex;margin-top: 1rem;">
              <div style="width:6rem;font-size: 1.2rem;display: flex;align-items: center;">猜你想问：</div>
              <el-card style="cursor:pointer;" shadow="always" @click="input_text='有什么景点推荐吗？'">有什么景点推荐吗？</el-card>
            </div>
            <div class="btns">
              <button @click="chat_history = []">
                🧹 清除历史对话
              </button>
              <button @click="handlePerson()">{{ operation }}数字人生成</button>
              <button class="submit" @click="toSubmit()">
                发送🚀
              </button>
            </div>
          </div>
          <div class="right" v-if="right_show" v-loading="loading2">
            <img src="../assets/final1.png" alt="图片走丢啦" class="person" v-if="pc_img_show" >
            <video :src="video2_play" type="video/mp4" autoplay ref="video2" @ended="handleEnd1()" controls="controls" v-show="pc_video_show" class="person-video">
              <!-- <source :src="video" type="video/mp4"  > -->
            </video>
          </div>
        </div>
      </div>
    </div>
  </template>
  
  <script setup>
  import { useDistrictStore } from '../stores/district.js';
  import Humans from '../components/Humans.vue';
  import Assistant from '../components/Assistant.vue';
  import { ref, onMounted } from 'vue';
  import axios from 'axios';
  import { ElMessage, ElMessageBox } from 'element-plus'
  import Dialog from '../components/Dialog.vue';
  const district = useDistrictStore();
  const chat_history = ref([])
  function changeDistrcit(){
    district.change();
    dialogVisible.value = false;
    chat_history.value = []
  }
  const flag = ref(0);
  const dialogVisible = ref(false);
  const input_text = ref("")
  const video1_play = ref("");
  const video2_play = ref("");
  const pc_img_show = ref(true);
  const pc_video_show = ref(false);
  const right_show = ref(true);
  const phone_img_show = ref(true);
  const phone_video_show = ref(false);
  const video1 = ref(null);
  const video2 = ref(null);
  const loading1 = ref(false);
  const loading2 = ref(false);
  const disabled = ref(false);
  const phone_vis = ref(true);
  const operation = ref("关闭");
  // 获取窗口宽度
  let windowWidth = window.innerWidth;
  // 判断设备类型
  if (windowWidth < 768) {
    // 手机端适配
    flag.value = 1;
    right_show.value = false;
    phone_img_show.value = true;
    phone_video_show.value = false;
    pc_img_show.value = false;
    pc_video_show.value = false;
  } else {
    // 电脑端适配
    flag.value = 0;
    right_show.value = true;
    phone_img_show.value = false;
    phone_video_show.value = false;
    pc_img_show.value = true;
    pc_video_show.value = false;
  }
  // replace here with your own baseURL
  let baseUrl = "YOUR BASEURL";
  function toSubmit(){
    disabled.value = true;
    if (input_text.value.length == 0) {
      disabled.value = false;
      ElMessage.error('输入内容不可为空！')
      return;
    }
    if (phone_video_show.value){
      console.log(1);
      phone_video_show.value = false;
      phone_img_show.value = true;
    }
    if (pc_video_show.value){
      console.log(2);
      pc_video_show.value = false;
      pc_img_show.value = true;
    }
    let temp_history =[]; 
    temp_history = chat_history.value.concat();
  
    console.log(temp_history);
    chat_history.value.push(input_text.value);
    let text = input_text.value;
    input_text.value = "";
    if(flag.value == 0) {
        loading2.value = true;
    }else{
        loading1.value = true;
    } 
    axios.post(baseUrl + "/getResponse", {
      input_text: text,
      chat_history: temp_history,
      district: district.district.join("")
    })
    .then(function (response) {
      console.log(response.data);
      // get_video(response)
      pc_img_show.value = true;
      let res = response.data.response;
      console.log(res);
      chat_history.value.push(res);
      disabled.value = false;
      if(operation.value === "关闭") {
        get_video(res);
      } else {
        if(loading1.value) loading1.value = false;
        if(loading2.value) loading2.value = false;
        if(video1_play.value != "") video1_play.value = "";
        if(video2_play.value != "") video2_play.value = "";
      }
    })
    .catch(function (error) {
      console.log(error);
      ElMessageBox.alert('由于GPU租赁昂贵，当前GPU服务器处于关闭状态.', '提示消息！', {
      confirmButtonText: '确认',
    })
    });
  }
  function get_video(res){
    console.log(res)
    let url = baseUrl;
    console.log(url)
    if(flag.value == 0) {
      url += "/getVideo1";
    }
    else{
      url += "/getVideo2";
    } 
    console.log(url);
    axios.post(url, {
      text: res,
    })
    .then(function (response) {
      disabled.value = false;
      if(flag.value == 0) {
        loading2.value = false;
      }else{
        url += "/getVideo2";
        loading1.value = false;
      } 
      console.log(response.data);
      if(flag.value){
        video1_play.value = baseUrl + "/videos/" + response.data.video_path[0];
        phone_video_show.value = true;
        phone_img_show.value = false;
        video1.value.load();
        video1.value.play();
      } else {
        video2_play.value = baseUrl + "/videos/" + response.data.video_path[0];
        pc_img_show.value = false;
        pc_video_show.value = true;
        video2.value.load();
        video2.value.play();
      }
    })
    .catch(function (error) {
      console.log(error);
    });
  }
  function handleEnd1(){
    pc_img_show.value = true;
    pc_video_show.value = false;
    video2_play.value = "";
  }
  function handleEnd2(){
    phone_img_show.value = true;
    phone_video_show.value = false;
    video1_play.value = "";
  
  }
  function handlePerson(){
    if(operation.value === "关闭"){
      right_show.value = false;
      phone_vis.value = false;
      operation.value = "开启";
    } else if (operation.value === "开启"){
      if(!flag.value) right_show.value = true;
      phone_vis.value = true;
      operation.value = "关闭";
    }
  
  }
  </script>
  
  <style scoped>
  .dialog-footer {
    display: flex;
    justify-content: flex-end;
    align-items: center;
  }

  .wholeWrapper {
    display: flex;
    flex-direction: column;
    max-width: 1040px;
    margin: 0 auto;
    padding-top: 4rem;
    justify-content: center;
    align-items: center;
  }
  .main {
    width: 100%;
    display: flex;
    padding-top: 2rem;
    overflow-x: hidden;
  }
  .left {
    flex: 1;
    flex-direction: column;
  }
  .box {
    position: relative;
    width: 100%;
    height: 450px;
  }
  .chatbot {
    width: 100%;
    display: flex;
    flex-direction: column;
    border: 1px solid rgba(49, 51, 63, 0.2);
    border-radius: 0.5rem;
    padding: calc(1em - 1px);
    padding-right: 2rem;
    height: 450px;
    overflow: auto;
  }
  .textWrapper {
    display: flex;
    justify-content: center;
  }
  .text {
    padding: 10px;
    margin: 0;
    border: none;
    outline: none;
    resize: none;
    font-size: 1rem; /* 根据需要设置字体大小 */
    color: currentColor; /* 使用当前文本颜色 */
    width: 98%;
    background-color: rgb(240, 242, 246);
    border-radius: 0.5rem;
    margin-top: 10px;
  }
  .btns {
    display: flex;
    justify-content: flex-end;
  }
  
  .right {
    flex: 1;
    margin-left: 2rem;
  }
  .person {
    width: 100%;
  }
  .person-video {
    width: 100%;
  }
  
  .person-phone {
    position: absolute;
    width: 100px;
    height: 180px;
    right: -0.2rem;
    bottom: 0px;
    z-index: 5;
  }
  
  button {
    display: flex;
    height: 2rem;
    padding: 20px;
    outline: none;
    border: 1px solid rgba(49, 51, 63, 0.2);
    background: #fff;
    font-size: 1rem;
    justify-content: center;
    align-items: center;
    margin-right: 15px;
    margin-top: 15px;
    cursor: pointer;
    border-radius: 0.5rem;
  }
  
  button:hover {
    border: 1px solid rgb(255, 166, 0);
    color: rgb(255, 166, 0)
  }
  
  
  </style>