<template>
  <div class="whole-wrapper">
    <!-- <div class="pc-side-bar">
      <side-bar></side-bar>
    </div> -->
    <div class="main">
      <router-view></router-view>
    </div>
  </div>
</template>

<script setup>
import { RouterView } from 'vue-router';
import SideBar from './views/SideBar.vue';
</script>

<style scoped>
.whole-wrapper {
  position: fixed;
  width: 100%;
  height: 100%;
  display: flex;
}
.pc-side-bar {
  height: 100%;
}
.main {
  flex: 1;
}
</style>