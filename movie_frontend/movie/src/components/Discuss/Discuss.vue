<template>
  <div class="discuss">
    <div class="head"></div>
    <AllDiscuss></AllDiscuss>
  </div>
</template>

<script>
import AllDiscuss from "./AllDiscuss";

export default {
  name: "discuss",
  components: {
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