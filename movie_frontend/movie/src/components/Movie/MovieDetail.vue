<template>
  <div class="detail">
		{{ $store.state.selectedMovie.id }}
	</div>
</template>

<script>
export default {
  name: "MovieDetail",
  data() {
    return {
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
	color: #fff;
}
</style>