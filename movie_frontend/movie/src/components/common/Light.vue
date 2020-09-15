<template>
  <div class="light">
    <svg class="light-svgcontainer">
      <polygon
        class="light-blink"
        :points="`${this.position.x1},${this.position.y1} 
			${this.position.x2},${this.position.y2} 
			${this.position.x3},${this.position.y3}`"
        style="fill: rgb(255, 255, 255, 0.1)"
      />
      <text
        v-for="(value, index) in content"
        :class="'light-text-' + index"
        :key="'light-text' + index"
        fill="#fff"
      >{{ value }}</text>
    </svg>
    <!-- <div class="light-content">
      <p v-for="(value, index) in content" :key="'lightMenu' + index">{{ value }}</p>
    </div>-->
  </div>
</template>

<script>
import * as d3 from "d3";

export default {
  name: "Light",
  props: {
    position: Object,
    content: Array,
  },
  methods: {
		setTextPosition() {
			d3.selectAll('text')
				.attr((d, i) => {
					debugger
				})
		},
    getTextXpoint(index) {
      this.textObj = document.getElementsByClassName("light-text-" + index)[0];
      this.textObjClient = textObj.getBoundingClientRect();
      return (
        position.x1 - (this.textObjClient.right - this.textObjClient.left) / 2
      );
    },
    getTextYpoint(index) {
      return position.y1;
    },
	},
	mounted() {
		this.setTextPosition();
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

  .light-svgcontainer {
    height: 100%;
    width: 100%;

    .light-blink {
      animation: blink 8s linear infinite;
    }
  }

  .light-content {
    color: #fff;
    position: absolute;
  }
}
</style>