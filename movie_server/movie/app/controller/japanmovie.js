"use strict";

const Controller = require("./base");

class JapanMovieController extends Controller {
  async index() {
    const ctx = this.ctx;
    const { page, limit } = ctx.query;
    const query = {
      limit: parseInt(limit),
      page: parseInt(page),
    };
    const model = "Japanmovie";
    ctx.body = await ctx.service.movie.list(query, model);
    this.success(ctx.body);
  }
}

module.exports = JapanMovieController;
