<template>
  <div class="main">
    <Navigation class="nav"></Navigation>
    <StartPage class="st"></StartPage>
    <MovieMain class="mv-main"></MovieMain>
		<Discuss class="dics"></Discuss>
  </div>
</template>

<script>
import StartPage from "./StartPage";
import MovieMain from "../Movie/MovieMain";
import Navigation from "../Head/Navigation";
import Discuss from "../Discuss/Discuss"

export default {
  name: "Main",
  data() {
    return {
      direction: "down",
      prePos: 0,
      scrolling: false,
      index: 0,
    };
  },
  components: {
    StartPage,
    MovieMain,
		Navigation,
		Discuss
  },
  methods: {
    // scroll() {
    //   window.addEventListener("scroll", this.debounce(this.scrollHandler, 100));
    // },
    // scrollHandler() {
    //   this.top = document.documentElement.scrollTop;
    //   console.log(this.mvTo, this.top);
    //   if (this.mvTo && this.top >= this.mvTo) {
    //     this.scrolling = false;
    //     return;
    //   }
    //   if (this.top > this.prePos) {
    //     this.direction = "down";
    //   } else {
    //     this.direction = "up";
    //   }
    //   this.prePos = this.top;
    //   this.scrollEvent();
    // },
    scrollEvent() {
			console.log(this.height)
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
    },
    debounce(fn, wait) {
      let timeout = null;
      return function () {
        if (!timeout) window.clearTimeout(timeout);
        timeout = window.setTimeout(fn, wait);
      };
    },
    jumpToPage(val) {
      this.height = 0;
      switch (val) {
        case "首页":
          this.index = 1;
          this.height = 0;
          break;
        case "电影":
          this.index = 2;
          this.height = this.heightOfst;
          break;
			}
			this.scrollEvent();
    },
  },
  watch: {
    "$store.state.curPage": function (val) {
      this.jumpToPage(val);
    },
  },
  mounted() {
    // this.scroll();
    this.getHeightOfComp();
  },
  destroyed() {
    // window.removeEventListener(
    //   "scroll",
    //   this.debounce(this.scrollHandler, 100)
    // );
  },
};
</script>

<style lang="scss" scoped>
.main {
  height: 100%;
}
</style>