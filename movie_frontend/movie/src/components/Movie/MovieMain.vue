<template>
  <div class="movie-main">
    <transition name="menu">
      <Menu v-show="menu"></Menu>
    </transition>
    <div class="movie-container">
      <InfoContainer :info="movieInfo" :curPage="requestParam.page" @paging="paging"></InfoContainer>
    </div>
  </div>
</template>

<script>
import { mapState } from "vuex";
import Menu from "../common/Menu";
import InfoContainer from "./InfoContainer";

export default {
  name: "Movie",
  components: {
    InfoContainer,
    Menu,
  },
  data() {
    return {
      movieInfo: [],
      dripPicInfo: [],
      imageContainerHeight: 0,
      requestParam: {
        page: 1,
        itemsPerPage: 15,
      },
    };
  },
  methods: {
    getMoveInfo() {
      this.$store.dispatch("getMovieInfo", this.requestParam).then(() => {
        this.getHighestScoreMovie;
      });
    },
    paging(direction, transDistance) {
			this.direction = direction;
      this.imgContainerEle = document.getElementsByClassName(
        "image-container"
			)[0];
      this.imgContainerEle.style.cssText = `transform: translatex(${transDistance}px)`;
      this.removeTransEvent();
      this.imgContainerEle.addEventListener("transitionend", this.ifReqAPI, false);
    },
    removeTransEvent() {
      this.imgContainerEle.removeEventListener(
        "transitionend",
        this.ifReqAPI,
        false
      );
    },
    ifReqAPI() {
      const lastEle = $(".image-container div:last");
      const disToRLeftDoc = lastEle.offset().left;
      if (this.direction === "down" && disToRLeftDoc < $(window).width()) {
        this.requestParam.page++;
        this.getMoveInfo();
      }
    },
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
    ...mapState({
      getHighestScoreMovie(status) {
        this.movieInfo.push(...status.movieInfo);
      },
    }),
    menu() {
      return this.$store.state.menuIsShowing;
    },
  },
  mounted() {
    this.getMoveInfo();
  },
  destroyed() {
    this.removeTransEvent();
  },
};
</script>

<style lang="scss" scoped>
@keyframes menu-slidein {
  from {
    transform: translateX(-100%);
  }
  to {
    transform: translateX(0);
  }
}

.movie-main {
  background-color: #000;
  position: relative;
  width: 100%;
  height: 100%;
  overflow-y: auto;

  .menu-enter-active {
    animation: 0.5s menu-slidein;
  }
  .menu-leave-active {
    animation: 0.5s menu-slidein reverse;
  }

  .movieInfo-menuLogo {
    position: absolute;
    height: 4%;
    margin: 2% 0 0 2%;
    z-index: 999;
  }

  .movie-container {
    margin-left: 6%;
    height: 35%;
    margin-top: 5%;
  }
}
</style>
