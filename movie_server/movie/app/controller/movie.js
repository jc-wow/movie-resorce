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
    ctx.body = await ctx.service.movie.listAll(query);
    this.success(ctx.body);
  }

  async show() {
    const ctx = this.ctx;
    const { id } = ctx.query;
    ctx.body = await ctx.service.movie.listOne(id);
    this.success(ctx.body);
	}
	
	async search() {
		const ctx = this.ctx.request.body;
	}
}

module.exports = MovieController;
