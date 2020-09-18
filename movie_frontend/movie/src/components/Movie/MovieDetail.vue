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
    <div class="movie-detail-info">
      <p class="movie-detail-info-p1">{{ summary }}</p>
      <p>{{ title }}</p>
    </div>
  </div>
</template>

<script>
export default {
  name: "MovieDetail",
  data() {
    return {
      movieInfo: {},
      isrefresh: false,
      summary: "",
      title: "",
    };
  },
  methods: {
    saveMovieInfo() {
      sessionStorage.setItem("movieInfo", JSON.stringify(this.movieInfo));
    },
    getIntroduction() {
      this.summary = this.movieInfo.summary.replace(/\s/g, "");
      this.title = `本片上映于${this.getTargetItem(
        this.movieInfo.release_date,
        1
      )}，由${this.getTargetItem(
        this.movieInfo.director,
        2
      )}执导，${this.getTargetItem(this.movieInfo.actor, 3)}主演。`;
    },
    getTargetItem(val, limit) {
      const length = val.split("/").length;
      if (length > 1) {
        const resArray = val.split("/").splice(0, limit);
        return resArray.join(`、`) + `${limit === 1 ? "" : "等"}`;
      } else {
        return val;
      }
    },
  },
  watch: {
    "$store.state.resSelectedMovie": function (newVal, oldVal) {
      this.movieInfo = newVal;
      this.getIntroduction();
    },
  },
  mounted() {
    this.savedMovieInfo = JSON.parse(sessionStorage.getItem("movieInfo"));
    if (
      (this.savedMovieInfo &&
        Object.keys(this.savedMovieInfo).length > 0 &&
        !this.$store.state.resSelectedMovie.id) ||
      window.ispopstate
    ) {
      this.movieInfo = this.savedMovieInfo;
      this.getIntroduction();
    }
    // set movie detail in sessionstorage
    // in case disappear when refresh page
    window.addEventListener("beforeunload", (e) => {
      e.preventDefault();
      this.saveMovieInfo();
    });
    window.addEventListener("popstate", (e) => {
      window.ispopstate = true;
      this.$store.commit("getSelectedMovie", null);
    });
    window.ispopstate = false;
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
  animation: zoomIn;
  animation-duration: 1s;

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
    text-align: justify;
    line-height: 2rem;
    text-indent: 2em;
    font-size: 1.1rem;
    opacity: 0.8;

    p {
      width: 86%;
      letter-spacing: 1px;
    }

    .movie-detail-info-p1 {
      margin-top: 7%;
    }
  }
}
</style>