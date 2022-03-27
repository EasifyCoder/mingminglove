// const { defineConfig } = require('@vue/cli-service')
// module.exports = defineConfig({
//   transpileDependencies: true
// })

module.exports = {
  //代理跨域
  devServer: {
    proxy: {
      '/api': {
        target: 'http://127.0.0.1:5000'
      }
    }
  }
}

