"use strict";

const { INTEGER } = require("sequelize");
const { TEXT } = require("sequelize");
const { DATE } = require("sequelize");

module.exports = (app) => {
  const { STRING } = app.Sequelize;

  const Movie = app.model.define(
    "discuss_reply",
    {
      id: { type: INTEGER, primaryKey: true, autoIncrement: true },
      rid: INTEGER(11),
      author: STRING(50),
      email: STRING(50),
      reply_email: STRING(50),
      reply_author: STRING(50),
      content: TEXT,
      reply: TEXT,
      created_at: DATE,
      updated_at: DATE,
    },
    {
      tableName: "discuss_replies",
    }
  );

  return Movie;
};
