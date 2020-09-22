"use strict";

const Service = require("egg").Service;

class Discuss extends Service {
  async listAll(param) {
    const { limit, page, category } = param;
    const offset = limit * (page - 1);
    const options = {
      attributes: ["id", "rate", "title", "cover"],
      offset: offset,
      limit: limit,
      order: [
        ["rate", "DESC"],
        ["id", "DESC"],
      ],
      where: {
        category: category,
      },
    };
    return this.ctx.model.Discuss.findAll(options);
  }

  async listOne(param) {
    return this.ctx.model.Discuss.findByPk(param);
  }
}

module.exports = Discuss;
