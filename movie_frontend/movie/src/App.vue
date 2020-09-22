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
    "$store.state.selectedMovie.id": function (newVal, oldVal) {
      if (!newVal) return;
      this.routeToDetail();
    },
    // back to main page when click '电影' and '首页'
    "$store.state.curPage": function (newVal, oldVal) {
      if (!newVal) return;
      if (newVal === "电影" || newVal === "首页") {
        this.returnMainPage();
      } else {
        this.$router.push({ name: "discuss" });
      }
    },
    "$store.state.selectedDiscuss": function (newVal, oldVal) {
      if (this.$store.state.selectedDiscuss === "add") {
        this.$router.push({ path: "/discuss/new_discuss" });
        this.$store.commit("getCurPage", "");
      }
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
