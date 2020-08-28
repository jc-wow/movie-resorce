"use strict";

module.exports = (app) => {
  const { STRING } = app.Sequelize;

  const KoreaMovies = app.model.define(
    "classicalmovie",
    {
      id: { type: STRING, primaryKey: true },
      title: STRING,
      rate: STRING,
      cover: STRING,
    },
    {
      tableName: "korea_movies",
      timestamps: false,
    }
  );

  return KoreaMovies;
};
