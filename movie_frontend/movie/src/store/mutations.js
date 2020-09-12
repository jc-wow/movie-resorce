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
};

export default mutations;
