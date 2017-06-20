'use strict'

var path = require('path')

/**
 * import file entry point
 * @type {{index: string, details: string}|exports|module.exports}
 */
var webpack = require('webpack')
var WebpackDevServer = require('webpack-dev-server')
// extract common css
var HtmlWebpackPlugin = require('html-webpack-plugin')
var ExtractTextPlugin = require('extract-text-webpack-plugin')
var node_modules = path.resolve(__dirname, 'node_modules')
var pathToSrc = path.resolve(__dirname, 'src')
var pathToBuild = path.resolve(__dirname, 'dist')

var config = {
	devtool: false,
	entry: {
		app: [
			path.resolve(__dirname, 'src/app.ts')
		],
		common: [
			'vue',
			'vue-router',
			'vuex',
			'axios'
		]
	},
	output: {
		path: path.resolve(__dirname, 'dist'),
		chunkFilename: '[name].js',
		filename: '[name].js',
		publicPath: '/'
	},
	module: {
		rules: [
			{
				test: /\.(js|tsx|ts|vue)?$/,
				exclude: /node_modules/,
				loader: 'ts-loader',
				options: {
					transpileOnly: true,
					appendTsSuffixTo: [/\.vue$/]
				}
			},
			{
				test: /\.vue$/,
				loader: 'vue-loader'
			},
			{
				test: /\.(less|css)$/,
				exclude: /node_modules/,
				use: ExtractTextPlugin.extract({
					fallback: 'style-loader',
					use: ['css-loader', 'less-loader']
				})
			}
		]
	},
	resolve: {
		extensions: ['.js', '.ts', '.vue'],
		alias: {
			'utilities': path.resolve(__dirname, 'src/utilities/')
		}
	},

	plugins: [
		new webpack.LoaderOptionsPlugin({
			minimize: true,
			debug: true
		}),
		new webpack.optimize.UglifyJsPlugin({
			compress: {
				warnings: false,
				drop_console: false
			}
		}),
		new ExtractTextPlugin('app.css'),
		new webpack.DefinePlugin({
			'process.env.NODE_ENV': '"production"'
		}),
		new webpack.optimize.CommonsChunkPlugin({
			name: 'common',
			filename: 'common.js'
		}),

		new webpack.HotModuleReplacementPlugin(),
		new HtmlWebpackPlugin({
			title: 'react ui component',
			addLinkCss: ['/dist/styles/iconfont.css'],
			template: './template/index.ejs',
			hash: true
		})
	]
}


module.exports = config