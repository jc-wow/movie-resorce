"use strict";

const Controller = require("./base");

class DiscussReplyController extends Controller {
  async index() {
    const ctx = this.ctx;
    const query = ctx.query;
    ctx.body = await ctx.service.discussReply.listAll(query);
    this.success(ctx.body);
  }

  async create() {
    const ctx = this.ctx.request.body;
    const param = {
      rid: ctx.rid,
      author: ctx.author,
      email: ctx.email,
      content: ctx.content,
    };
    await this.ctx.service.discussReply.create(param);
    this.ctx.body = {
      success: true,
    };
    this.ctx.service.discussReply.updateTotalReply(ctx.rid);
  }
}

module.exports = DiscussReplyController;
