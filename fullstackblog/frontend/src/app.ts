import Vue from 'vue'
import Axios from 'axios'
import {App, router} from './router'

import * as Element from 'element-ui'
/**
 * it will raise an error: 
 * ERROR in ./~/element-ui/lib/theme-default/fonts/element-icons.woff?t=1472440741
Module parse failed: /Users/lucky/Documents/Code/Python/python-web/fullstackblog/frontend/node_modules/element-ui/lib/theme-default/fonts/element-icons.woff?t=1472440741 Unexpected character '' (1:4)
You may need an appropriate loader to handle this file type.
(Source code omitted for this binary file)
 @ ./~/css-loader!./~/less-loader/dist!./~/element-ui/lib/theme-default/index.css 6:644-694
 @ ./~/element-ui/lib/theme-default/index.css
 @ ./src/app.ts
 @ multi ./src/app.ts
 ------------------------------------------------------------------
 in webpack.config.dev.js
 add:
 {
                test: /\.(ttf|eot|svg|woff(2)?)(\?[a-z0-9=&.]+)?$/,
                loader: 'file-loader'
            }
 */
import 'element-ui/lib/theme-default/index.css'
Vue.use(Element)

new Vue({
	el: '#app',
	router,
	render: h => h(App)
})