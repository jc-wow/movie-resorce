<template>
  <div id="app">
    <transition name="changeRouter">
      <router-view></router-view>
    </transition>
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
    },
  },
};
</script>

<style lang="scss">
@keyframes changeRouter-slidein {
  from {
    transform: translateY(-100%);
  }

  to {
    transform: translateY(0);
  }
}

html {
  height: 100%;
  @media screen and (min-width: 1920px) {
    font-size: 20px;
  }

  body {
    height: 100%;
    margin: 0;

    #app {
      height: 100%;
      position: relative;

      .changeRouter-enter-active {
        animation: 2s startpage-slidein;
      }

      .changeRouter-leave-active {
        animation: 2s startpage-slidein reverse;
      }

      .menu-logo {
        position: fixed;
        height: 3.5%;
        margin: 1.5% 0 0 2%;
        z-index: 999;
        top: 0;
      }
    }
  }
}
</style>
