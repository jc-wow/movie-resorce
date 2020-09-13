"use strict";

module.exports = (app) => {
  const { STRING } = app.Sequelize;

  const Movie = app.model.define(
    "movies",
    {
      id: { type: STRING, primaryKey: true },
      title: STRING,
      rate: STRING,
      cover: STRING,
    },
    {
      tableName: "movies",
      timestamps: false,
    }
  );

  return Movie;
};
