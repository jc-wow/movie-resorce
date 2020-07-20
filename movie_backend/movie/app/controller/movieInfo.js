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
    const movieInfo = await service.movieInfoService.getMovieInfo(passParam);
    this.success(movieInfo);
  }
}

module.exports = UserController;
