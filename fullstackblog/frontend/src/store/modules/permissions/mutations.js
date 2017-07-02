import {SET_ROUTERS} from './mutation-types'
import {constantRouterMap} from 'src/router'

export default {
  [SET_ROUTERS](state, routers) {
    state.addRouters = routers
    state.routers = constantRouterMap.concat(routers)
  }
}