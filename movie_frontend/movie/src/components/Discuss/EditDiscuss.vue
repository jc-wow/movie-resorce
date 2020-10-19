<template>
  <div class="edit-discuss">
    <div class="edit-discuss-head"></div>
    <div class="edit-discuss-func">
      <el-button plain @click="preview">{{
        isPreview ? "返回编辑" : "预览"
      }}</el-button>
      <el-button plain type="primary" @click="post">提交</el-button>
    </div>
    <div class="edit-discuss-container" v-show="!isPreview">
      <el-input placeholder="添加标题" v-model="discussHead"></el-input>
      <Editor
        class="discuss-editor"
        @editorHtml="editorHtml"
        :height="editorHeight"
      ></Editor>
    </div>
    <div class="edit-discuss-login" v-show="!isPreview">
      <Login></Login>
    </div>
    <Preview
      :data="previewData"
      :head="discussHead"
      v-show="isPreview"
      @showEditor="preview"
    ></Preview>
  </div>
</template>

<script>
import Editor from "../common/Editor";
import Preview from "./Preview";
import Login from "../common/Login";
import { loginMixin } from "../../mixin/loginMixin.js";

export default {
  name: "editDiscuss",
  components: {
    Editor,
    Preview,
    Login,
  },
  mixins: [loginMixin],
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
      this.author = this.$store.state.userInfo.author;
      this.email = this.$store.state.userInfo.email;
      if (!this.checkUserinfo()) return;
      const param = {
        title: this.discussHead,
        author: this.author,
        tag: "",
        email: this.email,
        content: this.previewData,
      };
      this.$store.dispatch("postDiscuss", param).then((res) => {
        if (res.success) {
          this.$message({
            message: "恭喜，发表成功啦",
						type: "success",
						duration: 1500
          });
          this.saveUserinfo();
          this.$router.push({ name: "discuss" });
        }
      });
    },
    saveUserinfo() {
      if (sessionStorage.getItem("userInfo")) {
        sessionStorage.removeItem("userInfo");
      }
      sessionStorage.setItem(
        "userInfo",
        JSON.stringify({
          author: this.author,
          email: this.email,
        })
      );
    },
    editorHtml(val) {
      this.previewData = val;
    },
    listenLeavePage() {
      window.onbeforeunload = () => {
        return "sure";
      };
    },
  },
  destroyed() {
    window.onbeforeunload = null;
  },
};
</script>

<style lang="scss">
.edit-discuss {
  min-height: 100vh;
  display: flex;
  flex-direction: column;
  align-items: center;
  background-image: linear-gradient(
    to bottom,
    rgb(185, 185, 185),
    rgb(200, 200, 200) 30%,
    rgb(220, 220, 220)
  );

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

  .edit-discuss-login {
    height: 20vh;
    width: 55%;
  }
}
</style>