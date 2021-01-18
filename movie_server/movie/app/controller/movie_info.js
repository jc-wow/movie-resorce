"use strict";

const Controller = require("./base");

class MovieInfoController extends Controller {
  async getMovieInfoByTime() {
    const { time, offset, limit } = this.ctx.query;
    this.ctx.body = await this.ctx.service.movieInfo.getMovieInfoByTime({
      time,
      offset,
      limit,
    });
    this.success(this.ctx.body);
  }

  async getVideo() {
    const ctx = this.ctx;
    const { id } = ctx.query;
    this.ctx.body = await this.ctx.service.movieInfo.getVideo(id);
    this.success(this.ctx.body);
  }

  async getRandomMovie() {
		this.ctx.body = await this.ctx.service.movieInfo.getRandomMovie();
		this.success(this.ctx.body);
  }
}

module.exports = MovieInfoController;
