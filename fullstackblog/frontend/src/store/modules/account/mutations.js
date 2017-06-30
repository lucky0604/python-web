import {REG_USER, SET_TOKEN, SET_EMAIL, SET_GROUPS, SET_NAME} from './mutation-types'

export default {
  [REG_USER](state, data) {
    state.token = data
  },
  [SET_TOKEN](state, token) {
    state.token = token
  },
  [SET_EMAIL](state, email) {
    state.email = email
  },
  [SET_GROUPS](state, groups) {
    state.groups = groups
  },
  [SET_NAME](state, name) {
    state.name = name
  }
}