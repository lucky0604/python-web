import {constantRouterMap} from 'src/router'

function hasPermission(groups, route) {
  if (route.meta && route.meta.group) {
    return groups.some(group => route.meta.group.indexOf(group) >= 0)
  } else {
    return true
  }
}

