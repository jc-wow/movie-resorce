"use strict";

const Service = require("egg").Service;

class DiscussReply extends Service {
  async listAll(param) {
    const option = {
      attributes: ["id", "author", "content", "updated_at"],
      where: {
        rid: param.rid,
      },
    };
    return this.ctx.model.DiscussReply.findAndCountAll(option);
  }

  async create(param) {
    return this.ctx.model.DiscussReply.create(param);
  }
}

module.exports = DiscussReply;
