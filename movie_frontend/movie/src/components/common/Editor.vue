<template>
  <div class="editor" @click="focus">
    <div id="announcementEditorToolbar">
      <span class="ql-formats">
        <select class="ql-size">
          <option selected>默认</option>
          <option value="16px">16px</option>
          <option value="18px">18px</option>
          <option value="22px">22px</option>
          <option value="30px">30px</option>
        </select>
      </span>
      <button class="ql-bold"></button>
      <button class="ql-italic"></button>
      <button class="ql-underline"></button>
      <button class="ql-list" value="ordered"></button>
      <button class="ql-list" value="bullet"></button>
      <select class="ql-align"></select>
    </div>
    <quill-editor
      ref="myQuillEditor"
      :content="content"
      :options="editorOption"
      @change="onEditorChange($event)"
    />
  </div>
</template>

<script>
import { quillEditor } from "vue-quill-editor";
import "quill/dist/quill.core.css";
import "quill/dist/quill.snow.css";
import "quill/dist/quill.bubble.css";
import Quill from "quill";

export default {
  name: "editor",
  components: {
    quillEditor,
  },
  props: {
    height: String,
  },
  data() {
    return {
      content: "",
      editorOption: {
        theme: "snow",
        placeholder: "添加想法...",
        modules: {
          toolbar: "#announcementEditorToolbar",
        },
      },
    };
  },
  methods: {
    onEditorChange({ quill, html, text }) {
      this.$emit("editorHtml", html);
      this.content = html;
		},
		// get editor focus
    focus() {
      this.$refs.myQuillEditor.quill.focus();
    },
  },
  created() {
    let Size = Quill.import("attributors/style/size");
    Size.whitelist = ["16px", "18px", "22px", "30px"];
    Quill.register(Size, true);
  },
  mounted() {
    document.getElementsByClassName(
      "ql-container"
    )[0].style = `min-height: ${this.height}`;
  },
};
</script>

<style lang="scss">
.editor {
  background-color: #fff;
  height: 100%;

  #announcementEditorToolbar {
    display: flex;
  }

  .quill-editor {
    .ql-container {
      font-size: 16px;

      .ql-blank {
        font-size: 15px;
      }
    }
  }
}
</style>