<template>
  <div class="allvideos-category">
    <el-image
      class="allvideos-category-cover"
      :src="cover"
      referrerpolicy="no-referrer"
      fit="fill"
    ></el-image>
    <el-cascader
      class="allvideos-category-years"
      v-model="value"
      :options="options"
      :show-all-levels="false"
      :props="{ expandTrigger: 'hover' }"
      @change="handleChange"
    ></el-cascader>
  </div>
</template>

<script>
export default {
  name: "AllVideosCategory",
  props: {},
  data() {
    return {
      cover: "",
      value: "",
    };
  },
  methods: {
    handleChange(e) {
      if (!e || e.length === 0) return;
      if (e.length === 1) {
        this.years = e[0];
        this.year = e[0];
      } else {
        this.years = e[1] || "";
        this.year = e[2] || "";
      }
      this.getMoviesByYears();
      this.getMoviesByYear();
    },
    getMoviesByYears() {
      this.$store
        .dispatch("getMovieInfoByTime", {
          time: this.years,
          offset: 1,
          limit: 50,
        })
        .then((res) => {
          this.$store.commit("getMovieInfoByTime", res.data);
          this.$emit("getMovieInfo");
        });
    },
    getMoviesByYear() {
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
          // this.$emit("getMovieInfo");
          this.$emit("selectPage", true);
        });
    },
    getOptions() {
      const date = new Date();
      const curYear = date.getFullYear();
      this.options.forEach((century) => {
        if (century.children)
          century.children.forEach((year) => {
            const curYears = year.value;
            let years = 0;
            if (curYears === "2020s") {
              years = curYear - 2020 + 1;
            } else {
              years = 10;
            }
            year.children = new Array(years).fill(0).map((ele, index) => {
              return {
                value: curYears.slice(0, 3) + index,
                label: curYears.slice(0, 3) + index,
              };
            });
          });
      });
    },
    // random change cover
    getCover() {
      this.$store.dispatch("getRandomMovie").then((res) => {
        if (res.success) {
          this.cover = res.data[0].cover;
        }
      });
    },
    changeCover() {
			if (this.randomCoverTimer) clearInterval(this.getCover);
      this.randomCoverTimer = setInterval(this.getCover, 15000);
    },
  },
  beforeMount() {
    this.options = [
      {
        value: "21th",
        label: "21th",
        children: [
          {
            value: "2020s",
            label: "2020s",
          },
          {
            value: "2010s",
            label: "2010s",
          },
          {
            value: "2000s",
            label: "2000s",
          },
        ],
      },
      {
        value: "20th",
        label: "20th",
        children: [
          {
            value: "1990s",
            label: "1990s",
          },
          {
            value: "1980s",
            label: "1980s",
          },
          {
            value: "1970s",
            label: "1970s",
          },
          {
            value: "1960s",
            label: "1960s",
          },
          {
            value: "1950s",
            label: "1950s",
          },
          {
            value: "1940s",
            label: "1940s",
          },
          {
            value: "1930s",
            label: "1930s",
          },
          {
            value: "1920s",
            label: "1910s",
          },
          {
            value: "1910s",
            label: "1910s",
          },
          {
            value: "1900s",
            label: "1900s",
          },
        ],
      },
      {
        value: "19th",
        label: "19th",
      },
    ];
		this.getOptions();
		this.getCover();
    this.changeCover();
  },
  destroyed() {
    if (this.randomCoverTimer) clearInterval(this.randomCoverTimer);
  },
};
</script>

<style lang='scss'>
.allvideos-category {
  height: 100%;
  position: relative;
  display: flex;
  justify-content: center;
  .allvideos-category-cover {
    height: 100%;
    width: 80%;
    opacity: 0.5;
  }
  .allvideos-category-years {
    position: absolute;
  }
}
</style>
