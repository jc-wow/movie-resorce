import Vue from "vue";
import Vuex from "vuex";
import actions from "./actions";
import mutations from "./mutations";

Vue.use(Vuex);

export default new Vuex.Store({
  state: {
    movieInfo: [], // movie data array
    menuIsShowing: false, // menu show flag
    curPage: "", // current menu
    selectedMovie: {}, // current selected movie
    resSelectedMovie: {}, // current selected movie which request from api
    selectedDiscuss: {}, // current selected discuss
    resPostDiscuss: "", // response after post a new discuss
    allDiscuss: [], // all discuss from api request,
    discussReply: [],
    userInfo: {
      email: "",
      author: ""
		},
		movieInfoByTime: [],
		movieInfoByYear: [],
		curSelectYear: ''
	},
  mutations,
  actions,
  modules: {}
});
