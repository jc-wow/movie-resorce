const mutations = {
  getMovieInfo(state, movieInfo) {
    state.movieInfo = movieInfo;
  },
  showMenu(state) {
    state.menuIsShowing = !state.menuIsShowing;
  },
  getCurPage(state, val) {
    state.curPage = val;
  },
  getSelectedMovie(state, val) {
    state.selectedMovie = val;
  },
  getResSelectedMovie(state, val) {
    state.resSelectedMovie = val;
  },
  getSelectedDiscuss(state, val) {
    state.selectedDiscuss = val;
  },
  getResPostDiscuss(state, val) {
    state.resPostDiscuss = val;
  },
  getAllDiscuss(state, val) {
    state.allDiscuss = val;
  },
  getDiscussReply(state, val) {
    state.discussReply = val;
  },
  getUserInfo(state, val) {
    const key = Object.keys(val)[0];
    state.userInfo[key] = val[key];
	},
	getMovieInfoByTime(state, val) {
		state.movieInfoByTime = val;
	},
	getMovieInfoByYear(state, val) {
		state.movieInfoByYear = val;
	},
	getCurSelectYear(state, val) {
		state.curSelectYear = val;
	}
};

export default mutations;
