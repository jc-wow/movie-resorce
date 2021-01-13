<template>
  <div class="allvideos-category">
    <div class="allvideos-category-time">
      <DropDown></DropDown>
    </div>
    <!-- <div class="allvideo-category-year">
    </div> -->
  </div>
</template>

<script>
import DropDown from '../common/DropDown'

export default {
  name: "AllVideosCategory",
  components: {
    DropDown
  },
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
};
</script>

<style scoped lang='scss'>
.allvideos-category {
  height: 100%;
  position: relative;
  .allvideos-category-time {
    height: 50%;
    width: 97%;
    display: flex;
    padding: 3% 3%;
    position: relative;
    .year {
      height: calc(90% / 7);
      display: flex;
      align-items: center;
      justify-content: center;
      margin: 1%;
      border: #fff solid;
      border-radius: 10px;
    }
    .year:hover {
      cursor: pointer;
      background-color: #fff;
    }
  }
}
</style>
