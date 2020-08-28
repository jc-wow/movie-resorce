"use strict";

module.exports = (app) => {
  const { STRING } = app.Sequelize;

  const ClassicalMovies = app.model.define(
    "classicalmovie",
    {
      id: { type: STRING, primaryKey: true },
      title: STRING,
      rate: STRING,
      cover: STRING,
    },
    {
      tableName: "high_score_movies",
      timestamps: false,
    }
  );

  return ClassicalMovies;
};
