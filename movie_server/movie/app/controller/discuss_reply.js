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
      reply: ctx.reply,
      reply_author: ctx.reReplyAuthor,
      reply_email: ctx.reReplyEmail,
    };
    await this.ctx.service.discussReply.create(param);
    this.ctx.body = {
      success: true,
    };
    // update discuss table total column after insert a new reply to discuss
    this.ctx.service.discussReply.updateTotalReply(ctx.rid);
  }

  async update() {
    const param = this.ctx.request.body;
    try {
      await this.ctx.service.discussReply.updateDiscussRereply(param);
      this.ctx.body = {
        success: true,
      };
    } catch (err) {
      this.ctx.body = {
        success: false,
      };
    }
  }
}

module.exports = DiscussReplyController;
