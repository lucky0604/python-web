export default {
  token: state => state.account.token,
  name: state => state.account.name,
  groups: state => state.account.groups,
  permission_routers: state => state.permissions.routers,
  addRouters: state => state.permissions.addRouters,
  sidebar: state => state.app.sidebar,
}