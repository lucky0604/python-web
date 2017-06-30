import * as actions from './actions'
import mutations from './mutations'
import Cookies from 'js-cookie'

const state = {
  token: Cookies.get('Admin-Token'),
  user: '',
  name: '',
  groups: [],

}


export default {
  actions,
  state,
  mutations
}