module.exports = {
    publicPath:
        process.env.NODE_ENV === 'production'
            ? '/static/dist/'
            : 'http://127.0.0.1:8080',

    pages: {
        base: {
            entry: 'src/pages/base/main.js',
            template: 'public/index.html',
            filename: '../../templates/vue/base.html',
            title: 'Pollapp',
            chunks: ['chunk-vendors', 'chunk-common', 'base']
        },
        index: {
            entry: 'src/pages/index/main.js',
            template: 'public/index.html',
            filename: '../../templates/vue/index.html',
            title: 'Index Page',
            chunks: ['chunk-vendors', 'chunk-common', 'index']
        },
    },

    outputDir: '../backend/static/dist',

    chainWebpack: (config) => {

        config.devServer
            .public("http://127.0.0.1:8080")
            .hotOnly(true)
            .headers({ "Access-Control-Allow-Origin": "*" })
            .writeToDisk((filePath) => filePath.endsWith(".html")); //NOTE THIS CHANGE HERE
    },
}