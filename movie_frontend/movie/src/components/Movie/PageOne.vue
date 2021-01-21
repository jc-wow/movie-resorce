<template>
  <div class="page-one">
      <div class="page-one-back" v-if="load">
        <section class="page-one-desc">
          <p class="page-one-desc1">让影视在时间中穿梭</p>
          <p class="page-one-desc2">
            <span>一个影视爱好者按时间收集影视的网站</span>
          </p>
          <p class="page-one-desc3">
            “Roads? Where we're going <br />
            we don't need roads.”
          </p>
        </section>
        <el-cascader
          class="page-one-years"
          v-model="value"
          :options="options"
          :show-all-levels="false"
          :props="{ expandTrigger: 'hover' }"
          @change="handleChange"
          placeholder="请选择年份"
        ></el-cascader>
      </div>
  </div>
</template>

<script>
export default {
  name: "PageOne",
  data() {
    return {
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
    this.load = true;
    this.getOptions();
  },
};
</script>

<style lang="scss">
.page-one {
  width: 100%;
  background-image: linear-gradient(45deg, #cac531, #f3f9a7);
  position: relative;
  .page-one-desc {
    text-align: center;
    perspective: 60;
    -webkit-perspective: 60;
    margin-top: 15%;

    .page-one-desc1 {
      font-size: 2rem;
      font-weight: 800;
      margin-bottom: 0;
    }
    .page-one-desc2 {
      font-size: 1.1rem;
      font-weight: 500;

      span {
        padding-left: 32%;
      }
    }
    .page-one-desc3 {
      margin-top: 35%;
      font-size: 2.2rem;
      transform: rotateX(45deg);
      opacity: 0.5;
    }
  }

  .page-one-years {
    position: absolute;
    top: 46%;
    left: 30%;
    .el-input--suffix {
      font-size: 1.2rem;
      font-weight: 700;
      width: 80%;
      .el-input__inner::-webkit-input-placeholder {
        color: rgb(10, 10, 10) !important;
        font-size: 1rem;
      }
      .el-input__inner {
        border-radius: 1.5rem;
        border: none;
        text-align: center;
        background-color: #f3f9a7;
        color: #000;
      }
      .el-input__inner:focus {
        border-color: #fff;
      }
    }
  }
}

.el-cascader__dropdown {
  border-radius: 1rem;
  background-color: rgba(0, 0, 0, 0.8);

  .el-cascader-panel {
    font-size: 1rem;
    width: 70%;
  }

  .el-cascader-menu {
    min-width: 10vw;

    .el-cascader-menu__wrap {
      .el-cascader-menu__list {
        color: #fff;
        font-weight: 700;
        .el-cascader-node:hover {
          color: #409eff !important;
        }
        .el-icon-arrow-right {
          font-size: 0.9rem;
        }
      }
    }
  }
}
</style>
