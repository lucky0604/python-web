import api from '@/api'
import { USER_REG, USER_LOGIN, USER_LOGOUT } from './mutation-types'

export default {
  UserReg: ({ commit }, data) => {
    api.localReg(data).then(function(res) {
        commit(USER_REG, res.data)
        console.log(res.data)
      })
      .catch(function(err) {
        console.log(err)
      })
  },
  UserLogin: ({commit}, data) => {
    /*
    api.localLogin(data).then(function(res) {
      commit(USER_LOGIN, res.data.token)
    })
      .catch(function(err) {
        console.log(err)
      })
      */
    return new Promise((resolve, reject) => {
      api.localLogin(data).then(res => {
        if (res) {
          commit(USER_LOGIN, res.data.token)
        }
        resolve(res.data.token)
      }, error => {
        reject(error)
      })
    })
  },
  UserLogout: ({commit}) => {
    commit(USER_LOGOUT)
  }
}
