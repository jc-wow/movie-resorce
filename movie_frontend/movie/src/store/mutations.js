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
	getSelectedMovieId(state, val) {
		state.selectedMovieId = val;
	}
};

export default mutations;
