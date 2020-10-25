<template>
  <div id="app">
    <Navigation></Navigation>
    <keep-alive include="Main">
      <router-view :key="$store.state.selectedMovie.title"></router-view>
    </keep-alive>
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
    returnToMainPage() {
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
        this.returnToMainPage();
      } else {
        sessionStorage.removeItem("alldiscussOffset");
        this.$router.push({ name: "discuss" }).catch((err) => err);
      }
    },
    // listen select discuss and add new discuss
    "$store.state.selectedDiscuss": function (newVal, oldVal) {
      if (newVal.length === 0) return;
      if (this.$store.state.selectedDiscuss === "add") {
        this.$router.push({ path: "/discuss/new" }).catch((err) => err);
        this.$store.commit("getSelectedDiscuss", "");
      } else {
        sessionStorage.removeItem("discussRepOffset");
        this.$router
          .push({
            path: `/discuss/${this.$store.state.selectedDiscuss.id}`,
          })
          .catch((err) => err);
      }
      this.$store.commit("getCurPage", "");
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
    font-family: "Helvetica Neue", Helvetica, "PingFang SC", "Hiragino Sans GB",
      "Microsoft YaHei", "微软雅黑", Arial, sans-serif;
    #app {
      position: relative;
      height: 100%;
      background-color: #000;
      @media screen and (max-width: 1920px) {
        min-width: 1500px;
      }
      @media screen and (min-width: 2000px) {
        min-width: 2500px;
      }
    }
  }
}
</style>
