<template>
  <div class="title">
    <span>一九九四</span>
    <span @click="changePage($event)">首页</span>
    <span @click="changePage($event)">电影</span>
  </div>
</template>

<script>
export default {
  name: "Navigation",
  methods: {
    changePage(val) {
      this.$store.commit("getCurPage", val.target.textContent);
    },
  },
};
</script>

<style lang="scss" scoped>
@keyframes grain {
  0%, 100% {
    transform: translate(0, 0, 0);
  }

  10% {
    transform: translate(-1%, -1%);
  }

  20% {
    transform: translate(1%, 1%);
  }

  30% {
    transform: translate(-2%, -1%);
  }

  40% {
    transform: translate(3%, 1%);
  }

  50% {
    transform: translate(-3%, -1%);
  }

  60% {
    transform: translate(4%, 1%);
  }

  70% {
    transform: translate(-4%, -1%);
  }

  80% {
    transform: translate(2%, 1%);
  }

  90% {
    transform: translate(-3%, -1%);
  }
}

.title {
  width: 100%;
  height: 8vh;
  display: flex;
  color: #fff;
  font-size: 1.5rem;
  position: fixed;
  z-index: 999;

  span {
    cursor: pointer;
    margin-left: 20%;
  }
}

.title::after {
  content: "";
  width: 110%;
  height: 110%;
  position: absolute;
  top: -5%;
  left: -5%;
  opacity: 0.25;
  background-image: url("../../assets/grain.jpg");
  -webkit-animation: grain 0.8s steps(1) infinite;
  animation: grain 0.8s steps(1) infinite;
	z-index: -1;
}
</style>
