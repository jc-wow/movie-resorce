"use strict";

const { INTEGER } = require("sequelize");
const { TEXT } = require("sequelize");
const { DATE } = require("sequelize");

module.exports = (app) => {
  const { STRING } = app.Sequelize;

  const Movie = app.model.define(
    "discuss",
    {
      id: { type: INTEGER, primaryKey: true, autoIncrement: true },
      title: STRING(255),
      author: STRING(50),
      tag: STRING(100),
      content: TEXT,
      reply: TEXT,
      created_at: DATE,
      updated_at: DATE,
    },
    {
      tableName: "discusses",
    }
  );

  return Movie;
};
