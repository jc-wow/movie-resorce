import Vue from "vue";
import VueRouter from "vue-router";
import StartPage from "@/components/StartPage";
import Movie from "@/components/Movie/MovieMain";

Vue.use(VueRouter);

const routes = [
  {
    path: "/movie",
    name: "movie",
    component: Movie
  },
  {
    path: "/startPage",
    name: "startPage",
    component: StartPage
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
  if (to.path === "/" && from.path === "/") next({ path: "/startPage" });
  else next();
});

export default router;
