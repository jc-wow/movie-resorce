<template>
  <div class="main">
    <Navigation class="nav"></Navigation>
    <div v-show="!isShowDetail">
      <SideBar class="sbar"></SideBar>
      <StartPage class="st"></StartPage>
      <MovieMain class="mv-main"></MovieMain>
      <Music class="mu-main"></Music>
      <Discuss class="dics"></Discuss>
    </div>
    <router-view v-show="isShowDetail"></router-view>
  </div>
</template>

<script>
import StartPage from "./StartPage";
import MovieMain from "../Movie/MovieMain";
import Navigation from "../Nav/Navigation";
import Discuss from "../Discuss/Discuss";
import Music from "../Music/MusicMain";
import SideBar from "../Nav/SideBar";

export default {
  name: "Main",
  data() {
    return {
      direction: "down",
      prePos: 0,
      scrolling: false,
      isShowDetail: false,
    };
  },
  components: {
    StartPage,
    MovieMain,
    Navigation,
    Music,
    Discuss,
    SideBar,
  },
  methods: {
    scrollEvent() {
      window.scrollTo({
        top: this.height,
        left: 0,
        behavior: "smooth",
      });
    },
    getHeightOfComp() {
      this.heightOfst = document.getElementsByClassName("st")[0].clientHeight;
      this.heightOfmv = document.getElementsByClassName(
        "mv-main"
      )[0].clientHeight;
      this.heightOfDics = document.getElementsByClassName(
        "dics"
      )[0].clientHeight;
    },
    jumpToPage(val) {
      this.height = 0;
      switch (val) {
        case "首页":
          this.height = 0;
          break;
        case "电影":
          this.height = this.heightOfst;
          break;
      }
      this.scrollEvent();
    },
    checkCurScrollPosition() {
      if (this.checkScroll) window.clearInterval(this.checkScroll);
      this.checkScroll = setInterval(() => {
        this.$store.commit("getCurPage", null);
      }, 500);
    },
    // trigger fn at the end of scroll event
    debounce(fn, wait) {
      let timeout = null;
      return function () {
        if (!timeout) window.clearTimeout(timeout);
        timeout = window.setTimeout(fn, wait);
      };
    },
    routeToDetail() {
      this.$router.push({ path: `/movie/${this.$store.state.selectedMovie}` }).catch((err) => err);
    },
    showDetail() {
			this.isShowDetail = true;
			
    },
    returnMainPage() {
      this.isShowDetail = false;
      this.$router.push({ path: "/" }).catch((err) => err);
    },
  },
  watch: {
    "$store.state.curPage": function (newVal, oldVal) {
      if (!newVal) return;
      this.returnMainPage();
      this.jumpToPage(newVal);
    },
    "$store.state.selectedMovie": function (val) {
      this.routeToDetail();
      this.showDetail();
    },
  },
  mounted() {
    this.getHeightOfComp();
    this.checkCurScrollPosition();
  },
  destroyed() {
    window.clearInterval(this.checkScroll);
  },
};
</script>

<style lang="scss" scoped>
</style>