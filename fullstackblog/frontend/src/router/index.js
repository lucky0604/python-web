import Vue from 'vue'
import Router from 'vue-router'
const _import = require('./_import_' + process.env.NODE_ENV)

const Regist = _import('register/register')
const Login = _import('login/login')
const Layout = _import('dashboard/index')

Vue.use(Router)

/*
export default new Router({
  routes: [
    {
      path: '/',
      name: 'regist',
      component: Regist
    }
  ]
})
*/


export const constantRouterMap = [
  {
    path: '/reg',
    name: 'regist',
    component: Regist
  },
  {
    path: '/login',
    name: 'login',
    component: Login
  },{
    path: '/',
    name: 'dashboard',
    meta: {requireAuth: true},
    component: Layout
  }
]

export default new Router({
  scrollBehavior: () => ({y: 0}),
  routes: constantRouterMap
})
