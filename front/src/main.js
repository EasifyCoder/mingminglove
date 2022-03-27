import Vue from 'vue'
import App from './App.vue'
import router from './router'
// 引入仓库
import store from '@/store'
import ElementUI from 'element-ui';
import 'element-ui/lib/theme-chalk/index.css';
// 引入文本编辑器
import mavonEditor from 'mavon-editor'
import 'mavon-editor/dist/css/index.css'

Vue.config.productionTip = false
Vue.use(ElementUI);
Vue.use(mavonEditor)

// //测试
// import {reqHundredThingsList} from '@/api';
// let a = reqHundredThingsList();
// console.log(a);

new Vue({
  router,
  //注册仓库：组件实例的身上会多一个属性$store属性
  store,
  render: h => h(App)
}).$mount('#app')
