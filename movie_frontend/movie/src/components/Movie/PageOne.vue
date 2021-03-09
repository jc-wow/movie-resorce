<template>
  <div class="page-one" v-if="load">
    <div class="page-one-back">
      <section class="page-one-desc">
        <p class="page-one-desc1">Movie File</p>
        <p class="page-one-desc2">
          <span>Search By Time</span>
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
    <div class="page-one-square">
      <div class="page-one-record"></div>
      <div class="page-one-button" @click="selectYear">{{ buttonValue }}</div>
    </div>
  </div>
</template>

<script>
import { options } from "../../libs/commonvar";

export default {
  name: "PageOne",
  data() {
    return {
      value: "",
      options: options,
      load: false,
      buttonValue: "请选择年份",
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
      this.setTextToSelectButton();
      this.getMoviesByYears();
      this.getMoviesByYear();
    },
    setTextToSelectButton() {
      this.buttonValue = this.year;
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
          this.$store.commit("selectPage", false); // change page state

          // clear search movie key
          this.$store.commit("searchMovieKey", "");
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
    selectYear() {
      document.getElementsByClassName("page-one-years")[0].click();
    },
  },
  created() {
    this.load = true;
  },
  beforeMount() {
    this.getOptions();
  },
};
</script>

<style lang="scss">
@keyframes recordRotate {
  100% {
    transform: rotate(360deg);
  }
}

.page-one {
  display: flex;
  flex-direction: column;
  align-items: center;
  width: 100%;
  position: relative;
  border-top: 1px solid rgba(148, 148, 148, 0.5);
  background: linear-gradient(to right, #000 90%, #c2bfbf);

  .page-one-back {
    width: 100%;
  }

  .page-one-desc {
    text-align: center;
    perspective: 60;
    -webkit-perspective: 60;
    margin-top: 10%;
    color: #fff;

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
  }
  @media screen and (max-height: 800px) {
    .page-one-years {
      position: absolute;
      top: 34%;
      left: 30%;
      z-index: -1;
      visibility: hidden;
      margin-top: 28%;
    }
  }
  @media screen and (min-height: 800px) {
    .page-one-years {
      position: absolute;
      top: 40%;
      left: 30%;
      z-index: -1;
      visibility: hidden;
      margin-top: 28%;
    }
  }
  .page-one-years {
    .el-input--suffix {
      font-size: 1rem;
      font-weight: 700;
      width: 80%;
      .el-input__inner::-webkit-input-placeholder {
        color: rgb(10, 10, 10) !important;
        font-size: 0.9rem;
      }
      .el-input__inner {
        border-radius: 1.5rem;
        border: none;
        text-align: center;
        color: #000;
      }
      .el-input__inner:focus {
        border-color: #fff;
      }
    }
  }
  .page-one-square {
    width: 70%;
    position: relative;
    display: flex;
    justify-content: center;
    align-items: center;
    .page-one-record {
      position: absolute;
      background-image: url("../../assets/record.png");
      width: 100%;
      height: 100%;
      background-size: 100%;
      background-repeat: no-repeat;
      background-position: center;
      animation: recordRotate 30s infinite linear;
    }
    .page-one-record:hover {
      animation-play-state: paused;
    }
    .page-one-button {
      z-index: 999;
      display: inline-block;
      text-decoration: none;
      color: rgb(0, 0, 0);
      width: 31%;
      height: 31%;
      display: flex;
      align-items: center;
      justify-content: center;
      border-radius: 50%;
      text-align: center;
      vertical-align: middle;
      overflow: hidden;
      background-image: linear-gradient(45deg, #709dff 0%, #91fdb7 100%);
      transition: 0.4s;
      font-size: 1.3rem;
    }
    .page-one-button:hover {
      cursor: pointer;
      transform: rotate(10deg);
    }
  }
  .page-one-square:after {
    content: "";
    display: block;
    padding-bottom: 100%;
  }
}

.el-cascader__dropdown {
  border-radius: 1rem;
  background-color: rgba(0, 0, 0, 0.1);

  .el-cascader-panel {
    font-size: 1rem;
    width: 70%;

    .el-cascader-menu {
      min-width: 8vw;

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
  .popper__arrow {
    display: none;
  }
}
</style>
