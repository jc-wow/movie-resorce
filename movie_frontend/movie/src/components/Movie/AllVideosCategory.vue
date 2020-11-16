<template>
  <div class="allvideos-category">
    <div class="allvideos-category-time">
      <div class="allvideos-category-time-left">
        <div
          class="left year"
          v-for="(year, index) in leftColtimes"
          :key="'leftColtimes' + index"
        >
          {{ year }}
        </div>
      </div>
      <div class="allvideos-category-time-right">
        <div
          class="right, year"
          v-for="(year, index) in rightColtimes"
          :key="'rightColtimes' + index"
        >
          {{ year }}
        </div>
      </div>
      <Notes></Notes>
    </div>
    <div class="allvideo-category-year"></div>
  </div>
</template>

<script>
import Notes from "../common/MusicNotes";

export default {
  name: "AllVideosCategory",
  components: { Notes },
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
        .dispatch("getMovieInfoByTime", { time: param, offset: 1, limit: 50 })
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
          this.$store.commit("getIsPreviewVideoState", false);
          this.$emit("getMovieInfo");
          this.$emit("selectPage", true);
        });
    },
  },
  created() {
    this.leftColtimes = [
      "2020s",
      "2000s",
      "1980s",
      "1960s",
      "1940s",
      "1920s",
      "1900s",
    ];
    this.rightColtimes = [
      "2010s",
      "1990s",
      "1970s",
      "1950s",
      "1930s",
      "1910s",
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
    height: 50%;
    width: 97%;
    display: flex;
    padding: 3% 3%;
		position: relative;
    .allvideos-category-time-left {
      width: 50%;
      height: 100%;
    }
    .allvideos-category-time-right {
      width: 50%;
      height: 100%;
    }
    .year {
      height: calc(90% / 7);
      display: flex;
      align-items: center;
      justify-content: center;
      margin: 1%;
			border: #fff solid;
      // background-color: #fff;
    }
    .year:hover {
      cursor: pointer;
    }
  }
}
</style>