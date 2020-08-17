"use strict";

const Controller = require("./base");

class ChinieseMovieController extends Controller {
  async index() {
    const ctx = this.ctx;
    const { page, itemsPerPage } = ctx.query;
    const param = {
      itemsPerPage: parseInt(itemsPerPage),
      page: parseInt(page),
    };
    ctx.body = await ctx.model.Chiniesemovie.findAll();
    // const movieInfo = await service.movieInfoService.getMovieInfo(param);
    this.success(ctx.body);
  }
}

module.exports = ChinieseMovieController;
