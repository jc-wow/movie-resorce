<template>
  <div class="main">
    <Navigation class="nav"></Navigation>
    <StartPage class="st"></StartPage>
    <MovieMain class="mv-main"></MovieMain>
  </div>
</template>

<script>
import StartPage from "./StartPage";
import MovieMain from "../Movie/MovieMain";
import Navigation from "../Head/Navigation";

export default {
  name: "Main",
  data() {
    return {
      direction: "down",
      prePos: 0,
      scrolling: false,
      mvTo: null,
    };
  },
  components: {
    StartPage,
    MovieMain,
    Navigation,
  },
  methods: {
    scroll() {
      window.addEventListener("scroll", this.debounce(this.scrollHandler, 100));
    },
    scrollHandler() {
      this.top = document.documentElement.scrollTop;
      if (this.top === this.mvTo || this.top === 1) {
        this.scrolling = false;
        return;
      }
      if (this.top > this.prePos) {
        this.direction = "down";
      } else {
        this.direction = "up";
      }
      this.prePos = this.top;
      this.scrollEvent();
    },
    scrollEvent() {
      if (this.direction === "down") {
        if (this.top < 200 && !this.scrolling) {
          this.scrolling = true;
          this.mvTo = this.heightOfst;
          window.scrollTo({
            top: this.heightOfst,
            left: 0,
            behavior: "smooth",
          });
        }
      } else {
        if (this.top < this.heightOfst + 200 && !this.scrolling) {
          this.scrolling = true;
          this.mvTo = 0;
          window.scrollTo({
            top: 1,
            left: 0,
            behavior: "smooth",
          });
        }
      }
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
  },
  watch: {
    "$store.state.curPage": function (val) {
      console.log(val);
    },
  },
  mounted() {
    this.scroll();
    this.getHeightOfComp();
  },
  destroyed() {
    window.removeEventListener(
      "scroll",
      this.debounce(this.scrollHandler, 100)
    );
  },
};
</script>

<style lang="scss" scoped>
.main {
  height: 100%;
}
</style>