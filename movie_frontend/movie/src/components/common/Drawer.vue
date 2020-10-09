<template>
  <el-drawer
    :visible.sync="showDrawer"
    :with-header="false"
    direction="ttb"
    append-to-body="true"
    show-close="false"
  >
  </el-drawer>
</template>

<script>
export default {
  name: "drawer",
  props: {
    showDrawer: Boolean,
  },
};
</script>

<style lang="scss" scoped>
</style>