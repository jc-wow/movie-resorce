<template>
  <div class="allvideobook">
    <div class="cover">
      <div class="book">
        <div
          class="book-page book-page-1"
          :class="{ 'allvideobook-load': loaded }"
          @click="selectPage($event)"
        ></div>
        <div class="book-page book-page-4">
          <div class="page-content-4">
            <AllVideosByYear :isPreviewVideo="isPreviewVideo"></AllVideosByYear>
          </div>
        </div>
        <div
          class="book-page book-page-2"
          :class="{ 'allvideobook-page': paging }"
        >
          <transition name="load">
            <div class="book-page-front" v-show="loaded">
              <AllVideosCategory
                @getMovieInfo="getMovieInfo"
                @selectPage="selectPage"
              ></AllVideosCategory>
            </div>
          </transition>
          <div class="book-page-back">
            <div class="page-content" v-show="showBackPageAni">
              <div
                class="video-img-content"
                v-for="(item, index) in movieInfo"
                :key="'movie_' + index"
                @click="selectMovie(item)"
              >
                <h4>{{ item.title }}</h4>
                <img
                  :src="item.cover"
                  onerror="this.style.display='none'"
                  referrerpolicy="no-referrer"
                />
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
import AllVideosByYear from "./AllVideosByYear";
import "../../style/waterfall.scss";
import { nextTick } from "process";

export default {
  name: "AllVideoBook",
  components: { AllVideosCategory, AllVideosByYear },
  data() {
    return {
      paging: false,
      loaded: false,
      movieInfo: [],
			showBackPageAni: false,
			isPreviewVideo: false
    };
  },
  methods: {
    selectPage(e) {
      if (
        !e ||
        e.currentTarget.className.includes("front") ||
        e.currentTarget.className.includes("1")
      ) {
        this.paging = true;
        this.showBackPageAni = true;
      } else {
        this.paging = false;
        if (this.backpageAni) clearTimeout(this.backpageAni);
        this.backpageAni = setTimeout(() => {
          this.showBackPageAni = false;
        }, 900);
      }
    },
    getMovieInfo() {
      const movieCount = this.$store.state.movieInfoByTime.rows.length;
      this.movieInfo = this.$store.state.movieInfoByTime.rows.slice(0, 20);
      let start = 0,
        end = 20;
      // get movie info every 60s
      if (this.getMovieInfoByTime) clearInterval(this.getMovieInfoByTime);
      this.getMovieInfoByTime = setInterval(() => {
        start += 20;
        end += 20;
        if (end > movieCount) {
          start = 0;
          end = 20;
        }
        this.movieInfo = this.$store.state.movieInfoByTime.rows.slice(
          start,
          end
        );
      }, 60000);
    },
    removeCheckFinishPageAnimation() {
      if (this.pageBackListen) {
        this.pageObj.removeEventListener(
          "transitionend",
          this.finishPageAnimationCallback()
        );
      }
    },
    finishPageAnimationCallback() {
      this.paging = false;
    },
    selectMovie(item) {
      this.$store.dispatch("getVideo", { id: item.id }).then((res) => {
        if (res.success) {
          this.$store.commit("getSearchVideo", res.data);
          this.isPreviewVideo = true;
        }
      });
    },
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

.allvideobook {
  --body-bg: rgb(220, 220, 220);
  --page-bg: #f5f5f5;
  --dark-text: #2a2935;
  --baseline: 12px;
  --base-size: var(--baseline) * 1.2;
  height: 92vh;
  margin-top: 8vh;
  background-color: rgb(0, 0, 0);
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

      &-page {
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

        &-1 {
          cursor: pointer;
          overflow: hidden;
          transform: rotateY(180deg);
          transform-origin: 100%;
        }

        &-2 {
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

        &-4 {
          cursor: pointer;
          padding: 0 1% 0 calc(var(--baseline) * 5);

          .page-content-4 {
            overflow: hidden;
          }
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

          .page-content {
            padding: var(--baseline);
            width: 100%;
            height: 100%;
            position: relative;
            text-align: center;
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
  }
}
</style>