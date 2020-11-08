<template>
  <div class="allvideos-category">
    <div class="allvideos-category-time">
      <span
        class="category"
        v-for="(item, index) in times"
        :key="'time_' + index"
        @click="selectCat($event)"
      >
        {{ item }}
      </span>
    </div>
    <div class="allvideo-category-year">
      <span
        class="year"
        v-for="(item, index) in years"
        :key="'year_' + index"
        @click="selectYear($event)"
      >
        {{ time.slice(0, 3) + item }}</span
      >
    </div>
  </div>
</template>

<script>
export default {
  name: "AllVideosCategory",
  props: {},
  data() {
    return {
      time: "",
      year: "",
    };
  },
  methods: {
    selectCat(e) {
      this.time = e.currentTarget.textContent.trim();
      let param = "";
      // TODO: not handle 18th yet
      if (this.time.startsWith("18")) {
        param = "18";
      } else {
        param = this.time.slice(0, 3);
      }
      this.$store
        .dispatch("getMovieInfoByTime", { time: param, offset: 1, limit: 500 })
        .then((res) => {
          this.$store.commit("getMovieInfoByTime", res.data);
          this.$emit("getMovieInfo");
        });
    },
    selectYear(e) {
      this.year = e.currentTarget.textContent.trim();
      if (this.year.startsWith("18")) {
        this.year = "18";
      }
      this.$store
        .dispatch("getMovieInfoByTime", {
          time: this.year,
          limit: 20,
          offset: 1,
        })
        .then((res) => {
          this.$store.commit("getMovieInfoByYear", res.data);
          this.$store.commit("getCurSelectYear", this.year);
          this.$emit("getMovieInfo");
          this.$emit("selectPage");
        });
    },
  },
  created() {
    this.times = [
      "2020s",
      "2010s",
      "2000s",
      "1990s",
      "1980s",
      "1970s",
      "1960s",
      "1950s",
      "1940s",
      "1930s",
      "1920s",
      "1910s",
      "1900s",
      "18th",
    ];
    this.years = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"];
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