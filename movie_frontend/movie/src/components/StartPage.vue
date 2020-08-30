<template>
  <div class="start-page">
    <transition name="menu">
      <Menu v-show="menu"></Menu>
    </transition>
    <div class="video-container">
      <video class="start-page-video" autoplay loop muted @click="closeMenuPanel">
        <source src="../assets/ep1.mp4" type="video/mp4" />
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
      if (this.$store.state.menuIsShowing) {
        this.$store.commit("showMenu");
      }
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