"use strict";

module.exports = (app) => {
  const { STRING } = app.Sequelize;

  const ChinieseMovie = app.model.define(
    "chiniesemovie",
    {
      id: { type: STRING, primaryKey: true },
      title: STRING,
      rate: STRING,
    },
    {
      tableName: "chiniese_movies",
      timestamps: false,
    }
  );

  return ChinieseMovie;
};
