"use strict";

/**
 * @param {Egg.Application} app - egg application
 */
module.exports = (app) => {
  const { router, controller } = app;
  router.resources("chiniesemovies", "/chiniesemovies", controller.chiniesemovie);
};
