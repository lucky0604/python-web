import {TOGGLE_SIDEBAR, ADD_VISITED_VIEWS, DEL_VISITED_VIEWS} from './mutation-types'

export default {
  ToggleSideBar: ({commit}) => {
    commit(TOGGLE_SIDEBAR)
  },
  addVisitedViews: ({commit}, view) => {
    commit(ADD_VISITED_VIEWS, view)
  },
  delVisitedViews: ({commit}, view) => {
    commit(DEL_VISITED_VIEWS, view)
  }
}