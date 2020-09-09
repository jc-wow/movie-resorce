import Vue from "vue";
import VueRouter from "vue-router";
import Main from "@/components/Main/Main";
import MovieDetail from "@/components/Movie/MovieDetail";

Vue.use(VueRouter);

const routes = [
  {
    path: "/",
    name: "main",
    component: Main,
    children: [
    	{
    		path: 'movie',
    		component: MovieDetail,
    		name: 'movie'
			}
    ]
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
  if (to.name === "" && from.name === "") next({ name: "main" });
  else next();
});

export default router;
