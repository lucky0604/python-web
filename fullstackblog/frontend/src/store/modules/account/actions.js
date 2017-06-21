import api from '@/api'
import { USER_REG } from './mutation-types'

export default {
    UserReg: ({ commit }, data) => {
        api.localReg(data).then(function(res) {
                commit(USER_REG, res.data)
                console.log(res.data)
            })
            .catch(function(err) {
                console.log(err)
            })
    }
}