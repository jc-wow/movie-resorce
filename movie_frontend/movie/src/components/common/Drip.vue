<template>
  <div class="drip">
    <div class="movie" v-for="(item, index) in dripData" :key="'image_' + index">
      <div class="image">
        <el-image
          class="img"
          :src="item.url"
          referrerpolicy="no-referrer"
          fit="contain"
          :lazy="lazyLoad"
        ></el-image>
      </div>
      <div class="movie-desc">
        <ul v-for="(childValue, childKey) in item.info" :key="childKey">
          <span>{{ childValue }}</span>
        </ul>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "Drip",
  props: {
    data: Array
  },
  data() {
    return {
      dripData: this.data,
      lazyLoad: true
    };
  },
  methods: {},
  watch: {
    data: {
      handler: function(value) {
        this.dripData = [];
        this.data = value;
        this.dripData.push(...this.data);
      },
      deep: true
    }
  }
};
</script>

<style lang="scss" scoped>
.drip {
  display: flex;
  flex-direction: column;

  .movie {
    width: 100%;
    display: flex;
    flex-direction: row;

    .image {
      width: 40%;

      .img {
        width: 100%;
        height: 100%;
      }
    }

    .movie-desc {
      color: #fff;
    }
  }
}
</style>