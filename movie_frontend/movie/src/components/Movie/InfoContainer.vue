<template>
  <div class="info-container">
    <div class="page-icon">
      <div class="category">{{ category.title }}</div>
      <div class="pagnation">
        <i
          class="el-icon-arrow-left"
          @click="upPage"
          :style="{ opacity: transDistance === 0 ? 0.2 : 1 }"
        ></i>
        <i
          class="el-icon-arrow-right"
          v-show="!reqAPIing"
          @click="downPage"
          :style="{ opacity: isEnd ? 0.2 : 1 }"
        ></i>
        <i class="el-icon-loading" v-show="reqAPIing" />
      </div>
    </div>
    <div :class="['image-container', 'image-container-' + category.key]">
      <div
        class="image-info"
        :id="'image-info_' + index"
        v-for="(item, index) in movieInfo"
        :key="'container_' + index"
        @click="selectMovie(item)"
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
    category: Object,
  },
  data() {
    return {
      movieInfo: [],
      imageInfoContainerWidth: 0,
      transDistance: 0,
      isEnd: false,
      reqAPIing: false,
      requestParam: {
        page: 1,
        limit: 15,
        category: this.category.api,
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
      this.reqAPIing = true;
      this.$store.dispatch("getMovieInfo", this.requestParam).then((res) => {
        this.stopReqAPI(res);
        this.getHighestScoreMovie;
        this.reqAPIing = false;
      });
    },
    paging(direction, transDistance) {
      this.direction = direction;
      this.imgContainerEle.style.cssText = `transform: translatex(${transDistance}px)`;
    },
    listenImgTrans() {
      this.imgContainerEle = document.getElementsByClassName(
        `image-container-${this.category.key}`
      )[0];
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
      const lastEle = $(`.image-container-${this.category.key} div:last`);
      const disToRLeftDoc = lastEle.offset().left;
      if (this.direction === "down" && disToRLeftDoc < $(window).width()) {
        this.requestParam.page++;
        this.getMoveInfo();
      }
    },
    stopReqAPI(res) {
      if (res && res.success && res.data.length === 0) this.isEnd = true;
    },
    selectMovie(val) {
      this.$store.commit("getSelectedMovie", val);
      this.$store.dispatch("getResSelectedMovie", val);
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
    this.listenImgTrans();
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
    height: 11%;
    width: 97%;
    display: flex;
    flex-direction: row;
    justify-content: space-between;

    .category {
      color: #fff;
      margin-left: 1%;
      font-size: 1.2rem;
    }

    .pagnation {
      font-size: 1.3rem;
      width: 4%;
      display: flex;
      justify-content: space-between;

      .el-icon-arrow-left {
        color: #fff;
        cursor: pointer;
      }

      .el-icon-arrow-right {
        color: #fff;
        cursor: pointer;
      }

      .el-icon-loading {
        color: #fff;
        height: fit-content;
      }
    }
  }
  .image-container {
    height: 89%;
    display: flex;
    transition: transform 0.8s;

    .image-info {
      display: flex;
      flex-direction: column;
      justify-content: space-around;
      margin: 0 1%;
      cursor: pointer;

      .image-info-container {
        @media screen and (min-width: 1920px) {
          height: 230px;
          width: 180px;
        }
        height: 200px;
        width: 150px;
        margin: 1%;
        border-radius: 4px;
      }

      a {
        font-size: 0.9rem;
        color: #fff;
        text-align: center;
        display: block;
        margin: 0 2%;
      }
    }
  }
}
</style>