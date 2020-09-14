<template>
  <svg class="light">
    <polygon
      class="light-blink"
      :points="`${this.position.x},${this.position.y} ${this.position.x + 1.1 * this.position.left},
        ${this.position.y + 1.5 * this.position.top} ${this.position.x - 1.1 * this.position.left},
        ${this.position.y + 1.5 * this.position.top}`"
      style="fill: rgb(255, 255, 255, 0.1)"
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
@keyframes blink {
  50% {
    opacity: 0;
  }
}

.light {
  height: 100%;
  width: 100%;

  .light-blink {
    animation: blink 8s linear infinite;
  }
}
</style>