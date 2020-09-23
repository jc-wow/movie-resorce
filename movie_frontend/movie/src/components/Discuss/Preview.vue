<template>
  <div class="preview">
    <div class="preview-edit">
      <el-button plain @click="returnEditor">返回编辑</el-button>
    </div>
    <div class='preview-text'>
      <div class="preview-title" v-html="head"></div>
      <div class="preview-content" v-html="data"></div>
    </div>
  </div>
</template>

<script>
export default {
  name: "preview",
  props: {
    data: String,
    head: String,
  },
  data() {
    return {};
  },
  methods: {
    returnEditor() {
      this.$emit("showEditor");
    },
  },
};
</script>

<style lang="scss" scoped>
.preview {
  width: 100%;

  .preview-edit {
    display: flex;
    justify-content: flex-end;
    width: 99.5%;
    margin-top: 0.1%;
  }
}
</style>