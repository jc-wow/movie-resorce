<template>
  <div class="start-page">
    <div class="video-head"></div>
    <div class="video-container">
      <video class="start-page-video" autoplay loop muted @click="closeMenuPanel">
        <source src="../../assets/ep1.mp4" type="video/mp4" />
      </video>
    </div>
    <div class="start-page-sidebar">
      <img src="../../assets/projector.svg" class="start-page-projector" @load="getProjectPosition" />
    </div>
    <Light :position="projectorPosition"></Light>
  </div>
</template>

<script>
import Menu from "@/components/common/Menu";
import Light from "@/components/common/Light";

export default {
  name: "startPage",
  components: { Menu, Light },
  data() {
    return {
      movies: ["天堂电影院"],
      projectorPosition: {
        x: 0,
        y: 0,
				left: 0,
				top: 0
      },
    };
  },
  methods: {
    closeMenuPanel() {
      if (this.$store.state.menuIsShowing) {
        this.$store.commit("showMenu");
      }
    },
    getProjectPosition() {
      const projectObj = document.getElementsByClassName(
        "start-page-projector"
      )[0];
      const headerObj = document.getElementsByClassName("video-head")[0];
      const headerObjHeight = headerObj.getBoundingClientRect().height;
      const projectObjClient = projectObj.getBoundingClientRect();
			this.projectorPosition.left = projectObjClient.left;
			this.projectorPosition.top = projectObjClient.top;
      this.projectorPosition.x =
        projectObjClient.right - projectObjClient.width / 2;
      this.projectorPosition.y =
        projectObjClient.bottom - headerObjHeight - projectObjClient.height / 5;
    },
  },
  computed: {
    menu() {
      return this.$store.state.menuIsShowing;
    },
  },
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
  height: 100vh;
  position: relative;

  .menu-enter-active {
    animation: 0.5s menu-slidein;
  }
  .menu-leave-active {
    animation: 0.5s menu-slidein reverse;
  }

  .video-head {
    height: 8%;
  }

  .video-container {
    display: flex;
    justify-content: center;
    flex-direction: row;

    .start-page-video {
      position: absolute;
      height: 92%;
      width: 90%;
    }

    .start-page-about {
      position: absolute;
      top: 42%;
      left: 92%;
    }
  }

  .start-page-sidebar {
    position: absolute;
    left: 4%;
    top: 25%;

    .start-page-projector {
      width: 17%;
    }
  }
}
</style>