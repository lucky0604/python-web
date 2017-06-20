import * as types from './types'

const actions = {
  userLogin({commit}, data) {
    commit(types.LOGIN, data)
  },
  delUserSession({commit}, data) {
    commit(types.DELSESSION, data)
  },
  userLoginOut({commit}) {
    commit(types.LOGINOUT)
  }
}

export default actions
