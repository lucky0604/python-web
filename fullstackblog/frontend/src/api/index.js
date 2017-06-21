import axios from 'axios'
import Vue from 'vue'
import VueAxios from 'vue-axios'

Vue.use(VueAxios, axios)

const instance = axios.create()

Vue.axios.defaults.headers['Content-Type'] = 'application/json'

export default {
    localReg: function(data) {
        alert(data)
        return Vue.axios.post('http://127.0.0.1:8000/api/accounts/create/', data)
    }
}