"use strict";

const Controller = require("./base");

class MovieInfoController extends Controller {
  async getMovieInfoByTime() {
    const { time } = this.ctx.query;
    this.ctx.body = await this.ctx.service.movieInfo.getMovieInfoByTime(time);
    this.success(this.ctx.body);
  }
}

module.exports = MovieInfoController;
