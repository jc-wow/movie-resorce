const actions = {
  getMovieInfo({ commit }, param) {
    return new Promise((resolve, reject) => {
      this._vm.get("movieInfo", param).then(res => {
        if (res.success) {
          commit("getMovieInfo", res.data);
          resolve();
        }
      });
    });
  }
};

export default actions;
