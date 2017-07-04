import {TOGGLE_SIDEBAR, ADD_VISITED_VIEWS, DEL_VISITED_VIEWS} from './mutation-types'
import Cookies from 'js-cookie'

export default {
  [TOGGLE_SIDEBAR](state) {
    if (state.sidebar.opened) {
      Cookies.set('sidebarStatus', 1)
    } else {
      Cookies.set('sidebarStatus', 0)
    }
    state.sidebar.opened = !state.sidebar.opened
  },
  [ADD_VISITED_VIEWS](state, view) {
    if (state.visitedViews.includes(view)) {
      return
    }
    state.visitedViews.push(view)
  },
  [DEL_VISITED_VIEWS](state, view) {
    const index = state.visitedViews.indexOf(view)
    state.visitedViews.splice(index, 1)
  }
}