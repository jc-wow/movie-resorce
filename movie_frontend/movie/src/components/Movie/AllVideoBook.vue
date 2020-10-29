<template>
  <div class="allvideobook">
    <div class="cover">
      <div class="book">
        <label
          for="page-1"
          class="book__page book__page--1"
        >
          <AllVideosCategory :category="categoryLeft"></AllVideosCategory>
        </label>
        <label
          for="page-2"
          class="book__page book__page--4"
        >
          <div class="page__content">
            ask公开撒娇感觉
            <!-- <div class="page__number">3</div> -->
          </div>
        </label>
        <input type="radio" name="page" id="page-1" />
        <input type="radio" name="page" id="page-2" />
        <label class="book__page book__page--2" @click="selectPage($event)">
          <div class="book__page-front" @click="selectPage($event)">
            <AllVideosCategory :category="categoryRight"></AllVideosCategory>
          </div>
          <div class="book__page-back" @click="selectPage($event)">
            <div class="page__content">
              ask公开撒娇感觉
              <!-- <div class="page__number">2</div> -->
            </div>
          </div>
        </label>
      </div>
    </div>
  </div>
</template>

<script>
import AllVideosCategory from "./AllVideosCategory";

export default {
  name: "AllVideoBook",
  components: { AllVideosCategory },
  methods: {
    selectPage(e) {
      console.log(e);
    },
  },
  created() {
    this.categoryLeft = [
      "2020s",
      "2010s",
      "2000s",
      "1990s",
      "1980s",
      "1970s",
      "1960s",
    ];
    this.categoryRight = [
      "1950s",
      "1940",
      "1930",
      "1920",
      "1910",
      "1900",
      "19th",
    ];
  },
};
</script>


<style scoped lang="scss">
* {
  box-sizing: border-box;
}

.allvideobook {
  --body-bg: rgb(220, 220, 220);
  --page-bg: #f5f5f5;
  --dark-text: #2a2935;
  --baseline: 12px;
  --base-size: var(--baseline) * 1.2;
  height: 92vh;
  margin-top: 8vh;
  background-color: #000;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;

  .cover {
    width: 70%;
    height: 90%;
    box-shadow: 0 0 100px rgba(0, 0, 0, 0.3);

    .book {
      width: 100%;
      height: 100%;
      display: flex;
      perspective: 1200px;

      &__page {
        position: relative;
        width: 50%;
        height: 100%;
        display: grid;
        transform: rotateY(0deg);
        transition: transform 0.9s cubic-bezier(0.645, 0.045, 0.355, 1);
        transform-origin: 0% 0%;
        background-color: var(--page-bg);
        background-image: linear-gradient(
          90deg,
          rgba(227, 227, 227, 1) 0%,
          rgba(247, 247, 247, 0) 18%
        );

        &:nth-of-type(1) {
          background-image: linear-gradient(
            -90deg,
            rgba(227, 227, 227, 1) 0%,
            rgba(247, 247, 247, 0) 18%
          );
        }

        &--1 {
          cursor: pointer;
          overflow: hidden;

          // .allvideobook-video-container {
          //   position: absolute;
          //   top: 0;
          //   bottom: 0;
          //   width: 100%;
          //   height: 100%;
          //   overflow: hidden;

          //   video {
          //     min-width: 100%;
          //     min-height: 100%;
          //     /* Setting width & height to auto prevents the browser from stretching or squishing the video */
          //     width: auto;
          //     height: auto;

          //     /* Center the video */
          //     position: absolute;
          //     top: 50%;
          //     left: 50%;
          //     transform: translate(-50%, -50%);
          //   }
          // }
        }

        &--2 {
          position: absolute;
          right: 0;
          pointer-events: none;
          transform-style: preserve-3d;
          background-color: var(--page-bg);
          background-image: linear-gradient(
            90deg,
            rgba(227, 227, 227, 1) 0%,
            rgba(247, 247, 247, 0) 18%
          );
        }

        &--4 {
          cursor: pointer;
          padding: 0 calc(var(--baseline) * 3);
        }

        &-front {
          position: absolute;
          width: 100%;
          height: 100%;
          transform: rotateY(0deg) translateZ(1px);
        }

        &-back {
          position: absolute;
          width: 100%;
          height: 100%;
          padding: 0 calc(var(--baseline) * 1.8);
          transform: rotateY(180deg) translateZ(1px);
        }

        .page__content {
          padding: var(--baseline);
          height: 100%;
          position: relative;
          text-align: center;
        }
      }
      .page__number {
        position: absolute;
        bottom: var(--baseline);
        width: calc(100% - (var(--baseline) * 2));
        font-family: var(--title);
        font-size: calc(var(--base-size) * 0.67);
        text-align: center;
      }
    }

    input[type="radio"] {
      display: none;

      &:checked + .book__page {
        transition: transform 0.9s cubic-bezier(0.645, 0.045, 0.355, 1);
        transform: rotateY(-180deg);
      }
    }
  }
}
</style>