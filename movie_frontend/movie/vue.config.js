const path = require("path");
const resolve = dir => path.join(__dirname, dir);
const IS_PROD = ["production", "prod"].includes(process.env.NODE_ENV);
const CompressionWebpackPlugin = require("compression-webpack-plugin");
const productionGzipExtensions = /\.(js|css|json|txt|html|ico|svg)(\?.*)?$/i;
const BundleAnalyzerPlugin = require("webpack-bundle-analyzer").BundleAnalyzerPlugin;

module.exports = {
  publicPath: IS_PROD ? process.env.VUE_APP_PUBLIC_PATH : "./", // 默认'/'，部署应用包时的基本 URL
  // outputDir: process.env.outputDir || 'dist', // 'dist', 生产环境构建文件的目录
  // assetsDir: "", // 相对于outputDir的静态资源(js、css、img、fonts)目录
  lintOnSave: false,
  // runtimeCompiler: true, // 是否使用包含运行时编译器的 Vue 构建版本
  productionSourceMap: IS_PROD, // 生产环境的 source map
  parallel: require("os").cpus().length > 1,
  pwa: {},
  configureWebpack: {
    resolve: {
      alias: {
        vue$: "vue/dist/vue"
      },
      extensions: [".js", ".vue", ".json"]
    },
    plugins: [
      new CompressionWebpackPlugin({
        filename: "[path].gz[query]",
        algorithm: "gzip",
        test: productionGzipExtensions,
        threshold: 10240,
        minRatio: 0.8
      })
    ]
  },
  chainWebpack: config => {
    if (IS_PROD) {
      config.module
        .rule("images")
        .test(/\.(png|jpe?g|gif|svg)(\?.*)?$/)
        .use("image-webpack-loader")
        .loader("image-webpack-loader")
        .options({
          mozjpeg: { progressive: true, quality: 65 },
          optipng: { enabled: false },
          pngquant: { quality: [0.65, 0.9], speed: 4 },
          gifsicle: { interlaced: false },
          webp: { quality: 75 }
        })
        .end()
        .rule("scss")
        .test(/\.vue$/)
        .use("css-loader")
        .loader("css-loader")
        .end()

      // 打包分析
      config.plugin("webpack-report").use(BundleAnalyzerPlugin, [
        {
          analyzerMode: "static"
        }
      ]);
    }
  }
};
