<template>
    <div class="pc-sidebar-wrapper">
        <el-menu
        class="el-menu-vertical-demo"
        @open="handleOpen"
        @close="handleClose"
      >
        <el-menu-item index="1" @click="transferTo('/')">
          <el-icon><location /></el-icon>
          <span>智能旅游助手</span>
        </el-menu-item>
        <el-sub-menu index="1">
          <template #title>
            <el-icon><icon-menu /></el-icon>
            <span>自定义</span>
          </template>
          <el-menu-item index="1-1" @click="transferTo('designImage')">自定义数字人形象</el-menu-item>
          <el-menu-item index="1-2">自定义数字人声音</el-menu-item>
        </el-sub-menu>
      </el-menu>
    </div>
</template>

<script setup>
import {
  Document,
  Menu as IconMenu,
  Location,
  Setting,
} from '@element-plus/icons-vue'
import { useRouter } from 'vue-router';
const router = useRouter();
function transferTo(name){
    router.push(name);
}
</script>

<style scoped>
.pc-sidebar-wrapper{
  height: 100%;
}
.el-menu-vertical-demo{
  width: 15rem;
  height: 100%;
}
</style>