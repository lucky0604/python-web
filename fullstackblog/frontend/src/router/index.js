import Vue from 'vue'
import Router from 'vue-router'
import Reg from '@/pages/reg/reg.vue'
import Home from '@/pages/home/home.vue'
import Login from '@/pages/login/login.vue'
import store from '@/store'

Vue.use(Router)

const routes = [

  {
    path: '/reg',
//      name: 'Login',
    component: Reg
  },
  {
    path: '/login',
    name: 'login',
    component: Login
  },
  {
    path: '/',
    meta: {
      requireAuth: true
    },
    component: Home
  },
]

const RouterConfig = {
  mode: 'history',
  routes: routes
}

const router = new Router(RouterConfig)

router.beforeEach((to, from, next) => {
  if (to.matched.some(r => r.meta.requireAuth)) {
    let token = localStorage.getItem('token')
    if (token) {
      console.log('token match')
      next()
    } else {
      next({
        path: '/login'
      })
    }
  } else {
    console.log('----not match-----')
    next()
  }
})


export default router
