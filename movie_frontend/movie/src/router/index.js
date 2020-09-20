import Vue from "vue";
import VueRouter from "vue-router";
import Main from "@/components/Main/Main";
import MovieDetail from "@/components/Movie/MovieDetail";
import Discuss from "@/components/Discuss/Discuss";

Vue.use(VueRouter);

const routes = [
  {
    path: "/",
    name: "main",
    component: Main
  },
  {
    path: "/movie/:id",
    component: MovieDetail,
    name: "movie"
  },
  {
    path: "/discuss",
    component: Discuss,
    name: "discuss"
  }

  // route level code-splitting
  // this generates a separate chunk (about.[hash].js) for this route
  // which is lazy-loaded when the route is visited.
  // component: () => import(/* webpackChunkName: "about" */ '../views/About.vue'),
];

const router = new VueRouter({
  mode: "history",
  base: process.env.BASE_URL,
  routes
});

router.beforeEach((to, from, next) => {
  if (to.name === "" && from.name === "") {
    next({ name: "main" });
  } else next();
});

export default router;
