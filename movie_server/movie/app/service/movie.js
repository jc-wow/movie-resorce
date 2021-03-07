"use strict";

const Service = require("egg").Service;
const { Op } = require("sequelize");

class MovieInfo extends Service {
  async listAll(param) {
    const { limit, page, category } = param;
    const offset = limit * (page - 1);
    const options = {
      attributes: ["id", "rate", "title", "cover", "runtime", "genre"],
      offset,
      limit,
      order: [
        ["rate", "DESC"],
        ["id", "DESC"],
      ],
      where: {
        category,
      },
    };
    return this.ctx.model.Movie.findAll(options);
  }

  async listOne(param) {
    return this.ctx.model.Movie.findByPk(param);
  }

  async search(param) {
    const { key } = param;
    return this.ctx.model.MovieInfo.findAndCountAll({
      attributes: [
        "id",
        "title",
        "actor",
        "cover",
        "director",
        "release_date",
        "summary",
        "url",
        "imdb",
      ],
      order: [
        ["rate", "DESC"],
        ["id", "DESC"],
      ],
      offset: 0,
      limit: 20,
      where: {
        title: {
          [Op.substring]: key,
        },
      },
    });
  }
}

module.exports = MovieInfo;
