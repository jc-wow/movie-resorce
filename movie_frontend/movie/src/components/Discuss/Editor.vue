<template>
  <div class="editor">
    <quill-editor :content="content" :options="editorOption" @change="onEditorChange($event)" />
  </div>
</template>

<script>
import { quillEditor } from "vue-quill-editor";
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
        placeholder: "添加想法",
        modules: {
          toolbar: [
            [{ size: ["14px", "16px", "18px"] }],
            ["bold", "italic", "underline", "strike"],
            ["blockquote", "code-block"],
            [{ list: "ordered" }, { list: "bullet" }],
            [{ font: [] }],
            [{ align: [] }],
          ],
        },
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

<style lang="scss">
.editor {
  background-color: #fff;

  .ql-snow .ql-picker.ql-size .ql-picker-item[data-value="14px"]::before {
    content: "14px";
    font-size: 14px !important;
  }

  .ql-snow .ql-picker.ql-size .ql-picker-item[data-value="16px"]::before {
    content: "16px";
    font-size: 16px !important;
  }

  .ql-snow .ql-picker.ql-size .ql-picker-item[data-value="18px"]::before {
    content: "18px";
    font-size: 18px !important;
  }
}
</style>