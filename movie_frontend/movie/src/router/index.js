import Vue from "vue";
import VueRouter from "vue-router";
import Main from "@/components/Main/Main";

Vue.use(VueRouter);

const routes = [
  {
    path: "/main",
    name: "main",
    component: Main
  },

  // route level code-splitting
  // this generates a separate chunk (about.[hash].js) for this route
  // which is lazy-loaded when the route is visited.
  // component: () => import(/* webpackChunkName: "about" */ '../views/About.vue'),
];

const scrollBehavior = function(to, from, savedPosition) {
  // ...
};

const router = new VueRouter({
  mode: "history",
  base: process.env.BASE_URL,
  routes,
  scrollBehavior,
});

router.beforeEach((to, from, next) => {
  if (to.path === "/" && from.path === "/") next({ path: "/main" });
  else next();
});

export default router;
