// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import router from './router'
import wow from 'wowjs'
import '@/assets/fonts/iconfont.css'
import store from './store'
import {
  Button,
  Row,
  Col,
  Card,
  Timeline,
  TimelineItem,
  Tag,
} from 'element-ui'

/* 导入全局样式 */
import '@/assets/css/global.css'
import '@/assets/css/animate.min.css'

Vue.prototype.$wow = wow
Vue.prototype.$echarts = window.echarts
Vue.config.productionTip = false

Vue.use(Button)
Vue.use(Row)
Vue.use(Col)
Vue.use(Card)
Vue.use(Timeline)
Vue.use(TimelineItem)
Vue.use(Tag)


/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  components: { App },
  template: '<App/>',
  store
})
