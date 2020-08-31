<template>
  <div id="app">
    <router-view></router-view>
  </div>
</template>
<script>
export default {
  name: "App",
  data() {
    return {};
  },
  methods: {},
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
    }
  }
}
</style>
