<template>
  <div class="allvideos-category">
    <div class="allvideos-category-content">
      <div
        class="allvideos-category-content-title"
        :class="{ covertextfadein: coverTextFadein }"
      >
        <span id="cover-title">{{ coverData.title }}</span>
        <span id="cover-rd">{{ coverData.release_date }}</span>
      </div>
    </div>
    <el-image
      class="allvideos-category-cover"
      :class="{ fadein: isFadein }"
      :src="coverData.cover"
      referrerpolicy="no-referrer"
      fit="contain"
    ></el-image>
    <!-- <el-cascader
      class="allvideos-category-years"
      v-model="value"
      :options="options"
      :show-all-levels="false"
      :props="{ expandTrigger: 'hover' }"
      @change="handleChange"
    ></el-cascader> -->
  </div>
</template>

<script>
export default {
  name: "AllVideosCategory",
  props: {},
  data() {
    return {
      coverData: {},
      value: "",
      isFadein: true,
      coverTitle: "",
      coverTextFadein: true,
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
    getCover() {
      this.$store.dispatch("getRandomMovie").then((res) => {
        if (res.success) {
          this.isFadein = true;
          this.coverTextFadein = true;
          this.coverData = res.data[0];
        }
      });
    },
    // random change cover
    changeCover() {
      if (this.randomCoverTimer) clearInterval(this.getCover);
      this.randomCoverTimer = setInterval(() => {
        this.isFadein = false;
        this.coverTextFadein = false;
        this.getCover();
      }, 30000 + 5 * Math.random());
    },
    getCoverTitle() {
      if (Object.keys(this.coverData).length === 0) return;
      if (this.coverData.release_date.length === 0) {
        return this.coverData.title;
      } else {
        return (
          this.coverData.title +
          "\xa0\xa0\xa0\xa0\xa0\xa0\xa0" +
          this.coverData.release_date
        );
      }
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
    if (this.getCoverTimer) clearInterval(this.getCoverTimer);
  },
};
</script>

<style lang='scss'>
@keyframes fadein {
  0% {
    opacity: 0;
  }
  100% {
    opacity: 0.5;
  }
}

@keyframes textfadein {
  0% {
    opacity: 0;
  }
  100% {
    opacity: 1;
  }
}

.allvideos-category {
  height: 100%;
  position: relative;
  display: flex;
  align-items: center;
  flex-direction: column;

  .allvideos-category-content {
    width: 80%;
    height: 10%;
    display: flex;
    position: absolute;

    .allvideos-category-content-title {
      margin-left: 20%;
      width: 100%;
      span {
        display: block;
        color: #fff;
        text-align: center;
        font-size: 1rem;
        text-overflow: ellipsis;
        white-space: nowrap;
        overflow: hidden;
        width: 100%;
      }

      #cover-rd {
        margin-top: 1%;
      }
    }
  }

  .covertextfadein {
    animation: textfadein 6s ease;
  }
  .allvideos-category-cover {
    height: 80%;
    width: 80%;
    opacity: 0.5;
    position: absolute;
    top: 10%;
    margin-left: 20%;
  }
  .fadein {
    animation: fadein 6s ease;
  }
  .allvideos-category-years {
    position: absolute;

    .el-input__inner {
      background-color: #000;
      border-color: #000;
    }
    .el-input__inner:focus {
      border-color: #fff;
    }
  }
}
</style>
