"use strict";

const Service = require("egg").Service;
const Sequelize = require("sequelize");

class MovieInfo extends Service {
  async getMovieInfoByTime(param) {
    let { time, offset, limit } = param;
    offset = limit * (offset - 1);
    const options = {
      attributes: [],
      order: [["rate", "DESC"]],
      limit: parseInt(limit),
      offset: parseInt(offset),
      where: {
        release_date: {},
      },
    };
    // get info by year or by years
    const reqTime = time.replace(/[a-z]+/, "");
    if (time.endsWith("s")) {
      options.attributes = ["title", "cover", "id", "release_date"];
      options.where.release_date = {
        [Sequelize.Op.like]: `${reqTime.slice(0, 3)}%`,
      };
    } else if (!time.endsWith("s") || reqTime === "19") {
      options.attributes = [
        "title",
        "cover",
        "director",
        "actor",
        "summary",
        "release_date",
        "id",
      ];
      options.where.release_date = {
        [Sequelize.Op.like]: reqTime === "19" ? `${18}%` : `${reqTime}%`,
      };
    }
    return this.ctx.model.MovieInfo.findAndCountAll(options);
  }

  async getVideo(param) {
    return this.ctx.model.MovieInfo.findByPk(param);
  }

  async getRandomMovie() {
    return this.ctx.model.MovieInfo.query(
      "select cover FROM movies_info order by rand() limit 1",
      { type: Sequelize.QueryTypes.SELECT }
    );
  }
}

module.exports = MovieInfo;
