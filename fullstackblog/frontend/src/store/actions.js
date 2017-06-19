import api from '../api'
import {USER_REG} from './types'

export const UserReg = ({commit}, data) => {
  api.localReg(data).then(function(response) {
    if (response.data.type == true) {
      commit(USER_REG, data) 
      window.location = '/index'
    }
  })
  .catch(function(err) {
    console.log(err)
  })
}