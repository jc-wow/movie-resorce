import Vue from "vue";
import ElementUI from "element-ui";
import "element-ui/lib/theme-chalk/index.css";
import axios from "axios";
import VueAxios from "vue-axios";
import API from "./libs/api";
import jQuery from "jquery";
import Utils from "@/libs/utils";
import animated from "animate.css";
import Day from "dayjs";
import "dayjs/locale/zh-cn";

import App from "./App.vue";
import router from "./router";
import store from "./store";

Vue.config.productionTip = false;
Vue.use(ElementUI);
Vue.use(VueAxios, axios);
Vue.use(API);
Vue.use(animated);

Day.locale("zh-cn");
const relativeTime = require("dayjs/plugin/relativeTime");
Day.extend(relativeTime);

global.$ = jQuery;
Vue.prototype.utils = Utils;
Vue.prototype.Day = Day;

new Vue({
  router,
  store,
  render: h => h(App)
}).$mount("#app");
