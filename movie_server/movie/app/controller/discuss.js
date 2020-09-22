"use strict";

const Controller = require("./base");

class DiscussController extends Controller {
  async index() {
    const ctx = this.ctx;
    const { page, limit, id } = ctx.query;
    const query = {
      limit: parseInt(limit),
      page: parseInt(page),
      id,
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
	
	async create() {
		const ctx = this.ctx;
		
	}
}

module.exports = DiscussController;
