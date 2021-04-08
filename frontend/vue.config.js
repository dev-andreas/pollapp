module.exports = {
    publicPath:
        process.env.NODE_ENV === 'production'
            ? '/static/dist/'
            : 'http://127.0.0.1:8080',

    pages: {
        base: { // Should be used if you want to include TailwindCSS to Django template without Vue.js.
            entry: 'src/pages/base/base.js',
            template: 'public/index.html',
            filename: '../../templates/vue/base.html',
            title: 'Pollapp',
            chunks: ['chunk-vendors', 'chunk-common', 'base']
        },
        
        user: {
            entry: 'src/pages/user/main.js',
            template: 'public/index.html',
            filename: '../../templates/vue/user.html',
            title: 'Pollapp',
            chunks: ['chunk-vendors', 'chunk-common', 'user']
        }
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