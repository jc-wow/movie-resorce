<template>
  <div id="app">
    <Navigation></Navigation>
    <router-view></router-view>
  </div>
</template>
<script>
import Navigation from "./components/Nav/Navigation";

export default {
  name: "App",
  components: { Navigation },
  data() {
    return {};
  },
  methods: {
    routeToDetail() {
      this.$router
        .push({ path: `/movie/${this.$store.state.selectedMovie.title}` })
        .catch((err) => err);
    },
    returnMainPage() {
			this.$router.push({ path: "/" }).catch((err) => err);
			this.$store.commit("getSelectedMovie", {});
    },
  },
  watch: {
    "$store.state.selectedMovie.title": function (newVal, oldVal) {
			if (!newVal) return;
      this.routeToDetail();
    },
    "$store.state.curPage": function (newVal, oldVal) {
      if (!newVal) return;
      this.returnMainPage();
    },
  },
};
</script>

<style lang="scss">
html {
  height: 100%;
  @media screen and (min-width: 1920px) {
    font-size: 20px;
  }

  body {
    margin: 0;
    height: 100%;

    #app {
      position: relative;
      height: 100%;
      background-color: #000;
    }
  }
}
</style>
