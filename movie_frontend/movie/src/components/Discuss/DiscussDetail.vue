<template>
  <div class="discuss-detail">
    <section class="discuss-detail-section">
      <header class="discuss-detail-header">
        <h1>{{ discuss.title }}</h1>
      </header>
      <div class="discuss-detail-info">
        <span>来自：</span>
        <span>{{ discuss.author }}</span>
        <span class="discuss-detail-time">{{ utils.formatDate(discuss.updated_at) }}</span>
      </div>
      <article v-html="discuss.content" class="discuss-detail-content"></article>
    </section>
    <el-divider></el-divider>
    <div class="discuss-detail-reply"></div>
    <p style="width: 60%; font-size: 0.8rem">发表想法：</p>
    <div class="discuss-detail-newreply">
      <Editor :height="editorHeight" @editorHtml="editorHtml"></Editor>
      <el-button plain size="small" style="float: right; margin-top: 2%;" @click="updateDiscuss">发表</el-button>
    </div>
  </div>
</template>

<script>
import Editor from "../common/Editor";

export default {
  name: "discussDetail",
  components: {
    Editor,
  },
  data() {
    return {
      discuss: {},
      editorHeight: "30vh",
    };
  },
  methods: {
    saveDiscuss() {
      sessionStorage.setItem("discussDetail", JSON.stringify(this.discuss));
    },
    editorHtml(val) {
      this.reqParam = {
        id: this.$store.state.selectedDiscuss.id,
        reply: val,
      };
    },
    updateDiscuss() {
      this.$store.dispatch("updateDiscuss", this.reqParam);
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

<style lang="scss">
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

    .discuss-detail-info {
      margin-top: 4%;
      font-size: 0.8rem;
      font-weight: 400;
      opacity: 0.7;

      .discuss-detail-time {
        margin-left: 2%;
      }
    }

    .discuss-detail-content {
      margin-top: 7%;
    }
  }
  .el-divider {
    width: 60%;
  }

  .discuss-detail-newreply {
    width: 60%;
    min-height: 30vh;
  }
}
</style>