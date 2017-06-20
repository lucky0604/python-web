import * as types from './types'

export const mutations = {
  [types.LOGIN](state, data) {
    state.user.name = data.name
    localStorage.setItem('user', data.name)
  },

  [types.LOGINOUT](state) {
    state.user = {}
    localStorage.removeItem('user')
  },

  [types.DELSESSION](state) {
    localStorage.removeItem('session')
  }
}
