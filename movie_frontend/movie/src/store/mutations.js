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
};

export default mutations;
