﻿"use strict";

const Controller = require("./base");

class ChinieseMovieController extends Controller {
  async index() {
    const ctx = this.ctx;
    const { page, limit } = ctx.query;
    const query = {
      limit: parseInt(limit),
      page: parseInt(page),
		};
    ctx.body = await ctx.service.movie.list(query);
    this.success(ctx.body);
  }
}

module.exports = ChinieseMovieController;
