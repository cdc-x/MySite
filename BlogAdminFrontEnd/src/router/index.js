import Vue from 'vue'
import Router from 'vue-router'
import Login from '@/components/Login.vue'
import Home from '@/components/Home.vue'

Vue.use(Router)

const router =  new Router({
    mode: "history",
    routes: [
        { path: '/', redirect: '/login'},
        { path: '/login', component: Login },
        { path: '/config', component: Home},
    ]
})


router.beforeEach((to, from, next)=>{
    if (to.path === "/login"){
        next()
    }else{
        // 获取token
        const tokenStr =  window.sessionStorage.getItem("AUTHORIZATION");
        if (tokenStr){
            next()
        }else{
            next("/login")
        }
    }
})

export default router