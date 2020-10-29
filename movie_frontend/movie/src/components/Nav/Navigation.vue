<template>
  <div class="nav">
    <div class="nav-logo">
      <img src="../../assets/text.png" style="object-fit: cover" />
    </div>
    <div class="nav-classify">
      <span
        class="nav-classify-1"
        @click="changePage($event)"
        @mouseover="enterNav($event)"
        @mouseleave="leaveNav($event)"
        >首页</span
      >
      <span
        class="nav-classify-2"
        @click="changePage($event)"
        @mouseover="enterNav($event)"
        @mouseleave="leaveNav($event)"
        >电影</span
      >
      <span
        class="nav-classify-3"
        @click="changePage($event)"
        @mouseover="enterNav($event)"
        @mouseleave="leaveNav($event)"
        >想法</span
      >
    </div>
    <div class="nav-search">
      <el-input
        placeholder="搜索你感兴趣的电影"
        v-model="searchVal"
        @input="changeSearchVal"
        @keyup.enter.native="selectMovie()"
        @keydown.down.native="keyControlMovie($event)"
        @keydown.up.native="keyControlMovie($event)"
      >
        <el-button
          slot="append"
          icon="el-icon-search"
          @click="selectMovie()"
        ></el-button>
      </el-input>
    </div>
    <div class="nav-searchpanel">
      <div
        :id="'nav-searchpanel-' + index"
        v-for="(item, index) in searchResVal"
        :key="'search' + index"
        @mousemove="hoverMovie(item)"
        @mouseleave="leavehoverMovie(item)"
        :style="{ backgroundColor: item.ishover ? '#ececec' : null }"
        @click="selectMovie($event)"
      >
        {{ item.title }}
      </div>
    </div>
    <!-- <Drawer :showDrawer="showDrawer"></Drawer> -->
  </div>
</template>

<script>
// import Drawer from "@/components/common/Drawer";

export default {
  name: "Navigation",
  // components: { Drawer },
  data() {
    return {
      showDrawer: false,
      searchVal: "",
      timer: null,
      searchResVal: [],
      keyPosition: -1,
    };
  },
  methods: {
    selectMovie(e) {
      if (e) {
        this.curSelectMovie = e.target.textContent.trim() || "";
      } else {
        if (this.keyPosition !== -1) {
					this.curSelectMovie = this.searchResVal[this.keyPosition].title;
        } else {
          this.curSelectMovie = this.searchVal;
        }
      }
      if (this.curSelectMovie.length === 0) return;
      this.movieObj = this.searchResVal.filter(
        (ele) => ele.title === this.curSelectMovie
      )[0];
      if (!this.movieObj) return;
      this.$store.commit("getSelectedMovie", this.movieObj);
    },
    changePage(val) {
      // this.initData()
      this.$store.commit("getCurPage", val.target.textContent);
    },
    enterNav(e) {
      e.target.style = "background-color: #2b2929";
    },
    leaveNav(e) {
      e.target.style = "background-color: none";
    },
    changeSearchVal() {
      clearTimeout(this.timer);
      this.timer = setTimeout(() => this.reqSearchAPI(), 500);
    },
    keyControlMovie(event) {
      const searchResValLength = this.searchResVal.length;
      if (searchResValLength === 0 || !event.code) return;
      const curClassName = event.currentTarget.className;
      if (!curClassName.includes("el-input")) return;

      if (
        event.code === "ArrowDown" &&
        this.keyPosition + 1 < searchResValLength
      ) {
        if (this.keyPosition !== -1) {
          this.searchResVal[this.keyPosition].ishover = false;
        }
        this.keyPosition++;
      } else if (event.code === "ArrowUp" && this.keyPosition >= 0) {
        this.searchResVal[this.keyPosition].ishover = false;
        this.keyPosition--;
        if (this.keyPosition === -1) return;
      }
      this.checkKeyPosition();
      this.searchResVal[this.keyPosition].ishover = true;
    },
    checkKeyPosition() {
      if (this.keyPosition === -1) return;
      const searchPanel = document.getElementsByClassName("nav-searchpanel")[0];
      const searchPanelObj = searchPanel.getBoundingClientRect();
      const searchPanelBottom = searchPanelObj.bottom;
      const curKeyObj = document
        .getElementById(`nav-searchpanel-${this.keyPosition}`)
        .getBoundingClientRect();
      const curKeyBottom = curKeyObj.bottom;
      const curItemHeight = curKeyObj.height;
      if (curKeyBottom > searchPanelBottom) {
        searchPanel.scrollBy(0, curItemHeight);
      } else if (curKeyObj.top < searchPanelObj.top) {
        searchPanel.scrollBy(0, -curItemHeight);
      }
    },
    hoverMovie(item) {
      item.ishover = true;
    },
    leavehoverMovie(item) {
      item.ishover = false;
    },
    reqSearchAPI() {
      const reg = new RegExp(
        "[`~!@#$^&*()=|{}':;',\\[\\].<>/?~！@#￥……&*（）——|{}【】‘；：”“'。，、？]"
      );
      if (
        !this.searchVal ||
        this.searchVal.trim().length === 0 ||
        this.searchVal.trim().match(reg)
      ) {
        this.initData();
        return;
      }
      this.$store
        .dispatch("searchMovie", { key: this.searchVal })
        .then((res) => {
          res.data.rows.forEach((ele) => {
            ele.ishover = false;
          });
          this.searchResVal = res.data.rows;
        });
    },
    getSearchPanelPosition() {
      const searchInputObj = document.getElementsByClassName("nav-search")[0];
      const searchInputObjPosition = searchInputObj.getBoundingClientRect();
      const sWidth = searchInputObjPosition.right - searchInputObjPosition.left;
      const sX = searchInputObjPosition.left;
      const sY = searchInputObjPosition.bottom;
      this.searchPanelObj = document.getElementsByClassName(
        "nav-searchpanel"
      )[0];
      this.putSearchPanel(sWidth, sX, sY);
    },
    putSearchPanel(sWidth, sX, sY) {
      this.searchPanelObj.style.cssText = `width: ${sWidth}px; left: ${sX}px; top: ${
        1 + sY
      }px`;
    },
    initData() {
      this.keyPosition = -1;
      this.searchResVal = [];
      this.searchVal = "";
    },
  },
  watch: {
    $route(to, from) {
      this.initData();
      this.$nextTick(() => this.getSearchPanelPosition());
    },
  },
  mounted() {
    this.getSearchPanelPosition();
    const mainSelector = document.getElementsByClassName("main")[0];
    if (!mainSelector) return;
    mainSelector.addEventListener("click", () => {
      this.searchResVal = [];
      this.keyPosition === -1;
    });
    window.onresize = () => this.getSearchPanelPosition();
  },
  destroyed() {
    this.timer = null;
  },
};
</script>

