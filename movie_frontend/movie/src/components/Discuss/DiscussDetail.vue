<template>
  <div class="discuss-detail">
    <section class="discuss-detail-section">
      <header class="discuss-detail-header">
        <h1>{{ discuss.title }}</h1>
      </header>
      <article v-html="discuss.content" class="discuss-detail-content"></article>
    </section>
    <div class="discuss-detail-reply"></div>
  </div>
</template>

<script>
export default {
  name: "discussDetail",
  data() {
    return {
      discuss: {},
    };
  },
  methods: {
    saveDiscuss() {
      sessionStorage.setItem("discussDetail", JSON.stringify(this.discuss));
    },
  },
  mounted() {
    const discuss = JSON.parse(sessionStorage.getItem("discussDetail"));
    if (discuss && Object.keys(discuss).length !== 0) {
      this.discuss = discuss;
    } else {
      this.discuss = this.$store.state.selectedDiscuss;
      this.saveDiscuss();
    }
  },
};
</script>

<style lang="scss" scoped>
.discuss-detail {
  min-height: 92vh;
  padding-top: 8vh;
	display: flex;
	flex-direction: column;
  align-items: center;
  background-color: #e4e4e1;
  background-image: radial-gradient(
      at top center,
      rgba(255, 255, 255, 0.03) 0%,
      rgba(0, 0, 0, 0.03) 100%
    ),
    linear-gradient(
      to top,
      rgba(255, 255, 255, 0.1) 0%,
      rgba(143, 152, 157, 0.6) 100%
    );
  background-blend-mode: normal, multiply;

  .discuss-detail-section {
    width: 60%;
		padding-top: 1%;

    .discuss-detail-header {
      text-align: center;
    }

    .discuss-detail-content {
      margin-top: 9%;
    }
  }
}
</style>