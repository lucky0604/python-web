// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import router from './router'
import store from './store'
import ElementUI from 'element-ui'
import 'element-ui/lib/theme-default/index.css'
import NProgress from 'nprogress'
import 'nprogress/nprogress.css'
import 'normalize.css/normalize.css'
import 'styles/index.scss'
import * as filters from './filter'
import Cookies from 'js-cookie'
import Multiselect from 'vue-multiselect'
import 'vue-multiselect/dist/vue-multiselect.min.css'
import Sticky from 'components/Sticky'
import vueWaves from './directives/waves'

Vue.config.productionTip = false
Vue.component('multiselect', Multiselect)
Vue.component('Sticky', Sticky)
Vue.use(vueWaves)
Vue.use(ElementUI)

Object.keys(filters).forEach(key => {
  Vue.filter(key, filters[key])
})

// permission judge
function hasPermission(groups, permissionRoles) {
  if (groups.indexOf(1) >= 0) return true
  if (!permissionRoles) return true
  return groups.some(group => permissionRoles.indexOf(group) >= 0)
}

// register global progress
const whiteList = ['/login', '/reg']
router.beforeEach((to, from, next) => {
  if (store.getters.token) {
    if (to.path === '/login') {
      next({path: '/'})
    } else {
      if (store.getters.groups.length === 0) {
        alert('main router')
        store.dispatch('GetInfo').then(res => {
          const groups = res.data.groups
          console.log(groups)
          store.dispatch('GenerateRoutes', {groups}).then(() => {
            router.addRoutes(store.getters.addRouters)
            next(to.path)
          })
        }).catch(err => {
          console.log(err)
        })
      } else {
        if (hasPermission(store.getters.groups, to.meta.group)) {
          next()
        } else {
          alert()
        }
      }
      /*
      next({
        path: '/login',
      })
      */
    } 
  } else {
    if (whiteList.indexOf(to.path) !== -1) {
      next()
    } else {
      next('/login')
    }
  }

  /**
  // NProgress.start()   // enable NProgress
  if (store.getters.token) {    // check if there's token
    if (to.path === '/login') {
      next({path: '/'})
    } else {
      if (store.getters.groups.length === 0) {   // check the current user has already get the user_info
        store.dispatch('GetInfo').then(res => {
          const groups = res.data.groups
          
          store.dispatch('GenerateRoutes', {groups}).then(() => {
            router.addRoutes(store.getters.addRoutes)
            next(to.path)
          })
          
          console.log(groups)
        }).catch(err => {
          console.log(err)
        })
      } else {
        if (hasPermission(store.getters.groups, to.meta.group)) {
          next()
        } else {
          next({path: '/401', query: {noGoBack: true}})
        }
      }
    }
  } */
})

/*
router.afterEach(() => {
  NProgress.done()
})
*/

/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  store,
  render: h => h(App)
})
