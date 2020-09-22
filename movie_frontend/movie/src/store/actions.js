const actions = {
  getMovieInfo({ commit }, param) {
    return new Promise((resolve, reject) => {
      this._vm.get("movie", param).then((res) => {
        if (res.success) {
          commit("getMovieInfo", res.data);
          resolve(res);
        }
      });
    });
  },
  getResSelectedMovie({ commit }, id) {
    return new Promise((resolve, reject) => {
      this._vm.get(`movie/${id}`, { id: id }).then((res) => {
        if (res.success) {
          commit("getResSelectedMovie", res.data);
          resolve(res);
        }
      });
    });
  },
  postDiscuss({ commit }, param) {
    return new Promise((resolve, reject) => {
      this._vm.post("/discuss", param).then((res) => {
        if (res.success) {
          commit("getResPostDiscuss", res.data);
          resolve(data);
        }
      });
    });
  },
};

export default actions;
