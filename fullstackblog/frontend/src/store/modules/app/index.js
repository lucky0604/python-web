import actions from './actions'
import mutations from './mutations'
import Cookies from 'js-cookie'

const state = {
  sidebar: {
    opened: !+Cookies.get('sidebarStatus')
  },
  theme: 'default',
  livenewsChannels: Cookies.get('livenewsChannels') || '[]',
  visitedViews: []
}

export default {
  state,
  actions,
  mutations
}