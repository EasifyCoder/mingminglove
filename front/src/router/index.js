import Vue from 'vue'
import VueRouter from 'vue-router'
import HomeView from '../views/HomeView.vue'
import Login from '../views/Login'
import Home from '../views/Home'
import page1 from '../views/page1.vue'
import DaysMatter from '@/views/DaysMatter'
import HundredThings from '@/views/HundredThings'
import ImageWall from '../views/ImageWall'
import Memorandum from '@/views/Memorandum'

Vue.use(VueRouter)

const routes = [
  {
    path: '/homeview',
    name: 'HomeView',
    component: HomeView
  },
  {
    path: '/',
    name: 'Login',
    component: Login
  },
  {
    path: '/home',
    name: 'Home',
    component: Home,
    children: [
      {
        path: '/daysmatter',
        name: 'DaysMatter',
        component: DaysMatter
      },
      {
        path: '/hundredthings',
        name: 'HundredThings',
        component: HundredThings
      },
      {
        path: '/ImageWall',
        name: 'ImageWall',
        component: ImageWall
      }
    ]
  },
  {
    path: '/page1',
    name: 'page1',
    component: page1
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})


// 导航守卫
router.beforeEach((to, from, next) => {
  const token = localStorage.getItem('token')
  if (to.name !== 'Login' && !token) next({name: 'Login'})
  else next()
})


export default router
