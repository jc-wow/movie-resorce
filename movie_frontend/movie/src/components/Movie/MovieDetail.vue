<template>
  <div class="movie-detail">
    <div class="movie-detail-video">
      <img
        class="movie-detail-video-img"
        :src="movieInfo.cover"
        referrerpolicy="no-referrer"
        object-fit="cover"
      />
    </div>
    <div class="movie-detail-info"></div>
  </div>
</template>

<script>
export default {
  name: "MovieDetail",
  data() {
    return {
      movieInfo: {},
    };
  },
  methods: {
    saveMovieInfo() {
			debugger
      sessionStorage.setItem("movieInfo", JSON.stringify(this.movieInfo));
    },
  },
  watch: {
    "$store.state.resSelectedMovie": function (newVal, oldVal) {
      this.movieInfo = newVal;
    },
  },
  mounted() {
    const movieInfo = JSON.parse(sessionStorage.getItem("movieInfo"));
    if (
      movieInfo &&
      Object.keys(movieInfo).length > 0 &&
      this.$store.state.resSelectedMovie.id !== movieInfo.id
    ) {
      this.movieInfo = movieInfo;
    }
    // set movie detail in sessionstorage data
    // in case disappear when refresh page
    window.addEventListener("beforeunload", (e) => {
      e.preventDefault();
      this.saveMovieInfo();
    });
  },
  destroyed() {
    window.removeEventListener("beforeunload", this.saveMovieInfo());
  },
};
</script>

<style lang="scss" scoped>
.movie-detail {
  height: 92vh;
  width: 100%;
  position: absolute;
  top: 8vh;
  background-color: #000;
  color: #fff;
  display: flex;
  flex-direction: row;

  .movie-detail-video {
    width: 40%;
    text-align: center;

    .movie-detail-video-img {
      transform: rotate(5deg);
      width: 55%;
      margin-top: 10%;
      opacity: 0.7;
    }
  }

  .movie-detail-info {
    width: 60%;
  }
}
</style>