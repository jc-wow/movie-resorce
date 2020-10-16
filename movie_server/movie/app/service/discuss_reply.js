"use strict";

const { sequelize } = require("../../config/plugin");

const Service = require("egg").Service;

class DiscussReply extends Service {
  async listAll(param) {
    const option = {
      attributes: ["id", "author", "content", "updated_at", "email"],
      where: {
        rid: param.rid,
      },
    };
    return this.ctx.model.DiscussReply.findAndCountAll(option);
  }

  async create(param) {
    return this.ctx.model.DiscussReply.create(param);
  }

  async total(rid) {
    const option = {
      attributes: [
        "rid",
        [this.ctx.model.fn("COUNT", this.ctx.model.col("rid")), "rid_counts"],
      ],
      where: {
        rid,
      },
      group: "rid",
      raw: true,
    };
    return this.ctx.model.DiscussReply.findAll(option);
  }

  async updateTotalReply(rid) {
    const totalOfReply = await this.total(rid);
    if (totalOfReply.length === 0) return;
    this.updateReplyOfDiscussTable(totalOfReply[0]);
  }

  async updateReplyOfDiscussTable(param) {
    const { rid, rid_counts } = param;
    this.ctx.model.Discuss.update(
      { reply: rid_counts },
      {
        where: { id: rid },
      }
    );
  }
}

module.exports = DiscussReply;
