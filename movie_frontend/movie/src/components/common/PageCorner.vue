<template>
  <div
    class="page-corner"
    :style="{
      transform:
        pageState === 'front' ? 'rotate(-270deg)' : 'rotate(-180deg)',
      left: pageState === 'front' ? 'none' : 0
    }"
    @click="select"
  ></div>
</template>

<script>
export default {
  name: "PageCorner",
  props: {
    pageState: String,
    isHanging: Boolean
  },
  data() {
    return {};
  },
  methods: {
    select() {
      this.$emit("page", this.pageState);
    },
  },
};
</script>

<style lang="scss" scoped>
.page-corner {
  z-index: 999;
  background: linear-gradient(
    45deg,
    #2e2e2e 24%,
    #5f5f5f 40%,
    #6f6f6f 43%,
    #5f5f5f 46%,
    #2f2f2f 50%,
    #000 50%,
    #000
  );
  width: 90px;
  height: 90px;
  border-radius: 0 0 0px 90px / 0 0 0 30px;
  position: absolute;
  bottom: 0;
  right: 0;
  overflow: hidden;
}
.page-corner:hover {
    cursor: pointer;
    background: linear-gradient(
    45deg,
    #ffffff 24%,
    #5f5f5f 40%,
    #6f6f6f 43%,
    #5f5f5f 46%,
    #2f2f2f 50%,
    #000 50%,
    #000
  );
}
</style>
