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
			console.log(this.top)
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
        if (this.top > 0 && this.top < 100 && !this.scrolling) {
          window.scrollBy({
            top: this.heightOfst,
            left: 0,
            behavior: "smooth",
          });
        }
      } else {
				
			}

      // check scrolling
      if (this.scroll) window.clearTimeout(this.scroll);
      this.checkScrolling();
      this.scrolling = true;
    },
    checkScrolling() {
      this.scroll = window.setTimeout(() => {
        this.scrolling = false;
      }, 100);
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