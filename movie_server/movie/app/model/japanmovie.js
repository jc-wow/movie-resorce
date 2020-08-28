"use strict";

module.exports = (app) => {
  const { STRING } = app.Sequelize;

  const JapanMovies = app.model.define(
    "japanmovie",
    {
      id: { type: STRING, primaryKey: true },
      title: STRING,
      rate: STRING,
      cover: STRING,
    },
    {
      tableName: "japan_movies",
      timestamps: false,
    }
  );

  return JapanMovies;
};
