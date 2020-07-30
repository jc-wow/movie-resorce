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
        <i class="el-icon-arrow-right" @click="downPage"></i>
      </div>
    </div>
    <div class="image-container">
      <div
        class="image-info"
        :id="'image-info_' + index"
        v-for="(item, index) in info"
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
export default {
  name: "MovieInfo",
  props: {
    info: Array,
    curPage: Number,
    category: String,
  },
  data() {
    return {
      imageInfoContainerWidth: 0,
      transDistance: 0,
    };
  },
  methods: {
    upPage() {
      if (this.transDistance === 0) return;
      this.transDistance += 0.5 * this.pageWidth;
      this.$emit("paging", "up", this.transDistance);
    },
    downPage() {
      this.transDistance -= 0.5 * this.pageWidth;
      this.$emit("paging", "down", this.transDistance);
    },
  },
  mounted() {
    this.pageWidth = document.body.clientWidth;
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