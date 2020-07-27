<template>
  <div id="app">
    <router-view></router-view>
    <img class="menu-logo" src="./assets/menu.svg" @click="showMenu" />
  </div>
</template>
<script>
export default {
  name: "App",
  data() {
    return {};
  },
  methods: {
    showMenu() {
      this.$store.commit("showMenu");
    }
  }
};
</script>

<style lang="scss">
html {
  height: 100%;

  body {
    height: 100%;
    margin: 0;

    #app {
      height: 100%;
      position: relative;

      .menu-logo {
        position: fixed;
        height: 4%;
        margin: 2% 0 0 2%;
        z-index: 999;
        top: 0;
      }
    }
  }
}
</style>
