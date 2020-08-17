"use strict";

const Service = require("egg").Service;

class MovieInfo extends Service {
  async getMovieInfo(param) {
    const { itemsPerPage, page } = param;
    const offsetOfItem = itemsPerPage * (page - 1);
    const option = {
      attributes: ["id", "title", "cover"],
    };
    return MovieInfo;
  }
}

module.exports = MovieInfo;
