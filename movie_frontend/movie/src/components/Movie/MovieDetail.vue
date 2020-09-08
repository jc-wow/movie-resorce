<template>
  <div class="detail"></div>
</template>

<script>
export default {
  name: "MovieDetail",
  data() {
    return {
      showDetail: false,
    };
  },
  mounted() {},
};
</script>

<style lang="scss" scoped>
.detail {
  height: 92vh;
  width: 100%;
  position: absolute;
  top: 8vh;
  background-color: #000;
}

.detail-enter-active {
  transition: height 1s linear;
}

.detail-leave-active {
  transition: height 1s linear;
}
</style>