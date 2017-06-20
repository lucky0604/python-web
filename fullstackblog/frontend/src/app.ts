import Vue from 'vue'
import Axios from 'axios'
import {App, router} from './router'

new Vue({
	el: '#app',
	router,
	render: h => h(App)
})