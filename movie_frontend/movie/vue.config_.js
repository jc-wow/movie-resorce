const path = require("path"),
  webpack = require("webpack"),
  ExtractTextPlugin = require("extract-text-webpack-plugin"),
  CopyWebpackPlugin = require("copy-webpack-plugin"),
  CompressionPlugin = require("compression-webpack-plugin"),
  BundleAnalyzerPlugin = require("webpack-bundle-analyzer");

module.exports = {
  lintOnSave: false,
  productionSourceMap: false,
  output: {
    path: path.join(__dirname, "dist"),
    publicPath: "/",
    filename: "/assets/js/build.js"
  },
  module: {
    rules: [
      {
        test: /\.vue$/,
        loader: "vue",
        options: {
          loaders: {
            css: ExtractTextPlugin.extract({
              loader: "css-loader",
              fallbackLoader: "vue-style-loader"
            })
          }
        }
      },
      {
        test: /\.js$/,
        loader: "babel",
        exclude: /node_modules/,
        query: {
          presets: ["es2015", "stage-0"]
        },
        include: "./src"
      },
      {
        test: /\.(png|jpe?g|webp|git|svg|)$/i,
        use: [
          {
            loader: `img-optimize-loader`,
            options: {
              compress: {
                // This will transform your png/jpg into webp.
                webp: true,
                disableOnDevelopment: true,
              },
            },
          },
        ],
      },
    ]
  },
  resolve: {
    alias: {
      vue$: "vue/dist/vue"
    },
    extensions: [".js", ".vue", ".json"]
  },
  vendors: {
    index: [
      "eventsource-polyfill",
      "webpack-hot-middleware/client?path=/__webpack_hmr&timeout=20000",
      "./src/main.js"
    ]
  },
  plugins: [
    new ExtractTextPlugin("/assets/css/style.css"),
    new webpack.optimize.OccurrenceOrderPlugin(),
    new BundleAnalyzerPlugin(),
    new webpack.HotModuleReplacementPlugin(),
    new webpack.NoErrorsPlugin(),
    new CopyWebpackPlugin([{ from: "src/index.html" }], { copyUnmodified: true }),
    new CompressionPlugin({
      filename: "[path].gz[query]",
      //压缩算法
      algorithm: "gzip",
      //匹配文件
      test: /\.js$|\.css$|\.html$/,
      //压缩超过此大小的文件,以字节为单位
      threshold: 10240,
      minRatio: 0.8,
      //删除原始文件只保留压缩后的文件
      deleteOriginalAssets: true
    }),
    new webpack.optimize.CommonsChunkPlugin({
      name: "vendor",
      minChunks: function(module, count) {
        return (
          module.resource &&
          /\.js$/.test(module.resource) &&
          module.resource.indexOf(path.join(__dirname, "../node_modules")) === 0
        );
      }
    }),
    // 抽取出代码模块的映射关系
    new webpack.optimize.CommonsChunkPlugin({
      name: "manifest",
      chunks: ["vendor"]
    })
  ]
};
