import Vue from 'vue'
import VueRouter from 'vue-router'
import App from './App.vue'
import Modules from './views/index'


Vue.use(VueRouter)

const router = new VueRouter({
	routes: [
		{
			path: '/',
			component: Modules.AppController
		}
	]
})

export {
	App,
	router
}