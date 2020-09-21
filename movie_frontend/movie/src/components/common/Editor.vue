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
        theme: "snow",
        placeholder: "添加想法",
        modules: {
          toolbar: [
            [{ size: ["14px", "16px", "18px"] }],
            [{ header: 1 }, { header: 2 }],
            ["bold", "italic", "underline", "strike"],
            ["blockquote", "code-block"],
            [{ list: "ordered" }, { list: "bullet" }],
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

  .ql-snow .ql-picker.ql-size .ql-picker-item[data-value="14px"]::before,
  .ql-snow
    .ql-picker.ql-size
    .ql-picker-label.ql-active[data-value="14px"]::before {
    content: "14px";
  }

  .ql-snow .ql-picker.ql-size .ql-picker-item[data-value="16px"]::before,
  .ql-snow
    .ql-picker.ql-size
    .ql-picker-label.ql-active[data-value="16px"]::before {
    content: "16px";
  }

  .ql-snow .ql-picker.ql-size .ql-picker-item[data-value="18px"]::before,
  .ql-snow
    .ql-picker.ql-size
    .ql-picker-label.ql-active[data-value="18px"]::before {
    content: "18px";
  }

  .ql-size .ql-picker-label::before {
    content: "16px" !important;
  }
}
</style>