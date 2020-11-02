<template>
  <div class="allvideos-category">
    <div class="allvideos-category-time">
      <span
        class="category"
        v-for="(item, index) in category"
        :key="'category_' + index"
        @click="selectCat($event)"
      >
        {{ item }}
      </span>
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
  .allvideos-category-time {
		height: 30%;
		width: 100%;
    .category {
      width: calc(100% / 7);
			cursor: pointer;
			display: inline-block;
			line-height: 3rem;
			text-align: center;
    }
  }
}
</style>