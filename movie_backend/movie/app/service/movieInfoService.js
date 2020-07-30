"use strict";

const Service = require("egg").Service;

class MovieInfoService extends Service {
  async getMovieInfo(param) {
    const { itemsPerPage, page } = param;
    const offsetOfItem = itemsPerPage * (page - 1);
    const queryMovieSQL =
      "select * from movieInfo where genre not like '%动画%' and genre not like '%纪录片%' and genre not like '%真人秀%' and tag = '电影' order by rate desc limit ? offset ?";
    const movieInfo = await this.app.mysql.query(queryMovieSQL, [
      itemsPerPage,
      offsetOfItem,
    ]);
    return movieInfo;
  }
}

// module.exports = MovieInfoService;
