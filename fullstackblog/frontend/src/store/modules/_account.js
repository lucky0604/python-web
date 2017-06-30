import {loginByUsername, getInfo} from 'api/login'
import {registUser} from 'api/regist'
import Cookies from 'js-cookie'

const account = {
  state: {
    user: '',
    email: '',
    token: Cookies.get('Admin-Token'),
    name: '',
    groups: []
  },

  mutations: {
    REG_USER:(state, data) => {
      state.token = data
    },
    SET_TOKEN:(state, token) => {
      state.token = token
    },
    SET_EMAIL:(state, email) => {
      state.email = email
    },
    SET_GROUPS:(state, groups) => {
      state.groups = groups
    },
    SET_NAME:(state, name) => {
      state.name = name
    }
  },

  actions: {
    RegUser: ({commit}, data) => {
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
    },


    // Login
    LoginByUsername: ({commit}, payload) => {
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
    },

    // Get User info
    GetInfo: ({commit, state}) => {
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
  },
}

export default account