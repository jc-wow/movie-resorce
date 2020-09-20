<template>
  <div class="light">
    <svg class="light-svgcontainer">
      <polygon
        class="light-blink"
        :points="`${position.x1},0 0,${coor.leftY} ${coor.rightX},${coor.rightY}`"
        style="fill: rgb(255, 255, 255, 0.1)"
      />
      <text
        v-for="(value, index) in content"
        :id="'light-text-' + index"
        class="light-text"
        :key="'light-text' + index"
        fill="#fff"
      >{{ value }}</text>
    </svg>
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
  data() {
    return {
      coor: {
        leftY: 0,
        rightX: 0,
        rightY: 0,
      },
    };
  },
  methods: {
    setTextPosition() {
      d3.selectAll("text")
        .attr("x", (d, i) => {
          return this.getTextXpoint(i);
        })
        .attr("y", (d, i) => {
          return this.getTextYpoint(i);
        })
        .style("cursor", "pointer")
        .on("click", (d, i) => this.selectText(d))
        .on("mouseover", function () {
          d3.select(this).style("opacity", 1);
        })
        .on("mouseout", function () {
          d3.select(this).style("opacity", 0.3);
        });
    },
    selectText(val) {
      const selectedText = val.target.innerHTML;
      if (selectedText === "关于首页") {
        window.ispopstate = false;
        this.$emit("getCurMoviedetail");
      }
    },
    getLightXCoor() {
      const lightClientObj = document
        .getElementsByClassName("light")[0]
        .getBoundingClientRect();
      this.coor.leftY = (lightClientObj.bottom - lightClientObj.top) / 1.5;
      this.coor.rightX = lightClientObj.right - lightClientObj.left;
      this.coor.rightY = this.coor.leftY;
    },
    getTextXpoint(index) {
      this.textObj = document.getElementById(`light-text-${index}`);
      this.textObjBox = this.textObj.getBBox();
      return this.position.x1 - this.textObjBox.width / 2;
    },
    getTextYpoint(index) {
      return this.coor.rightY / 2.2 + (this.coor.rightY * (index + 1)) / 7;
    },
  },
  watch: {
    "position.x1": function () {
      this.getLightXCoor();
      this.setTextPosition();
    },
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
  height: 90%;
  width: 100%;

  .light-svgcontainer {
    height: 100%;
    width: 100%;
    z-index: 999;
    position: relative;

    .light-blink {
      animation: blink 8s linear infinite;
    }

    .light-text {
      font-size: 1.2rem;
      opacity: 0.3;
    }
  }

  .light-content {
    color: #fff;
    position: absolute;
  }
}
</style>