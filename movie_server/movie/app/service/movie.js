"use strict";

const Service = require("egg").Service;

class MovieInfo extends Service {
  async list(param) {
    const { limit, page, category } = param;
    const offset = limit * (page - 1);
    const options = {
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
}

module.exports = MovieInfo;
