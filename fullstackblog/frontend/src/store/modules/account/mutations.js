import { USER_REG } from './mutation-types'

export default {
    [USER_REG](state, user) {
        localStorage.setItem('user', JSON.stringify(user))
        state.user = user
    }
}