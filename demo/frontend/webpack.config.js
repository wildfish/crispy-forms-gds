const path = require('path');

const { CleanWebpackPlugin } = require('clean-webpack-plugin');
const CopyPlugin = require('copy-webpack-plugin');

const pathDist = `dist`;
const pathDistGov = path.resolve(__dirname, pathDist, 'govuk');


const config = {

  entry: {
    'index': [`./src/index.js`, `./src/index.scss`],
  },

  output: {
    path: path.resolve(__dirname, pathDist),
    publicPath: `/${pathDist}/`,
    filename: '[name].js'
  },

  plugins: [
    // Remove built js and css from the dist folder before building
    new CleanWebpackPlugin({
      cleanOnceBeforeBuildPatterns: ['**/*', '!.gitkeep'],
    }),
    // Copy GOV.UK assets into the dist path without modifying
    new CopyPlugin({
        patterns: [{
            context: path.resolve(__dirname, 'node_modules/govuk-frontend/govuk/assets'),
            from: '**/*',
            to: pathDistGov,
        }],
    }),
  ],

  module: {
    rules: [
      {
        test: /\.scss$/,
        use: [
          'style-loader',
          'css-loader',
          {
            loader: 'sass-loader',
            options: {
              sassOptions: {
                includePaths: ['./node_modules'],
              },
            },
          },
        ],
      },
    ],
  },
};

module.exports = (env, argv) => {
  return config;
}
