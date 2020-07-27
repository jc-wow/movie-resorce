<template>
  <div class="movie-menu">
    <img class="menu-close" src="../../assets/close.svg" @click="closeMenuPanel" />
    <div class="menu-title">
      <ul>
        <li @click="enterMovie">
          <span>影视</span>
        </li>
        <li>
          <span>原声</span>
        </li>
        <li>
          <span>讨论</span>
        </li>
        <li>
          <span>本站</span>
        </li>
      </ul>
    </div>
  </div>
</template>

<script>
export default {
  name: "movie-menu",
  data() {
    return {};
  },
  methods: {
    closeMenuPanel() {
      this.$store.commit("showMenu");
    },
    enterMovie() {
      this.$store.commit("showMenu");
      this.$router.push({ name: "movie" }).catch(err => err);
    }
  }
};
</script>

<style lang="scss" scoped>
.movie-menu {
  height: 100%;
  width: 20%;
  background-color: #f4f7f6;
  position: fixed;
  top: 0;
  z-index: 999;

  .menu-close {
    height: 5%;
    margin-top: 5%;
    margin-left: 80%;
  }

  .menu-title {
    font-size: 1.5rem;
    margin-top: 40%;

    ul {
      list-style: none;
    }

    li span {
      display: block;
      padding: 6% 30%;
      font-weight: bold;
      color: #202121;
      cursor: pointer;
      background: #f4f7f6;
      border-bottom: 1px solid #e6eaea;
    }
  }
}
</style>