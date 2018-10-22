const path = require('path')
const CleanWebpackPlugin = require('clean-webpack-plugin')
const HtmlWebpackPlugin = require('html-webpack-plugin')

module.exports = {
    entry: './src/index.js',
    mode: 'development',
    output: {
        filename: 'index.js',
        path: path.resolve(__dirname, 'dist')
    },
    devtool: 'inline-source-map',
    devServer: {
        contentBase: './dist',
        disableHostCheck: true
    },
    // plugins: [
    //     new CleanWebpackPlugin(['dist']),
    //     new HtmlWebpackPlugin({
    //         title: 'Development'
    //     })
    // ],
    module: {
        // rules: [{
        //     exclude: /node_modules/,
        //     use: {
        //         loader: 'babel-loader'
        //     }
        // }]
    }
}