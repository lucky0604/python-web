import {REG_USER} from './mutation-types'

export default {
  [REG_USER](state, data) {
    state.token = data
  }
}