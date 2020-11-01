<template>
  <div class="allvideobook">
    <div class="cover">
      <div class="book">
        <div
          class="book__page book__page--1"
          :class="{ 'allvideobook-load': loaded }"
          @click="selectPage($event)"
        ></div>
        <div class="book__page book__page--4" @click="selectPage($event)">
          <div class="page__content">ask公开撒娇感觉</div>
        </div>
        <div
          class="book__page book__page--2"
          :class="{ 'allvideobook-page': paging }"
        >
          <transition name="load">
            <div
              class="book__page-front"
              @click="selectPage($event)"
              v-show="loaded"
            >
              <AllVideosCategory
                :category="categoryRight"
                @getMovieInfo="getMovieInfo"
              ></AllVideosCategory>
            </div>
          </transition>
          <div class="book__page-back" @click="selectPage($event)">
            <div class="page__content">
              <div
                class="video-img-content"
                v-for="(item, index) in movieInfo"
                :key="'movie_' + index"
              >
                <transition name="loadimage">
                  <el-image
                    v-show="item.load"
                    :src="item.cover"
                    referrerpolicy="no-referrer"
                    fit="cover"
                    @load="loadedImg(item, index)"
                  ></el-image>
                </transition>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import AllVideosCategory from "./AllVideosCategory";

export default {
  name: "AllVideoBook",
  components: { AllVideosCategory },
  data() {
    return {
      paging: false,
      loaded: false,
      movieInfo: [],
    };
  },
  methods: {
    selectPage(e) {
      const curClassName = e.currentTarget.className;
      if (curClassName.includes("front") || curClassName.includes("1")) {
        this.paging = true;
      } else {
        this.paging = false;
      }
    },
    loadedImg(ele, index) {
      setTimeout(() => (ele.load = true), 150 * index);
    },
    getMovieInfo() {
      this.movieInfo = [];
      this.movieInfo = this.$store.state.movieInfoByTime.slice(0, 20);
      this.movieInfo.forEach((ele) => {
        this.$set(ele, "load", false);
      });
    },
  },
  created() {
    this.categoryRight = [
      "2020s",
      "2010s",
      "2000s",
      "1990s",
      "1980s",
      "1970s",
      "1960s",
      "1950s",
      "1940s",
      "1930s",
      "1920s",
      "1910s",
      "1900s",
      "18th",
    ];
  },
  mounted() {
    this.loaded = true;
  },
};
</script>

<style scoped lang="scss">
* {
  box-sizing: border-box;
}

.allvideobook-page {
  transition: transform 0.9s cubic-bezier(0.645, 0.045, 0.355, 1) !important;
  transform: rotateY(-180deg) !important;
}

.allvideobook-load {
  transition: transform 1.5s cubic-bezier(0.645, 0.045, 0.355, 1) !important;
  transform: rotateY(0) !important;
}

.load-enter {
  opacity: 0;
}

.load-enter-active {
  transition: opacity 1.5s cubic-bezier(0.845, 0.045, 1, 1);
}

.load-enter-to {
  opacity: 1;
}

.loadimage-enter {
  width: 80%;
}

.loadimage-active {
  transition: width 1s ease;
}

.loadimage-to {
  width: 50%;
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
          transform: rotateY(180deg);
          transform-origin: 100%;
        }

        &--2 {
          padding: 0 calc(var(--baseline) * 3);
          position: absolute;
          right: 0;
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

          .page__content {
            padding: var(--baseline);
            height: 100%;
            position: relative;
            text-align: center;

            .page-content-container {
              height: 100%;
              width: 100%;
            }

            .el-image {
              position: absolute;
            }
          }
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