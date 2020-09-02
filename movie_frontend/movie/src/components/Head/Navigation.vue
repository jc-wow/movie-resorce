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
			this.$store.commit('getCurPage', val.target.textContent)
		}
	},
};
</script>

<style lang="scss" scoped>
.title {
  width: 100%;
  height: 8%;
  background-color: black;
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
</style>
