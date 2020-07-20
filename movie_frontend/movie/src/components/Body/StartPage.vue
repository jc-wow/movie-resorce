<template>
  <div class="start-page">
    <div class="video-container">
      <transition name="menu" @before-leave="closeMenu" @before-enter="openMenu">
        <Menu v-show="menu"></Menu>
      </transition>
        <video class="start-page-video" autoplay loop muted @click="closeMenuPanel">
          <source src="../../assets/ep1.mp4" type="video/mp4" />
        </video>
    </div>
  </div>
</template>

<script>
import Menu from "@/components/common/Menu";

export default {
  name: "startPage",
  components: { Menu },
  data() {
    return {};
  },
  methods: {
    closeMenuPanel() {
      this.$store.commit("showMenu");
    },
    closeMenu() {
      document.getElementsByClassName("start-page-video")[0].style.cssText =
        "width: 100%; margin-left: 0; transition: margin-left: 0.5";
    },
    openMenu() {
      document.getElementsByClassName("start-page-video")[0].style.cssText =
        "width: 80%; margin-left: 20%; transition: margin-left: 0.5";
    }
  },
  computed: {
    menu() {
      return this.$store.state.menuIsShowing;
    }
  }
};
</script>

<style scoped lang="scss">
@keyframes menu-slidein {
  from {
    transform: translateX(-100%);
  }
  to {
    transform: translateX(0);
  }
}

.start-page {
  width: 100%;
  height: 100%;
  background-color: #000;
  position: relative;

  .menu-enter-active {
    animation: 0.5s menu-slidein;
  }
  .menu-leave-active {
    animation: 0.5s menu-slidein reverse;
  }
  .video-container {
    .start-page-video {
      position: absolute;
      height: 100%;
			width: 100%;
    }
  }
}
</style>