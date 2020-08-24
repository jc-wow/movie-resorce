<template>
  <div class="movie-main">
    <transition name="menu">
      <Menu v-show="menu"></Menu>
    </transition>
    <div class="movie-main-header"></div>
    <div class="movie-main-body">
      <!-- <div class="zoom-container">
        <el-slider class="zoom" v-model="slideValue" :show-tooltip="false"></el-slider>
        <i class="el-icon-s-grid"></i>
      </div> -->
      <div class="movie-container">
        <InfoContainer
          :info="movieInfo"
          :curPage="requestParam.page"
          :category="category"
          @paging="paging"
        ></InfoContainer>
      </div>
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
      category: "电影",
      slideValue: 50,
      requestParam: {
        page: 1,
        limit: 15,
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
      this.imgContainerEle.addEventListener(
        "transitionend",
        this.ifReqAPI,
        false
      );
    },
    removeTransEvent() {
      this.imgContainerEle &&
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

<style lang="scss">
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

  .movie-main-header {
    height: 9%;
  }

  .movie-main-body {
    height: 91%;

    // .zoom-container {
    //   display: flex;
    //   flex-direction: row;
    //   align-items: center;
    //   width: 9%;
    //   margin-left: 90%;

    //   .zoom {
    //     width: 50%;

    //     .el-slider__runway {
    //       height: 2px;
    //       background-color: rgba(255, 255, 255, 0.5);

    //       .el-slider__bar {
    //         background-color: transparent;
    //       }

    //       .el-slider__button-wrapper {
    //         top: -17px;

    //         .el-slider__button {
    //           border: 0;
    //           width: 13px;
    //           height: 13px;
    //         }
    //       }
    //     }
    //   }

    //   .el-icon-s-grid {
    //     color: #9e9797;
    //     margin-left: 5%;
    //     font-size: 1.4rem;
    //   }
    // }

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
      height: 32%;
      margin-top: 2%;
    }
  }
}
</style>
