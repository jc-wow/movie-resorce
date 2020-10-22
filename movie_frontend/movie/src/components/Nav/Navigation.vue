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
    <el-input
      placeholder="请输入内容"
      v-model="searchVal"
			@input="changeSearchVal"
    >
      <el-button slot="append" icon="el-icon-search"></el-button>
    </el-input>
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
			searchVal: '',
			timer: null
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
		changeSearchVal(val) {
			clearTimeout(this.timer);
			this.timer = setTimeout(() => this.reqSearchAPI(), 2000)
		},
		reqSearchAPI() {
			console.log(55555)
		}
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
    width: 50%;
    display: flex;
    align-items: center;

    span {
      cursor: pointer;
      margin-left: 8%;
      color: #e3dbdf;
      line-height: 2.5rem;
      // width: 9%;
      text-align: center;
      border-radius: 10px;
      border: 0px solid #000;
      // background-color: #2b2929;
    }
    .nav-classify-1 {
      margin-left: 15%;
    }
  }
	.el-input-group {
		width: 11%;

		.el-input__inner {
			height: 35px;
		}

		.el-button {
			padding: 10px 12px;
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
