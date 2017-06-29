import axios from 'axios'
import {Message} from 'element-ui'
import store from '../store'

const service = axios.create({
  baseURL: process.env.BASE_API,
  timeout: 5000
})

// request interceptor
service.interceptors.request.use(config => {
  // some actions before request is sent
  if (store.getters.token) {
    config.headers['X-Token'] = store.getters.token     // make each request has a token --- ['X-Token'] is custom key
  }
  return config
}, error => {
  // some actions with request error
  console.log(error)
  Promise.reject(error)
})


// response interceptors
service.interceptors.response.use(
  response => response,
  error => {
    console.log('err: ' + error)
    Message({
      message: error.message,
      type: 'error',
      duration: 5 * 1000
    })
    return Promise.reject(error)
  }
)

export default service