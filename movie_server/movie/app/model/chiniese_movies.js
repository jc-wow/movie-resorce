"use strict";


module.exports = (app) => {
  const { STRING, TEXT, JSONB } = app.Sequelize;

  const highScoreMovies = app.model.define(
    "highScoreMovies",
    {
      id: { type: STRING, primaryKey: true },
      title: STRING,
      rate: STRING,
    },
    {
      tableName: "high_score_movies",
      timestamps: false,
    }
  );

  return highScoreMovies;
};
