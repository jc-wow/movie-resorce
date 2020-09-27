const actions = {
  /* movie api */
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
  /* discuss api */
  postDiscuss({ commit }, param) {
    return new Promise((resolve, reject) => {
      this._vm.post("/discuss", param).then((res) => {
        if (res.success) {
          commit("getResPostDiscuss", res.data);
          resolve(res);
        } else {
          this._vm.$message.error("抱歉，程序猿开了小差~");
        }
      });
    });
  },
  getAllDiscuss({ commit }, param) {
    return new Promise((resolve, reject) => {
      this._vm.get("/discuss", param).then((res) => {
        if (res.success) {
          commit("getAllDiscuss", res.data);
          resolve(res);
        } else {
          this._vm.$message.error("抱歉，程序猿开了小差~");
        }
      });
    });
  },
  updateDiscuss({ commit }, param) {
    return new Promise((resolve, reject) => {
      this._vm.put(`/discuss/${param.id}`).then((res) => {
        if (res.success) {
          commit("getResPostDiscuss", res.data);
          resolve(res);
        } else {
          this._vm.$message.error("抱歉，程序猿开了小差~");
        }
      });
    });
  },
};

export default actions;
