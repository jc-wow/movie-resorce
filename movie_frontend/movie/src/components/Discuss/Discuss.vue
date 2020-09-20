<template>
  <div class="discuss">
    <div class="head"></div>
    <AllDiscuss class="discuss-alldiscuss"></AllDiscuss>
    <!-- <Editor class='discuss-editor'></Editor> -->
  </div>
</template>

<script>
import Editor from "./Editor";
import AllDiscuss from "./AllDiscuss";

export default {
  name: "discuss",
  components: {
    Editor,
    AllDiscuss,
  },
};
</script>

<style lang="scss" scoped>
.discuss {
  .head {
    height: 8vh;
  }
}
</style>