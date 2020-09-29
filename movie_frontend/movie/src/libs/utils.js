import Vue from "vue";

const utils = {
	/**
	 * format 'YYYY-MM-DD T hh:mm Z' to 'YYYY-MM-DD hh:mm'
	 * @param {Date} date 
	 */
  formatDate(date) {
    return Vue.prototype.Day(date).format("YYYY-MM-DD HH:mm");
  }
};

export default utils;