<style lang="scss">
@keyframes grain {
  0%,
  100% {
    transform: translate(0, 0, 0);
  }

  10% {
    transform: translate(-1%, 0%);
  }

  20% {
    transform: translate(1%, 0%);
  }

  30% {
    transform: translate(-2%, 0%);
  }

  40% {
    transform: translate(3%, 0%);
  }

  50% {
    transform: translate(-3%, 0%);
  }

  60% {
    transform: translate(4%, 0%);
  }

  70% {
    transform: translate(-4%, 0%);
  }

  80% {
    transform: translate(2%, 0%);
  }

  90% {
    transform: translate(-3%, 0%);
  }
}

.nav {
  width: 100%;
  height: 8vh;
  color: #fff;
  font-size: 1.2rem;
  position: fixed;
  z-index: 999;
  display: flex;
  align-items: center;
  background-color: #000;

  .nav-logo {
    height: 100%;
    width: 10%;
    margin-left: 20%;

    img {
      object-fit: cover;
      height: 97%;
      width: 100%;
      margin-top: 2%;
    }
  }

  .nav-classify {
    height: 100%;
    width: 45%;
    display: flex;
    align-items: center;

    span {
      cursor: pointer;
      margin-left: 8%;
      color: #e3dbdf;
      line-height: 2.5rem;
      text-align: center;
      border-radius: 10px;
      border: 0px solid #000;
      width: 8%;
    }
    .nav-classify-1 {
      margin-left: 15%;
    }
  }

  .nav-search {
    width: 14%;
    display: flex;
    .el-input-group {
      .el-input__inner {
        height: 33px;
        font-weight: 400;
        font-size: 0.9rem;
      }

      .el-button {
        padding: 10px 12px;
      }
    }
  }

  .nav-searchpanel {
    position: absolute;
    font-size: 0.9rem;
    background-color: #fff;
    color: #000;
    border-radius: 3px;
    font-size: 0.8rem;
    font-weight: 100;
    max-height: 20rem;
    overflow: auto;
    div {
      // display: block;
      line-height: 1.6rem;
      margin-left: 2%;
      cursor: pointer;
      white-space: nowrap;
      overflow: hidden;
      text-overflow: ellipsis;
    }
    div:hover {
      overflow: visible;
      white-space: normal;
    }
  }
}

.nav-searchpanel::-webkit-scrollbar-track {
  -webkit-box-shadow: inset 0 0 6px rgba(0, 0, 0, 0.3);
  border-radius: 10px;
  background-color: #f5f5f5;
}

.nav-searchpanel::-webkit-scrollbar {
  width: 12px;
  background-color: #f5f5f5;
}

.nav-searchpanel::-webkit-scrollbar-thumb {
  border-radius: 10px;
  -webkit-box-shadow: inset 0 0 6px rgba(0, 0, 0, 0.3);
  background-color: #9e9e9e;
}

.nav::after {
  content: "";
  width: 110%;
  height: 110%;
  position: absolute;
  top: -10%;
  left: -5%;
  opacity: 0.2;
  background-image: url("../../assets/grain.jpg");
  -webkit-animation: grain 0.8s steps(1) infinite;
  animation: grain 0.8s steps(1) infinite;
  z-index: -1;
}
</style>
