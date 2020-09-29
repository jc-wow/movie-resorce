<template>
  <div class="edit-discuss">
    <div class="edit-discuss-head"></div>
    <div class="edit-discuss-func">
      <el-button plain @click="preview">{{ isPreview ? '返回编辑' : '预览' }}</el-button>
      <el-button plain type="primary" @click="post">提交</el-button>
    </div>
    <div class="edit-discuss-container" v-show="!isPreview">
      <el-input placeholder="添加标题" v-model="discussHead"></el-input>
      <Editor class="discuss-editor" @editorHtml="editorHtml" :height="editorHeight"></Editor>
    </div>
    <Preview :data="previewData" :head="discussHead" v-show="isPreview" @showEditor="preview"></Preview>
  </div>
</template>

<script>
import Editor from "../common/Editor";
import Preview from "./Preview";

export default {
  name: "editDiscuss",
  components: {
    Editor,
    Preview,
  },
  data() {
    return {
      discussHead: "",
      previewData: "",
      isPreview: false,
      editorHeight: "60vh",
    };
  },
  methods: {
    preview() {
      this.isPreview = !this.isPreview;
    },
    post() {
      const param = {
        title: this.discussHead,
        author: "",
        tag: "",
        content: this.previewData,
      };
      this.$store.dispatch("postDiscuss", param);
    },
    editorHtml(val) {
      this.previewData = val;
    },
  },
};
</script>

<style lang="scss">
.edit-discuss {
  min-height: 100vh;
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

  .edit-discuss-head {
    height: 8vh;
  }

  .edit-discuss-func {
    width: 99%;
    margin-top: 0.1%;
    display: flex;
    justify-content: flex-end;
  }

  .edit-discuss-container {
    width: 100%;
		margin-top: 1%;
    display: flex;
    flex-direction: column;
    align-items: center;
    overflow-y: auto;

    .el-input {
      width: 55%;
      margin-top: 3%;

      .el-input__inner {
        font-weight: 500;
        font-size: 1.1rem;
      }
    }

    .discuss-editor {
      width: 55%;
      margin-top: 1%;
    }
  }
}
</style>