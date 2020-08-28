"use strict";

/**
 * @param {Egg.Application} app - egg application
 */
module.exports = (app) => {
  const { router, controller } = app;
  router.resources(
    "chiniesemovies",
    "/chiniesemovies",
    controller.chiniesemovie
  );
  router.resources(
    "classicalmovies",
    "/classicalmovies",
    controller.classicalmovie
  );
  router.resources("koreamovies", "/koreamovies", controller.koreamovie);
  router.resources("japanmovies", "/japanmovies", controller.japanmovie);
};
