import Vue from 'vue'
import axios from 'axios'
import VueAxios from 'vue-axios'

Vue.use(VueAxios, axios)

var instance = axios.create()

export default {
  localReg: function(data) {
    return Vue.axios.post('/users/users/', data)
  }
}