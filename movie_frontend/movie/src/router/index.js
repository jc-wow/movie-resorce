import Vue from "vue";
import VueRouter from "vue-router";


const Main = () => import("@/components/Main/Main");
const Discuss = () => import("@/components/Discuss/Discuss");
const EditDiscuss = () => import("@/components/Discuss/EditDiscuss");
const DiscussDetail = () => import("@/components/Discuss/DiscussDetail");

Vue.use(VueRouter);

const routes = [
  {
    path: "/",
    name: "main",
    component: Main
  },
  {
    path: "/discuss",
    component: Discuss,
    name: "discuss"
  },
  {
    path: "/discuss/new",
    component: EditDiscuss,
    name: "editDiscuss"
  },
  {
    path: "/discuss/:id",
    component: DiscussDetail,
    name: "discussDetail"
  }
  // route level code-splitting
  // this generates a separate chunk (about.[hash].js) for this route
  // which is lazy-loaded when the route is visited.
  // component: () => import(/* webpackChunkName: "about" */ '../views/About.vue'),
];

const scrollBehavior = (to, from, savedPosition) => {
  if (to.name === "discuss") {
    return {
      x: 0,
      y: 0
    };
  }
};

const router = new VueRouter({
  mode: "history",
  base: process.env.BASE_URL,
  routes,
  scrollBehavior
});

router.beforeEach((to, from, next) => {
  if (to.name === "" && from.name === "") {
    next({ name: "main" });
  } else next();
});

export default router;
