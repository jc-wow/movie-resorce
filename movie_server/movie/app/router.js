"use strict";

/**
 * @param {Egg.Application} app - egg application
 */
module.exports = (app) => {
  const { router, controller } = app;
  router.resources("movie", "/movie", controller.movie);
  router.resources("movie", "/movie/:id", controller.movie);
  router.resources("discuss", "/discuss", controller.discuss);
  router.resources("discuss", "/discuss/:id", controller.discuss);
};
