"use strict";

const Controller = require("./base");

class MovieController extends Controller {
  async index() {
    const ctx = this.ctx;
    const { page, limit, category } = ctx.query;
    const query = {
      limit: parseInt(limit),
      page: parseInt(page),
      category: category,
		};
    ctx.body = await ctx.service.movie.list(query);
    this.success(ctx.body);
  }
}

module.exports = MovieController;
