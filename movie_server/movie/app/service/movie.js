"use strict";

const Service = require("egg").Service;

class MovieInfo extends Service {
  async list(param) {
    const { limit, page } = param;
		const offset = limit * (page - 1);
		const options = {
			offset: offset,
			limit: limit,
			order: [['rate', 'DESC']]
		}
    return this.ctx.model.Chiniesemovie.findAll(options);
  }
}

module.exports = MovieInfo;
