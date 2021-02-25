const path = require("path"),
  webpack = require("webpack"),
  ExtractTextPlugin = require("extract-text-webpack-plugin"),
  CopyWebpackPlugin = require("copy-webpack-plugin"),
  CompressionPlugin = require("compression-webpack-plugin");

module.exports = {
  lintOnSave: false,
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
        test: /\.(png|jpg|gif|svg)$/,
        loader: "file",
        options: {
          name: "assets/images/[name].[ext]?[hash]"
        }
      }
    ]
  },
  resolve: {
    alias: {
      vue$: "vue/dist/vue"
    },
    extensions: [".js", ".vue"]
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
    new webpack.HotModuleReplacementPlugin(),
    new webpack.NoErrorsPlugin(),
    new CopyWebpackPlugin([{ from: "src/index.html" }], { copyUnmodified: true }),
    new CompressionPlugin({
      /* [file]被替换为原始资产文件名。
         [path]替换为原始资产的路径。
         [dir]替换为原始资产的目录。
         [name]被替换为原始资产的文件名。
         [ext]替换为原始资产的扩展名。
         [query]被查询替换。*/
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
    })
  ]
};
