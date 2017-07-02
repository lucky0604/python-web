import Vue from 'vue'
import Vuex from 'vuex'
import account from './modules/account'
import permissions from './modules/permissions'
import app from './modules/app'
import getters from './getters'

Vue.use(Vuex)

const store = new Vuex.Store({
  modules: {
    account,
    permissions,
    app
  },
  getters
})

export default store