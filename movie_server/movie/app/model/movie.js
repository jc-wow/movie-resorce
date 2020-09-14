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
      director: STRING,
      actor: STRING,
      genre: STRING,
      produce_area: STRING,
      language: STRING,
      release_date: STRING,
      runtime: STRING,
      other_name: STRING,
      imdb: STRING,
      official_site: STRING,
      rating_sum: STRING,
      ratings_on_weight: STRING,
      summary: STRING,
      award: STRING,
      short_comment: STRING,
      original_photo: STRING,
      similar_like: JSON,
      tag: STRING,
      ost: STRING,
    },
    {
      tableName: "movies",
      timestamps: false,
    }
  );

  return Movie;
};
