"use strict";
module.exports = {
  up: async (queryInterface, Sequelize) => {
    await queryInterface.createTable("chiniese_movies", {
      id: {
        type: Sequelize.STRING,
        allowNull: false,  
        primaryKey: true,
      },
      title: {
        type: Sequelize.STRING(50),
      },
      rate: {
        type: Sequelize.STRING(50),
      },
      url: {
        type: Sequelize.STRING(2000),
      },
      cover: {
        type: Sequelize.STRING(2000),
      },
      director: {
        type: Sequelize.STRING(500),
      },
      actor: {
        type: Sequelize.STRING(500),
      },
      genre: {
        type: Sequelize.STRING(500),
      },
      produce_area: {
        type: Sequelize.STRING(500),
      },
      language: {
        type: Sequelize.STRING(100),
      },
      release_date: {
        type: Sequelize.STRING(200),
      },
      runtime: {
        type: Sequelize.STRING(100),
      },
      other_name: {
        type: Sequelize.STRING(200),
      },
      imdb: {
        type: Sequelize.STRING(500),
      },
      official_site: {
        type: Sequelize.STRING(200),
      },
      rating_sum: {
        type: Sequelize.STRING(50),
      },
      ratings_on_weight: {
        type: Sequelize.STRING(50),
      },
      summary: {
        type: Sequelize.TEXT,
      },
      award: {
        type: Sequelize.STRING(200),
      },
      short_comment: {
        type: Sequelize.STRING(3000),
      },
      original_photo: {
        type: Sequelize.STRING(2000),
      },
      similer_like: {
        type: Sequelize.TEXT,
      },
      tag: {
        type: Sequelize.STRING(500),
      },
      ost: {
        type: Sequelize.STRING(2000),
      },
      created_at: {
        type: Sequelize.DATE,
      },
      updated_at: {
        type: Sequelize.DATE,
      },
    });
  },
  down: async (queryInterface, Sequelize) => {
    await queryInterface.dropTable("chiniese_movies");
  },
};
