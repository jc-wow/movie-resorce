const actions = {
  getMovieInfo({ commit }, param) {
    return new Promise((resolve, reject) => {
      this._vm.get('movie', param).then(res => {
        if (res.success) {
          commit("getMovieInfo", res.data);
          resolve(res);
        }
      });
    });
  }
};

export default actions;
