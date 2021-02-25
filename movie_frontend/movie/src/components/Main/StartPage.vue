<template>
  <div class="start-page">
    <div class="video-head"></div>
    <div class="video-container">
    </div>
  </div>
</template>

<script>

export default {
  name: "startPage",
  data() {
    return {
      menuContent: ["切换首页", "关于首页"],
    };
  },
  methods: {
    getProjectPosition() {
      const projectObj = document.getElementsByClassName(
        "start-page-projector"
      )[0];
      const headerObj = document.getElementsByClassName("video-head")[0];
      const headerObjHeight = headerObj.getBoundingClientRect().height;
      const projectObjClient = projectObj.getBoundingClientRect();
      this.projectorPosition.x1 =
        projectObjClient.right -
        (projectObjClient.right - projectObjClient.left) / 2;
    },
    getMoviedetail() {
      const id = this.movies[0].id;
      this.$store.dispatch("getResSelectedMovie", id);
      this.$store.commit("getSelectedMovie", this.movies[0]);
      this.$router
        .push({ path: `/movie/${this.movies[0].title}` })
        .catch((err) => err);
    },
	},
	activated() {
		document.getElementsByClassName('start-page-video')[0].play();
	},
};
</script>

<style scoped lang="scss">
.start-page {
  width: 100%;
  height: 100vh;
  position: relative;

  .video-head {
    height: 8%;
  }

  .video-container {
    display: flex;
    justify-content: center;
    flex-direction: row;

    .start-page-video {
      position: absolute;
      height: 92%;
      width: 100%;
    }

    .start-page-about {
      position: absolute;
      top: 42%;
      left: 92%;
    }
  }

  .start-page-sidebar-container {
    width: 11%;
    height: 90%;

    .start-page-sidebar {
      margin-left: 40%;
      margin-top: 51%;

      .start-page-projector {
        width: 21%;
        opacity: 0.4;
      }
    }
  }
}
</style>
