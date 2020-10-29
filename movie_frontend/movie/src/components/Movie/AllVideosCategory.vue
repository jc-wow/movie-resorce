<template>
  <div class="allvideos-category">
    <div v-for="(item, index) in category" :key="'category_' + index">
      {{ item }}
    </div>
  </div>
</template>

<script>
export default {
  name: "AllVideosCategory",
  props: {
    category: Array,
  },
  data() {
    return {};
  },
};
</script>

<style scoped lang='scss'>
</style>