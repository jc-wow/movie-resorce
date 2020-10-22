"use strict";

/**
 * @param {Egg.Application} app - egg application
 */
module.exports = (app) => {
  const { router, controller } = app;
  router.resources("movies", "/api/movie", controller.movie);
  router.resources("movie", "/api/movie/:id", controller.movie);
  router.resources("discusses", "/api/discuss", controller.discuss);
  router.resources("discuss", "/api/discuss/:id", controller.discuss);
  router.resources("reply", "/api/discuss_reply/:id", controller.discussReply);
  router.post(
    "reply",
    "/api/discuss_reply/:id/update",
    controller.discussReply.update
  );
};
