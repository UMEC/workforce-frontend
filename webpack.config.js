const path = require('path');


module.exports = {
  entry: "./src/Main.ts",
  output: {
      filename: "bundle.js",
      path: path.resolve(__dirname, 'dist')
  },

  // Enable sourcemaps for debugging webpack's output.
  devtool: "source-map",
	mode: 'development',

  resolve: {
      // Add '.ts' and '.tsx' as resolvable extensions.
      extensions: [ ".webpack.js", ".web.js", ".ts", ".tsx", ".js"]
  },

  module: {
      rules: [
          // All files with a '.ts' or '.tsx' extension will be handled by 'awesome-typescript-loader'.
          { test: /\.tsx?$/, loader: "awesome-typescript-loader" },
          // All output '.js' files will have any sourcemaps re-processed by 'source-map-loader'.
          { test: /\.js$/, loader: "source-map-loader" }
      ]
  
        },

  // Other options...
};
