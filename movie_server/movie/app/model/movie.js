"use strict";

module.exports = (app) => {
  const { STRING } = app.Sequelize;

  const Movie = app.model.define(
    "movie",
    {
      id: { type: STRING, primaryKey: true },
      title: STRING,
      cover: STRING,
    },
    {
      tableName: "movieInfo",
      timestamps: false,
    }
  );

  return Movie;
};
