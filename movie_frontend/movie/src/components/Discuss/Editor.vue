<template>
  <div class="editor">
    <quill-editor :content="content" :options="editorOption" @change="onEditorChange($event)" />
  </div>
</template>

<script>
import { quillEditor } from "vue-quill-editor"; //调用编辑器
import "quill/dist/quill.core.css";
import "quill/dist/quill.snow.css";
import "quill/dist/quill.bubble.css";

export default {
  name: "editor",
  components: {
    quillEditor,
  },
  data() {
    return {
      content: "",
      editorOption: {
        theme: "snow",
      },
    };
  },
  methods: {
    onEditorChange({ quill, html, text }) {
      console.log("editor change!", quill, html, text);
      this.content = html;
    },
  },
};
</script>

<style lang="scss" scoped>
.editor {
	background-color: #fff;
}
</style>