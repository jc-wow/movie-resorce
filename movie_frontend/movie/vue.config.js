const path = require("path"),
  webpack = require("webpack"),
  ExtractTextPlugin = require("extract-text-webpack-plugin"),
  CopyWebpackPlugin = require("copy-webpack-plugin"),
  CompressionPlugin = require("compression-webpack-plugin"),
  ImageMinimizerPlugin = require("image-minimizer-webpack-plugin");

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
        test: /\.(gif|png|jpe?g|svg)$/i,
        use: [
          "file-loader",
          {
            loader: "image-webpack-loader",
            options: {
              bypassOnDebug: true, // webpack@1.x
              disable: true // webpack@2.x and newer
            }
          }
        ]
      },
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
      },
      {
        test: /\.(png|jpe?g|gif|svg)(\?.*)?$/,
        use: [
          {
            loader: "url-loader",
            options: {
              limit: 10000,
              name: utils.assetsPath("img/[name].[hash:7].[ext]")
            }
          },
          {
            loader: "image-webpack-loader",
            options: {
              bypassOnDebug: true
            }
          }
        ]
      }
    ]
  },
  resolve: {
    alias: {
      vue$: "vue/dist/vue",
      comp: path.resolve(__dirname, "src/components/")
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
    new ImageMinimizerPlugin({
      minimizerOptions: {
        // Lossless optimization with custom option
        // Feel free to experiment with options for better result for you
        plugins: [
          ["gifsicle", { interlaced: true }],
          ["jpegtran", { progressive: true }],
          ["optipng", { optimizationLevel: 5 }],
          [
            "svgo",
            {
              plugins: [
                {
                  removeViewBox: false
                }
              ]
            }
          ]
        ]
      }
    }),
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
