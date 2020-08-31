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
    };
  },
  components: {
    StartPage,
    MovieMain,
    Navigation,
  },
  methods: {
    scroll() {
      window.addEventListener("scroll", () => this.scrollHandler());
    },
    scrollHandler() {
      this.top = document.documentElement.scrollTop;
      if (this.top > this.prePos) {
        this.direction = "down";
      } else {
        this.direction = "up";
      }
      this.prePos = this.top;
      if (this.direction === "down") {
        this.scrollDownHandler();
      }
    },
    scrollDownHandler() {
      if (this.top > 0 && this.top < this.heightOfst) {
				window.scrollTo(1, this.heightOfst);
      }
    },
    getHeightOfComp() {
      this.heightOfst = document.getElementsByClassName("st")[0].clientHeight;
      this.heightOfmv = document.getElementsByClassName(
        "mv-main"
      )[0].clientHeight;
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
    window.removeEventListener("scroll", () => this.scrollHandler());
  },
};
</script>

<style lang="scss" scoped>
.main {
  height: 100%;
}
</style>