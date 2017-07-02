/*
 * @CreateTime: Jul 3, 2017 12:07 AM
 * @Author: Lucky
 * @Contact: Lucky
 * @Last Modified By: undefined
 * @Last Modified Time: Jul 3, 2017 12:14 AM
 * @Description: Modify Here, Please 
 */
import {registUser} from 'api/regist'
import {loginByUsername, getInfo, logout} from 'api/login'
import {REG_USER} from './mutation-types'
import {Message} from 'element-ui'
import Cookies from 'js-cookie'

export const RegUser = ({commit}, data) => {
  registUser(data).then(function(res){
    if (res.status === 201) {
      commit(REG_USER, res.data.key)
      Message({
        message: 'Regist Successfully',
        type: 'success'
      })
    }
  })
  .catch(function(err) {
    console.log(err)
  })
}


// Login
export const LoginByUsername = ({commit}, payload) => {
  const username = payload.username.trim()
  return new Promise((resolve, reject) => {
    loginByUsername(username, payload.password).then(res => {
      const data = res.data
      Cookies.set('Admin-Token', res.data.key)
      commit('SET_TOKEN', data.key)
      // commit('SET_EMAIL', email)
      resolve()
    }).catch(err => {
      reject(err)
    })
  })
}

// Get User info
export const GetInfo = ({commit, state}) => {
  return new Promise((resolve, reject) => {
    getInfo().then(res => {
      const data = res.data
      console.log(data)
      commit('SET_GROUPS', data.groups)
      commit('SET_NAME', data.username)
      resolve(res)
    }).catch(err => {
      reject(err)
    })
  })
}

// log out
export const LogOut = ({commit, state}) => {
  return new Promise((resolve, reject) => {
    logout().then(res => {
      commit('SET_TOKEN', '')
      commit('SET_GROUPS', [])
      Cookies.remove('Admin-Token')
      resolve()
    }).catch(err => {
      reject(err)
    })
  })
}