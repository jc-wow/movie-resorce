"use strict";

const Service = require("egg").Service;

class MovieInfo extends Service {
  async listAll(param) {
    const { limit, page, category } = param;
    const offset = limit * (page - 1);
    const options = {
      attributes: ["id", "rate", "title", "cover", "runtime", "genre"],
      offset: offset,
      limit: limit,
      order: [
        ["rate", "DESC"],
        ["id", "DESC"],
      ],
      where: {
        category: category,
      },
    };
    return this.ctx.model.Movie.findAll(options);
  }

  async listOne(param) {
    return this.ctx.model.Movie.findByPk(param);
  }
}

module.exports = MovieInfo;
