'use strict'

var path = require('path')

/**
 * import file entry
 * @type {{index: string, details: string}|exports|module.exports}
 */
var webpack = require('webpack')
var WebpackDevServer = require('webpack-dev-server')

// extract comment css
var HtmlWebpackPlugin = require('html-webpack-plugin')
var node_modules = path.resolve(__dirname, 'node_modules')
var pathToSrc = path.resolve(__dirname, 'src')
var pathToBuild = path.resolve(__dirname, 'dist')

var config = {
    // pathToBuild: pathToBuild
    devtool: 'source-map',
    // entry file config
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

    /**
     * output file config
     * path: the file output absolute path
     * path + publicPath: http://127.0.0.1:8989/index.html
     */
    output: {
        path: path.resolve(__dirname, 'dist'),
        chunkFilename: '[name].js',
        filename: '[name].js',
        publicPath: '/'
    },
    module: {
        rules: [{
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
                use: [
                    'style-loader',
                    'css-loader',
                    'less-loader'
                ]
            },
            {
                test: /\.(ttf|eot|svg|woff(2)?)(\?[a-z0-9=&.]+)?$/,
                loader: 'file-loader'
            }
        ]
    },
    resolve: {
        extensions: ['.js', '.ts', '.vue'],
        alias: {
            'components': path.resolve(__dirname, 'src/components/'),
            'utilities': path.resolve(__dirname, 'src/utilities/')
        }
    },
    plugins: [
        new webpack.LoaderOptionsPlugin({
            minimize: true,
            debug: true
        }),
        new webpack.optimize.CommonsChunkPlugin({
            name: 'common',
            filename: 'common.js'
        }),
        new webpack.HotModuleReplacementPlugin(),
        new HtmlWebpackPlugin({
            title: 'vue ui components',
            addLinkCss: ['/styles/iconfont.css'],
            template: './template/index.ejs',
            hash: true
        })
    ]
}


module.exports = config