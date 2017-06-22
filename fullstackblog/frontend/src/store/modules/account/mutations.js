import { USER_REG, USER_LOGIN, USER_LOGOUT } from './mutation-types'

export default {
  [USER_REG](state, user) {
    localStorage.setItem('user', JSON.stringify(user))
    state.user = user
  },
  [USER_LOGIN](state, data) {
    if (data) {
      state.token = data
      state.isLogin = true
      localStorage.setItem('token', data)
    }
  },
  [USER_LOGOUT](state, user) {
    state.user = {}
    localStorage.removeItem('token')
    state.isLogin = false
  }
}
