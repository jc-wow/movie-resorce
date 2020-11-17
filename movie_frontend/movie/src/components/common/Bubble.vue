<template>
  <div class="bubble">
    <div class="bubble-container">
      <div class="bubble-shape"></div>
    </div>
  </div>
</template>
<script>
export default {
  name: "Bubble",
};
</script>

<style scoped lang='scss'>
@keyframes morph {
  0% {
    border-radius: 60% 40% 30% 70% / 60% 30% 70% 40%;
    background: linear-gradient(45deg, #88d5bf 0%, #5d6bf8 100%);
  }

  50% {
    border-radius: 30% 60% 70% 40% / 50% 60% 30% 60%;
    background: linear-gradient(45deg, #e27fcb 0%, #5d6bf8 100%);
  }

  100% {
    border-radius: 60% 40% 30% 70% / 60% 30% 70% 40%;
    background: linear-gradient(45deg, #88d5bf 0%, #5d6bf8 100%);
  }
}
/* body {
  background: #005;
} */
.bubble {
  width: 100%;
  height: 100%;
  position: absolute;

  .bubble-container {
    align-items: center;
    display: flex;
    justify-content: center;
  }

  .bubble-shape {
    background: linear-gradient(45deg, #88d5bf 0%, #88d5bf 100%);
    animation: morph 8s ease-in-out infinite;
    border-radius: 60% 40% 30% 70% / 60% 30% 70% 40%;
    height: 400px;
    transition: all 1s ease-in-out;
    width: 400px;
    z-index: 5;
  }
}
</style>