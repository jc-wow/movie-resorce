"use strict";

const Service = require("egg").Service;
const Sequelize = require("sequelize");
const { Op } = require("sequelize");

class MovieInfo extends Service {
  async getMovieInfoByTime(param) {
    let { time, offset, limit, searchMovieKey } = param;
    offset = limit * (offset - 1);

    const options = {
      attributes: [
        "title",
        "cover",
        "director",
        "actor",
        "summary",
        "release_date",
        "id",
        "url",
        "imdb",
      ],
      order: [
        ["rate", "DESC"],
        ["id", "DESC"],
      ],
      limit: parseInt(limit),
      offset: parseInt(offset),
      where: {},
    };

    // get info by year or by years
    const reqTime = time.replace(/[a-z]+/, "");

    // check if has searchMovieKey
    if (searchMovieKey && searchMovieKey.length !== 0) {
      options.where.title = {
        [Op.substring]: searchMovieKey,
      };
    } else {
      if (time.endsWith("s")) {
        options.attributes = ["title", "cover", "id", "release_date"];
        options.where.release_date = {
          [Sequelize.Op.like]: `${reqTime.slice(0, 3)}%`,
        };
      } else if (!time.endsWith("s") || reqTime === "19") {
        options.where.release_date = {
          [Sequelize.Op.like]: reqTime === "19" ? `${18}%` : `${reqTime}%`,
        };
      }
    }

    return this.ctx.model.MovieInfo.findAndCountAll(options);
  }

  async getVideo(param) {
    return this.ctx.model.MovieInfo.findByPk(param);
  }

  async getRandomMovie() {
    return this.app.model.query(
      "select * FROM movies_info order by rand() limit 1",
      { type: Sequelize.QueryTypes.SELECT }
    );
  }
}
module.exports = MovieInfo;
