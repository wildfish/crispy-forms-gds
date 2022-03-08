const Path = require('path');
const { CleanWebpackPlugin } = require('clean-webpack-plugin');

const config = {

  entry: {
    'index': ['./src/index.js', './src/index.scss'],
  },

  output: {
    path: Path.resolve(__dirname, 'assets'),
    publicPath: '/assets/',
    filename: '[name].js'
  },

  plugins: [
    // Remove built js and css from the assets folder before building
    new CleanWebpackPlugin({
      cleanOnceBeforeBuildPatterns: ['**/*'],
    }),
  ],

  module: {
    rules: [
      {
        test: /\.s[ac]ss$/i,
        use: [
          'style-loader',
          'css-loader',
          'sass-loader',
        ],
      },
    ],
  },
};

module.exports = (env, argv) => {
  return config;
}
