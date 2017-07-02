/*
 * @CreateTime: Jul 1, 2017 6:46 PM
 * @Author: Lucky
 * @Contact: Lucky
 * @Last Modified By: undefined
 * @Last Modified Time: Jul 1, 2017 9:29 PM
 * @Description: Modify Here, Please 
 */
import {asyncRouterMap, constantRouterMap} from 'src/router'
import {SET_ROUTERS} from './mutation-types'

function hasPermission(groups, route) {
  if (route.meta && route.meta.group) {
    return groups.some(group => route.meta.group.indexOf(group) >= 0)
  } else {
    return true
  }
}

/**
 * filt the routes by using recursion, return the routes
 * @param {*} asyncRouterMap 
 * @param {*} groups 
 */
function filterAsyncRouter(asyncRouterMap, groups) {
  const accessedRouters = asyncRouterMap.filter(route => {
    if (hasPermission(groups, route)) {
      if (route.children && route.children.length) {
        route.children = filterAsyncRouter(route.children.groups)
      }
      return true
    }
    return false
  })
  return accessedRouters
}

export default {
  GenerateRoutes: ({commit}, data) => {
    return new Promise(resolve => {
      const groups = data.groups
      alert(groups)
      let accessedRouters
      if (groups.indexOf(1) >= 0) {
        accessedRouters = asyncRouterMap
      } else {
        accessedRouters = filterAsyncRouter(asyncRouterMap, groups)
      }
      commit(SET_ROUTERS, accessedRouters)
      resolve()
    })
  }
}