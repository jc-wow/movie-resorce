"use strict";

const Controller = require("./base");

class MovieController extends Controller {
  async index() {
    const ctx = this.ctx;
    const { page, limit, category } = ctx.query;
    const query = {
      limit: parseInt(limit),
      page: parseInt(page),
      category,
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
    const query = this.ctx.query;
    this.ctx.body = await this.ctx.service.movie.search(query);
    this.success(this.ctx.body);
  }
}

module.exports = MovieController;
