<template>
  <div class="allvideos-category">
    <div
      class="category"
      v-for="(item, index) in category"
      :key="'category_' + index"
      @click="selectCat($event)"
    >
      {{ item }}
    </div>
  </div>
</template>

<script>
export default {
  name: "AllVideosCategory",
  props: {
    category: Array,
  },
  data() {
    return {};
  },
  methods: {
    selectCat(e) {
      const cat = e.currentTarget.textContent.trim();
      let param = "";
      if (cat.startsWith("18")) {
        param = "18";
      } else {
        param = cat.slice(0, 3);
      }
      this.$store
        .dispatch("getMovieInfoByTime", { time: param })
        .then((res) => {
          this.$store.commit("getMovieInfoByTime", res.data);
          this.$emit("getMovieInfo");
        });
    },
  },
};
</script>

<style scoped lang='scss'>
.allvideos-category {
  height: 100%;
  .category {
    height: calc(100% / 14);
    display: flex;
    align-items: center;
    cursor: pointer;
  }
}
</style>