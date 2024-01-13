const webpack = require('webpack')
const path = require('path')
const HtmlWebpackPlugin = require('html-webpack-plugin')
const MiniCssExtractPlugin = require('mini-css-extract-plugin')
const { CleanWebpackPlugin } = require('clean-webpack-plugin')

const production = process.env.NODE_ENV === 'production'

module.exports = {
    entry: [
        './src/index.jsx',
        './src/styles/index.scss'
    ],
    output: {
        path: path.resolve(__dirname, './dist'),
        filename: production ? '[contenthash].modern.js' : '[name].js',
        asyncChunks: true,
        clean: true
    },
    module: {
        rules: [
            {
                test: /\.(js|jsx)$/,
                exclude: /node_modules/,
                use: ['babel-loader'],
            },
            {
                test: /\.s(a|c)ss$/,
                exclude: /node_modules/,
                use: [
                    production ? MiniCssExtractPlugin.loader : 'style-loader',
                    {
                        loader: 'css-loader',
                        options: {
                            modules: true,
                            sourceMap: !production
                        }
                    },
                    {
                        loader: 'sass-loader',
                        options: {
                            sourceMap: !production
                        }
                    }
                ]
            },

        ],
    },
    resolve: {
        extensions: ['*', '.js', '.jsx', '.scss'],
    },
    plugins: [
        // TODO: НАДО ЧТО-ТО ДЕЛАТЬ СО СТАТИЧНЫМИ КАРТИНКАМИ
        new CleanWebpackPlugin(),
        new HtmlWebpackPlugin({
            title: 'TalentSpot',
            template: './public/index.html',
            favicon: './public/favicon.png'
        }),
        new MiniCssExtractPlugin({
            filename: production ? '[contenthash].modern.css' : '[name].css',
        }),
    ],
    devServer: {
        port: 3000,
        hot: true,
    },
    mode: production ? 'production' : 'development'
}
