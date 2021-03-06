import Axios from "axios";
import qs from "qs";

const instance = Axios.create({
  headers: {
    "Content-Type": "application/json",
  },
});

if (process.env.NODE_ENV === "development") {
  instance.defaults.baseURL = "http://127.0.0.1:7003/api/";
} else if (process.env.NODE_ENV === "debug") {
  instance.defaults.baseURL = "";
} else if (process.env.NODE_ENV === "production") {
  instance.defaults.baseURL = "https://1994movie.xyz/api/";
}

instance.defaults.timeout = 100000;

export default {
  install(Vue, option) {
    Vue.prototype.get = function(url, params) {
      return new Promise((resolve, reject) => {
        instance
          .get(url, {
            params: params,
          })
          .then((res) => {
            resolve(res.data);
          })
          .catch((error) => {
            reject(error);
          });
      });
    };
    Vue.prototype.post = function(url, params) {
      return new Promise((resolve, reject) => {
        instance
          .post(url, params)
          .then((res) => {
            resolve(res.data);
          })
          .catch((err) => {
            reject(err);
          });
      });
    };
    Vue.prototype.put = function(url, params) {
      return new Promise((resolve, reject) => {
        instance
          .put(url, params)
          .then((res) => {
            resolve(res.data);
          })
          .catch((err) => reject(err));
      });
    };
  },
};
