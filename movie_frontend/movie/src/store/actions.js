const actions = {
  getMovieInfo({ commit }, param) {
    const { reqParam, api } = param;
    return new Promise((resolve, reject) => {
      this._vm.get(api, reqParam).then(res => {
        if (res.success) {
          commit("getMovieInfo", res.data);
          resolve(res);
        }
      });
    });
  }
};

export default actions;
