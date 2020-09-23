<template>
  <div class="preview">
    <div class="preview-title" v-html="head"></div>
    <div class="preview-content" v-html="data"></div>
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
};
</script>

<style lang="scss">
.preview {
  width: 60%;
  margin-top: 3%;

  .preview-title {
    text-align: center;
    font-weight: 600;
    font-size: 1.7rem;

    p {
      margin: 2px;
    }
  }

  .preview-content {
    margin-top: 7%;

    p {
      margin: 0;
    }
  }
}
</style>