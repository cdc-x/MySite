import Vue from 'vue'
import Router from 'vue-router'
import Index from '@/components/Index.vue'
import Home from '@/components/Home.vue'


Vue.use(Router)

const router = new Router({
  routes: [
    { path: '/', component: Index },
    { path: '/home', component: Home },
  ]
})


export default router