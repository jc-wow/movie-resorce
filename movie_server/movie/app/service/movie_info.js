"use strict";

const Service = require("egg").Service;
const { Op } = require("sequelize");

class MovieInfo extends Service {
  async getMovieInfoByTime(param) {
    let options = {};
    const { time, offset, limit } = param;
    // get info by year
    if (time.length === 4) {
      options = {
        attributes: ["title", "cover", "director", "actor", "summary"],
        order: [["rate", "DESC"]],
        offset: parseInt(offset),
        limit: parseInt(limit),
        where: {
          release_date: {
            [Op.like]: `${time}%`,
          },
        },
      };
    } else {
      // get info by time
      options = {
        attributes: ["title", "cover", "id"],
        order: [["rate", "DESC"]],
        offset: parseInt(offset),
        limit: parseInt(limit),
        where: {
          release_date: {
            [Op.like]: time === "18" ? `${time}%` : `%${time}%`,
          },
        },
      };
    }
    return this.ctx.model.MovieInfo.findAndCountAll(options);
  }

  async getVideo(param) {
    return this.ctx.model.MovieInfo.findByPk(param);
  }
}

module.exports = MovieInfo;
