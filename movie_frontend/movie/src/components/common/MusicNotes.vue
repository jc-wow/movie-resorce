<template>
  <div class="music-notes">
    <div class="muzieknootjes">
      <div class="noot-1">&#9835; &#9833;</div>
      <div class="noot-2">&#9833;</div>
      <div class="noot-3">&#9839; &#9834;</div>
      <div class="noot-4">&#9834;</div>
    </div>
  </div>
</template>

<script>
export default {
  name: "MusicNotes",
};
</script>

<style scoped lang="scss">
.music-notes {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100%;
	width: 100%;
  color: rgb(128, 122, 122);
	position: absolute;
	z-index: -1;

  .muzieknootjes {
    display: block;
    margin: auto;
    position: relative;
    width: 100%;
    height: 100%;
    border: 0px solid #fff;
  }

  .noot-1,
  .noot-2,
  .noot-3,
  .noot-4 {
    position: absolute;
    animation: notes 4s infinite linear;
    font-size: 2rem;
    opacity: 0;
  }

  .noot-1 {
    top: 50%;
    left: 0;
    animation-delay: 2s;
  }

  .noot-2 {
    top: 55%;
    left: 30%;
    animation-delay: 3s;
  }

  .noot-3 {
    top: 60%;
    left: 60%;
    animation-delay: 4.5s;
  }

  .noot-4 {
    top: 40%;
    left: 90%;
    animation-delay: 5s;
  }

  @keyframes notes {
    0% {
      transform: scale(1) translate(0, 0);
      opacity: 0;
    }
    50% {
      opacity: 0.5;
      transform: scale(1.5) translate(50%, -50%);
    }
    80% {
      opacity: 0;
      transform: scale(1.5) translate(100%, -100%);
    }
    100% {
      transform: scale(1.5) translate(100%, -100%);
      opacity: 0;
    }
  }
}
</style>