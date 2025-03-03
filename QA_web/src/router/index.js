import { createRouter, createWebHistory } from 'vue-router'
// import HomeView from '../views/HomeView.vue'
import ChatView from '@/views/ChatView.vue';
import DesignImage from '@/views/selfDesign/DesignImage.vue';

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'chatView',
      component: ChatView,
    },
    {
      path: '/designImage',
      name: 'designImage',
      component: DesignImage,
    }
  ]
})

export default router
