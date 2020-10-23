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
        @keyup.enter.native="changeSearchVal"
      >
        <el-button
          slot="append"
          icon="el-icon-search"
          @click="changeSearchVal"
        ></el-button>
      </el-input>
    </div>
    <div class="nav-searchpanel">
      <span
        v-for="(item, index) in searchResVal"
        :key="'search' + index"
        @mousemove="hoverMovie(item)"
        @mouseleave="leavehoverMovie(item)"
        :style="{ backgroundColor: item.ishover ? '#ececec' : null }"
      >
        {{ item.title }}
      </span>
    </div>
    <Drawer :showDrawer="showDrawer"></Drawer>
  </div>
</template>

<script>
import Drawer from "@/components/common/Drawer";

export default {
  name: "Navigation",
  components: { Drawer },
  data() {
    return {
      showDrawer: false,
      searchVal: "",
      timer: null,
      searchResVal: [],
    };
  },
  methods: {
    changePage(val) {
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
        this.searchResVal = [];
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
    putSearchPanel() {
      const searchInputObj = document.getElementsByClassName("nav-search")[0];
      const searchInputObjPosition = searchInputObj.getBoundingClientRect();
      const sWidth = searchInputObjPosition.right - searchInputObjPosition.left;
      const sX = searchInputObjPosition.left;
      const sY = searchInputObjPosition.bottom;
      this.searchPanelObj = document.getElementsByClassName(
        "nav-searchpanel"
      )[0];
      this.searchPanelObj.style.cssText = `width: ${sWidth}px; left: ${sX}px; top: ${
        1 + sY
      }px`;
    },
  },
  mounted() {
    this.putSearchPanel();
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
    }
    .nav-classify-1 {
      margin-left: 15%;
    }
  }

  .nav-search {
    width: 13%;
    display: flex;
    .el-input-group {
      .el-input__inner {
        height: 33px;
        font-weight: 600;
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
    font-size: 0.7rem;
    font-weight: 100;
    span {
      display: block;
      line-height: 1.6rem;
      margin-left: 2%;
      cursor: pointer;
    }
  }
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
