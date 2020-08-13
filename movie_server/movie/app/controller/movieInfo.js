"use strict";

const Controller = require("./base");

class UserController extends Controller {
  async index() {
    const { ctx, service } = this;
    const { page, itemsPerPage } = ctx.query;
    const passParam = {
      itemsPerPage: parseInt(itemsPerPage),
      page: parseInt(page),
    };
    ctx.body = await ctx.model.highScoreMovies.findAll();
    // console.log(ctx.body);
    // const movieInfo = await service.movieInfoService.getMovieInfo(passParam);
		console.log(ctx.body);
		this.success(ctx.body);
  }
}

module.exports = UserController;
