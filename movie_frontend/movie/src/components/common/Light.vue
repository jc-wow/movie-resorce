<template>
  <svg>
    <line
      :x1="position.x"
      :y1="position.y"
      :x2="position.x - 20"
      :y2="position.y + 50"
      style="stroke:rgb(255,0,0);stroke-width:2"
    />
    <line
      :x1="position.x"
      :y1="position.y"
      :x2="position.x + 20"
      :y2="position.y + 50"
      style="stroke:rgb(255,0,0);stroke-width:2"
    />
  </svg>
</template>

<script>
import * as d3 from "d3";

export default {
  name: "Light",
  props: {
    position: Object,
  },
};
</script>

<style scoped lang='scss'>
</style>