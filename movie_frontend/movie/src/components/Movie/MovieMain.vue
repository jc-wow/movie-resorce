<template>
  <div class="movie-main">
    <!-- <transition name="startpage"> -->
    <StartPage class="movie-main-startpage" v-show="showStartpage" @scroll.native="scrollCallback"></StartPage>
    <!-- </transition> -->
    <transition name="menu">
      <Menu v-show="menu"></Menu>
    </transition>
    <div class="movie-main-header"></div>
    <div class="movie-main-body" @click="showStartpage = !showStartpage">
      <div class="movie-container" v-for="(item, index) in category" :key="item.key">
        <InfoContainer :category="item"></InfoContainer>
      </div>
    </div>
  </div>
</template>

<script>
import Menu from "../common/Menu";
import InfoContainer from "./InfoContainer";
import StartPage from "../StartPage";
import { debug } from "console";

export default {
  name: "Movie",
  components: {
    InfoContainer,
    Menu,
    StartPage,
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
  created() {
    this.listenCompScroll();
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

  .menu-enter-active {
    animation: 0.5s menu-slidein;
  }
  .menu-leave-active {
    animation: 0.5s menu-slidein reverse;
  }

  .movie-main-body {
    height: 91%;

    .movieInfo-menuLogo {
      position: absolute;
      height: 4%;
      margin: 2% 0 0 2%;
      z-index: 999;
    }

    .movie-container {
      margin-left: 6%;
      height: 43%;
      margin-top: 2%;
    }
  }
}
</style>
