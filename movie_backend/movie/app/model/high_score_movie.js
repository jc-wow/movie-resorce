'use strict';
const {
  Model
} = require('sequelize');
module.exports = (sequelize, DataTypes) => {
  class high_score_movie extends Model {
    /**
     * Helper method for defining associations.
     * This method is not a part of Sequelize lifecycle.
     * The `models/index` file will call this method automatically.
     */
    static associate(models) {
      // define association here
    }
  };
  high_score_movie.init({
    id: DataTypes.STRING
  }, {
    sequelize,
    modelName: 'high_score_movie',
  });
  return high_score_movie;
};