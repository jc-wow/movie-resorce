"use strict";

const Controller = require("./base");

class DiscussController extends Controller {
  async index() {
    const ctx = this.ctx;
    const { page, limit, id } = ctx.query;
    const query = {
      limit: parseInt(limit),
      page: parseInt(page),
      id,
    };
    ctx.body = await ctx.service.discuss.listAll(query);
    this.success(ctx.body);
  }

  async show() {
    const ctx = this.ctx;
    const { id } = ctx.query;
    ctx.body = await ctx.service.discuss.listOne(id);
    this.success(ctx.body);
  }

  async create() {
    const ctx = this.ctx.request.body;
    const param = {
      title: ctx.title,
      author: ctx.author,
      tag: ctx.tag,
      content: ctx.content,
      reply: ctx.reply,
    };
    await this.ctx.service.discuss.create(param);
    this.ctx.body = {
      success: true,
    };
  }
}

module.exports = DiscussController;
