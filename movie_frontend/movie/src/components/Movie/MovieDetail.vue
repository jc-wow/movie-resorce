<template>
  <transition name="detail">
    <div class="detail" v-show="showDetail"></div>
  </transition>
</template>

<script>
export default {
  name: "MovieDetail",
  data() {
    return {
      showDetail: false,
    };
  },
  watch: {
    "$store.state.selectedMovieId": function (val) {
      this.showDetail = true;
    },
  },
};
</script>

<style lang="scss" scoped>
.detail {
  height: 100vh;
  width: 100%;
	position: absolute;
	top: 8vh;
	background-color: #000;
}

.detail-enter-active {
	transition: height 1s linear;
}

.detail-leave-active {
	transition: height 1s linear
}
</style>