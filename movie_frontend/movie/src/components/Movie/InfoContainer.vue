<template>
  <div class="info-container">
    <div class="page-icon">
      <div class="category">{{ category }}</div>
      <div class="pagnation">
        <i
          class="el-icon-arrow-left"
          @click="upPage"
          :style="{ opacity: transDistance === 0 ? 0.2 : 1 }"
        ></i>
        <i class="el-icon-arrow-right" @click="downPage" :style="{ opacity: isEnd ? 0.2 : 1 }"></i>
      </div>
    </div>
    <div class="image-container">
      <div
        class="image-info"
        :id="'image-info_' + index"
        v-for="(item, index) in movieInfo"
        :key="'container_' + index"
      >
        <el-image
          class="image-info-container"
          :src="item.cover"
          referrerpolicy="no-referrer"
          fit="cover"
        ></el-image>
        <a>{{ item.title }}</a>
      </div>
    </div>
  </div>
</template>

<script>
import { mapState } from "vuex";

export default {
  name: "MovieInfo",
  props: {
    // info: Array,
    // curPage: Number,
    category: String,
  },
  data() {
    return {
      movieInfo: [],
      imageInfoContainerWidth: 0,
      transDistance: 0,
      isEnd: false,
      requestParam: {
        page: 1,
        limit: 15,
      },
    };
  },
  methods: {
    upPage() {
      if (this.transDistance === 0) return;
      this.transDistance += 0.5 * this.pageWidth;
      this.paging("up", this.transDistance);
    },
    downPage() {
      if (this.isEnd) return;
      this.transDistance -= 0.5 * this.pageWidth;
      this.paging("down", this.transDistance);
    },
    getMoveInfo() {
      this.$store.dispatch("getMovieInfo", this.requestParam).then((res) => {
        this.stopReqAPI(res);
        this.getHighestScoreMovie;
      });
    },
    paging(direction, transDistance) {
      this.direction = direction;
      this.imgContainerEle = document.getElementsByClassName(
        "image-container"
      )[0];
      this.imgContainerEle.style.cssText = `transform: translatex(${transDistance}px)`;
      this.removeTransEvent();
      this.imgContainerEle.addEventListener(
        "transitionend",
        this.ifReqAPI,
        false
      );
    },
    removeTransEvent() {
      this.imgContainerEle &&
        this.imgContainerEle.removeEventListener(
          "transitionend",
          this.ifReqAPI,
          false
        );
    },
    ifReqAPI() {
      const lastEle = $(".image-container div:last");
      const disToRLeftDoc = lastEle.offset().left;
      if (this.direction === "down" && disToRLeftDoc < $(window).width()) {
        this.requestParam.page++;
        this.getMoveInfo();
      }
    },
    stopReqAPI(res) {
      if (res && res.success && res.data.length === 0) this.isEnd = true;
    },
  },
  computed: {
    ...mapState({
      getHighestScoreMovie(status) {
        this.movieInfo.push(...status.movieInfo);
      },
    }),
  },
  mounted() {
    this.getMoveInfo();
    this.pageWidth = document.body.clientWidth;
  },
  destroyed() {
    this.removeTransEvent();
  },
};
</script>

<style lang="scss" scoped>
.info-container {
  display: flex;
  flex-direction: column;
  height: 100%;
  justify-content: space-between;
  overflow-x: hidden;

  .page-icon {
    height: 15%;
    width: 97%;
    display: flex;
    flex-direction: row;
    justify-content: space-between;

    .category {
      color: #fff;
      margin-left: 1%;
    }

    .pagnation {
      font-size: 1.3rem;
      width: 4%;
      display: flex;
      justify-content: space-between;

      .el-icon-arrow-left {
        color: #fff;
      }

      .el-icon-arrow-right {
        color: #fff;
      }
    }
  }
  .image-container {
    height: 85%;
    display: flex;
    transition: transform 0.8s;

    .image-info {
      display: flex;
      flex-direction: column;
      justify-content: space-around;
      margin: 0 1%;

      .image-info-container {
        height: 150px;
        width: 100px;
        margin: 1%;
        border-radius: 4px;
      }

      a {
        width: 90px;
        font-size: 0.9rem;
        color: #fff;
        text-overflow: ellipsis;
        white-space: nowrap;
        display: block;
        overflow: hidden;
        margin: 0 2%;
      }

      a:hover {
        text-overflow: clip;
        white-space: normal;
        word-break: break-all;
      }
    }
  }
}
</style>