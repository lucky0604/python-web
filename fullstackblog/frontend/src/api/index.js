import axios from 'axios'
import Vue from 'vue'
import VueAxios from 'vue-axios'
import store from '../store'

Vue.use(VueAxios, axios)

const instance = axios.create()

Vue.axios.defaults.headers['Content-Type'] = 'application/json'

Vue.axios.interceptors.request.use = instance.interceptors.request.use

instance.interceptors.request.use(
  config => {
    if (store.state.account.token) {
      config.headers.Authorization = `token ${store.state.account.token}`
    }
    return config
  },
  err => {
    return Promise.reject(err)
  }
)

export default {
  localReg: function(data) {
    alert(data)
    return Vue.axios.post('http://127.0.0.1:8000/api/accounts/create/', data)
  },
  localLogin: function (data) {
    return Vue.axios.post('http://127.0.0.1:8000/api-token-auth/', data)
  },
}
