"use strict";

const Service = require("egg").Service;

class Discuss extends Service {
  async listAll(param) {
    const { limit, page } = param;
    const offset = limit * (page - 1);
    const options = {
      attributes: [
        "id",
        "title",
        "author",
        "tag",
        "email",
        "content",
        "reply",
        "updated_at",
      ],
      offset,
      limit,
      order: [["updated_at", "DESC"]],
    };
    return this.ctx.model.Discuss.findAndCountAll(options);
  }

  async listOne(param) {
    return this.ctx.model.Discuss.findByPk(param);
  }

  async create(param) {
    return this.ctx.model.Discuss.create(param);
  }
}

module.exports = Discuss;
