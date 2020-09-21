<template>
  <div class="edit-discuss">
    <div class="edit-discuss-head"></div>
    <el-input placeholder="添加标题" v-model="discussHead"></el-input>
    <Editor class="discuss-editor"></Editor>
  </div>
</template>

<script>
import Editor from "./Editor";

export default {
	name: "editDiscuss",
	data() {
		return {
			discussHead: ''
		}
	},
  components: {
    Editor,
  },
};
</script>

<style lang="scss" scoped>
.edit-discuss {
  height: 100vh;
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

  .el-input {
    width: 55%;
  }
  .discuss-editor {
    width: 55%;
  }
}
</style>