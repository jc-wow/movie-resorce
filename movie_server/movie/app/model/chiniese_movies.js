'use strict';
const {
  Model
} = require('sequelize');
module.exports = (sequelize, DataTypes) => {
  class chiniese_movies extends Model {
    /**
     * Helper method for defining associations.
     * This method is not a part of Sequelize lifecycle.
     * The `models/index` file will call this method automatically.
     */
    static associate(models) {
      // define association here
    }
  };
  chiniese_movies.init({
    id: DataTypes.STRING
  }, {
    sequelize,
    modelName: 'chiniese_movies',
  });
  return chiniese_movies;
};