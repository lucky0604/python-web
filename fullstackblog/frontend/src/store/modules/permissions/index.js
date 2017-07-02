import actions from './actions'
import mutations from './mutations'
import {constantRouterMap} from 'src/router'

const state = {
  routers: constantRouterMap,
  addRouters: []
}

export default {
  state,
  actions,
  mutations
}