import Vue from 'vue'
import Router from 'vue-router'
const _import = require('./_import_' + process.env.NODE_ENV)

const Regist = _import('register/register')
const Login = _import('login/login')

// layout
import Layout from '../views/layout/Layout'

// dashboard
const dashboard = _import('dashboard/index')

// Introduction
const Introduction = _import('introduction/index')
const PostIntro = _import('introduction/post/index')


// Components
const Tinymce = _import('components/tinymce/index')
const Draglist = _import('components/draglist/index')
const Sticky = _import('components/sticky/index')
const countTo = _import('components/countTo/index')

// Charts
const KeyboardChart = _import('charts/keyboard/index')
const KeyboardChart2 = _import('charts/keyboard2/index')
const LineMarker = _import('charts/line/index')
const MixChart = _import('charts/mixChart/index')

// examples
const TableLayout = _import('example/table/index')
const DynamicTable = _import('example/table/dynamictable')
const DragTable = _import('example/table/dragTable')

// permission
const Permission = _import('permission/index')

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
    component: Login,
    hidden: true
  },{
    path: '/',
    name: 'Homepage',
    redirect: '/dashboard',
    component: Layout,
    hidden: true,
    children: [{
      path: 'dashboard',
      component: dashboard
    }]}
  
]

export default new Router({
  scrollBehavior: () => ({y: 0}),
  routes: constantRouterMap
})


export const asyncRouterMap = [
  {
    path: '/permission',
    component: Layout,
    name: 'Permission Test',
    meta: {group: [1], requireAuth: true},
    icon: 'quanxian',
    noDropdown: true,
    children: [{path: 'index', component: Permission, name: 'Permission test page', meta: {group: [1], requireAuth: true}}]
  }, {
      path: '/introduction',
      component: Layout,
      redirect: '/introduction/index',
      name: 'Introduction',
      children: [
        {path: 'index', component: Introduction, name: 'introduction'}, 
        {path: 'post', component: PostIntro, name: 'postIntro'}
        
      ]
    },{
      path: '/components',
      component: Layout,
      name: 'Components',
      children: [
        {path: 'tinymce', component: Tinymce, name: 'Tinymce'},
        {path: 'draglist', component: Draglist, name: 'Draglist'},
        {path: 'sticky', component: Sticky, name: 'Sticky'},
        {path: 'countTo', component: countTo, name: 'CountTo'}
      ]
    }, {
      path: '/charts',
      component: Layout,
      name: 'Charts',
      children: [
        {path: 'keyboard', component: KeyboardChart, name: 'KeyboardChart'},
        {path: 'keyboard2', component: KeyboardChart2, name: 'KeyboardChart2'},
        {path: 'line', component: LineMarker, name: 'Line Chart'},
        {path: 'mixchart', component: MixChart, name: 'Mix Chart'}
      ]
    }, {
      path: '/example',
      component: Layout,
      redirect: 'noredirect',
      name: 'Example',
      children: [
        {path: '/example/table', redirect: '/example/table/table', component: TableLayout, name: 'Table', children: [
          {path: 'dynamictable', component: DynamicTable, name: 'DynamicTable'},
          {path: 'dragtable', component: DragTable, name: 'Drag Table'}
        ]}
      ]
    }    
]