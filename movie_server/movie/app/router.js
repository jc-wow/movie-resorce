"use strict";

/**
 * @param {Egg.Application} app - egg application
 */
module.exports = (app) => {
  const { router, controller } = app;
  router.resources("movies", "/movie", controller.movie);
  router.resources("movie", "/movie/:id", controller.movie);
  router.resources("discusses", "/discuss", controller.discuss);
  router.resources("discuss", "/discuss/:id", controller.discuss);
  router.resources("reply", "/discuss_reply/:id", controller.discussReply);
};
