import Vue = require('vue')
import VueRouter = require('vue-router')
import {Route, RawLocation, NavigationGuard} from './index'

/**
 * declare keyword is used to declare variables that may not have originated from a Typescript file
 */

declare module "vue/types/vue" {
	interface Vue {
		$router: VueRouter;
		$route: Route;
	}
}


declare module "vue/types/options" {
	interface ComponentOptions<V extends Vue> {
		router?: VueRouter;
		beforeRouteEnter?: NavigationGuard;
		beforeRouteLeave?: NavigationGuard;
		beforeRouteUpdate?: NavigationGuard;
	}
}