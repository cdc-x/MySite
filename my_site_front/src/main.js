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
  Scrollbar,
  Collapse,
  CollapseItem,
  Pagination,
  Input
} from 'element-ui'
import axios from 'axios'
import mavonEditor from 'mavon-editor'
import 'mavon-editor/dist/css/index.css'

/* 导入全局样式 */
import '@/assets/css/global.css'
import '@/assets/css/animate.min.css'

// 配置根本请求路径
axios.defaults.baseURL = "http://127.0.0.1:8000/"

Vue.use(Button)
Vue.use(Row)
Vue.use(Col)
Vue.use(Card)
Vue.use(Timeline)
Vue.use(TimelineItem)
Vue.use(Tag)
Vue.use(Scrollbar)
Vue.use(mavonEditor)
Vue.use(Collapse)
Vue.use(CollapseItem)
Vue.use(Pagination)
Vue.use(Input)

Vue.prototype.$wow = wow
Vue.prototype.$echarts = window.echarts
Vue.config.productionTip = false
Vue.prototype.$http = axios

/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  components: { App },
  template: '<App/>',
  store
})
