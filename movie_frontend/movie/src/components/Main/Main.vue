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
      const top = document.documentElement.scrollTop;
      console.log(top);
    },
    getHeightOfComp() {
      this.heightOfst = document.getElementsByClassName("st")[0].clientHeight;
      this.heightOfmv = document.getElementsByClassName(
        "mv-main"
      )[0].clientHeight;
      console.log(this.heightOfst, this.heightOfmv);
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