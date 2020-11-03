"use strict";

const Service = require("egg").Service;
const { Op } = require("sequelize");

class MovieInfo extends Service {
  async getMovieInfoByTime(time) {
		let whereClause = {};
		// get info by year
		if (time.length === 4) {
			whereClause = {
				release_date: {
					[Op.like]: `${time}%`
				}
			}
		}
		// get info by time
    if (parseInt(time) >= 196) {
      whereClause = {
        release_date: {
          [Op.like]: time === "18" ? `${time}%` : `%${time}%`,
        },
        tag: "电影",
      };
    } else {
      whereClause = {
        release_date: {
          [Op.like]: time === "18" ? `${time}%` : `%${time}%`,
        },
      };
    }
    const options = {
      attributes: ["title", "release_date", "cover"],
      order: [["rate", "DESC"]],
      where: whereClause,
    };
    return this.ctx.model.MovieInfo.findAll(options);
  }
}

module.exports = MovieInfo;
