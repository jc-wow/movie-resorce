"use strict";

const Controller = require("./base");

class DiscussReplyController extends Controller {
  async index() {
    const ctx = this.ctx;
    const { rid } = ctx.query;
    const query = {
      rid,
    };
    ctx.body = await ctx.service.discussReply.listAll(query);
    this.success(ctx.body);
  }

  async create() {
    const ctx = this.ctx.request.body;
    const param = {
      rid: ctx.rid,
      author: ctx.author,
      content: ctx.content,
    };
    await this.ctx.service.discussReply.create(param);
    this.ctx.body = {
      success: true,
    };
  }
}

module.exports = DiscussReplyController;
