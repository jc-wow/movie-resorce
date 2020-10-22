import Vue from "vue";

const utils = {
  /**
   * format 'YYYY-MM-DD T hh:mm Z' to 'YYYY-MM-DD hh:mm'
   * @param {Date} date
   */
  formatDate(date) {
    return Vue.prototype.Day(date).format("YYYY-MM-DD HH:mm");
  },
  /**
   * test user email valid
   * @param {String} res
   */
  testEmailValid(res) {
    const pattern = /^([A-Za-z0-9_\-\.\u4e00-\u9fa5])+\@([A-Za-z0-9_\-\.])+\.([A-Za-z]{2,8})$/;
    return pattern.test(res);
  },
};

export default utils;
