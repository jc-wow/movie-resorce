<template>
  <div class="movie-main">
    <div class="movie-main-head"></div>
    <div class="movie-main-body" @click="showStartpage = !showStartpage">
      <div class="movie-container" v-for="(item, index) in category" :key="item.key">
        <InfoContainer :category="item"></InfoContainer>
      </div>
    </div>
  </div>
</template>

<script>
import InfoContainer from "./InfoContainer";

export default {
  name: "Movie",
  components: {
    InfoContainer,
  },
  data() {
    return {
      showStartpage: true,
      prev: window.scrollY,
      category: [
        {
          title: "经典",
          key: "classical",
          api: "classicalmovies",
        },
        {
          title: "华语",
          key: "chiniese",
          api: "chiniesemovies",
        },
        {
          title: "韩国",
          key: "korea",
          api: "koreamovies",
        },
        {
          title: "日本",
          key: "japan",
          api: "japanmovies",
        },
      ],
    };
  },
  methods: {
    /**
     * request API when the distance between scroll and
     * bottom of the page less than twenty percent.
     */
    getPositionOfScroll() {
      let windowHeight = $(window).height();
      let heightToBottomOfPage = 0.2 * windowHeight;
      let preDocHeight = 0;
      $(window).scroll(() => {
        let docHeight = $(document).height();
        let scrollTopHeight = $(window).scrollTop();
        if (
          scrollTopHeight + windowHeight > docHeight - heightToBottomOfPage &&
          docHeight > preDocHeight
        ) {
          this.getMoveInfo();
          preDocHeight = docHeight;
          this.requestParam.page += 1;
        }
      });
    },
  },
  computed: {
    menu() {
      return this.$store.state.menuIsShowing;
    },
  },
};
</script>

<style lang="scss">
.movie-main {
  background-color: #000;
  position: relative;
  width: 100%;
  height: auto;

  .movie-main-head {
    height: 8vh;
  }

  .movie-main-body {
    height: auto;

    .movieInfo-menuLogo {
      position: absolute;
      height: 4%;
      margin: 2% 0 0 2%;
      z-index: 999;
    }

    .movie-container {
      margin-left: 6%;
      height: 43vh;
      margin-top: 2%;
    }
  }
}
</style>
