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
    getIntroduction() {
      this.summary = this.movieInfo.summary.replace(/\s/g, "");
      this.title = `本片上映于${this.getTargetItem(
        this.movieInfo.release_date,
        1
      )}${
        !this.movieInfo.release_date.includes("-") &&
        !this.movieInfo.release_date.includes(")")
          ? "年"
          : ""
      }，由${this.getTargetItem(
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
    getMovieInfo() {
      this.id =
        this.$store.state.selectedMovie.id || sessionStorage.getItem("movieid");
      sessionStorage.setItem("movieid", this.id);
      this.$store.dispatch("getResSelectedMovie", this.id).then((res) => {
        if (res.success) {
          this.movieInfo = res.data;
          this.getIntroduction();
        }
      });
    },
  },
  created() {
    this.getMovieInfo();
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
  // animation: zoomIn;
  // animation-duration: 1s;

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
    line-height: 1.4rem;
    font-size: 1rem;
    opacity: 1;

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