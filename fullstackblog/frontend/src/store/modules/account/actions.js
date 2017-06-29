import {registUser} from 'api/regist'
import {REG_USER} from './mutation-types'
import {Message} from 'element-ui'

export const RegUser = ({commit}, data) => {
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
}