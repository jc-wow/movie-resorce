<template>
  <div class="allvideoby-year">
      <div class="allvideoby-year-view" v-if="previewVideo">
        <img
          class="view-back"
          src="../../assets/back.svg"
          @click="backToVideo"
        />
        <div class="view-video-container">
          <img
            class="view-video"
            :src="$store.state.searchVideo.cover"
            referrerpolicy="no-referrer"
          />
        </div>
        <div class="view-video-info">
          <div class="view-title">{{ $store.state.searchVideo.title }}</div>
          <div class="view-director">
            <span>导演：</span>{{ $store.state.searchVideo.director }}
          </div>
          <div class="view-actor">
            <span>演员：</span>{{ $store.state.searchVideo.actor }}
          </div>
          <div class="view-summary">
            <span></span>{{ $store.state.searchVideo.summary }}
          </div>
        </div>
      </div>
    <div class="center list flex-column" v-show="!previewVideo">
      <div
        class="card flex-row"
        :class="{ open: video.open }"
        v-for="(video, index) in videoInfo"
        :key="'video_' + index"
        @click="showVideoDetail(video)"
      >
        <img class="video" :src="video.cover" referrerpolicy="no-referrer" />
        <div class="flex-column info">
          <div class="title">{{ video.title }}</div>
          <div
            class="director"
            :style="video.open ? openInfoStyle : closeInfoStyle"
          >
            <span>导演：</span>{{ getPeopleInfo(video.director) }}
          </div>
          <div
            class="actor"
            :style="video.open ? openInfoStyle : closeInfoStyle"
          >
            <span>演员：</span>{{ getPeopleInfo(video.actor) }}
          </div>
          <div class="hidden bottom summary">{{ video.summary }}</div>
        </div>
      </div>
      <div class="card flex-flow load-video" v-show="showLoadVideo">
        加载中...
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "AllVideosByYear",
  props: {
    isPreviewVideo: Boolean,
  },
  data() {
    return {
      videoInfo: [],
      showLoadVideo: false,
      offset: 1,
      previewVideo: this.isPreviewVideo,
      openInfoStyle: {
        fontSize: "0.8rem",
        fontWeight: "normal",
        color: "rgb(201, 201, 201)",
        textOverflow: "unset",
        whiteSpace: "unset",
        overflow: "unset",
      },
      closeInfoStyle: {
        fontSize: "0.8rem",
        fontWeight: "normal",
        color: "rgb(201, 201, 201)",
        textOverflow: "ellipsis",
        whiteSpace: "nowrap",
        overflow: "hidden",
      },
    };
  },
  methods: {
    showVideoDetail(e) {
      if (!e.open) {
        for (let l = this.videoInfo.length, i = 0; i < l; i++) {
          if (this.videoInfo[i].open) {
            this.videoInfo[i].open = false;
            e.open = true;
            return;
          }
        }
        e.open = true;
      }
    },
    backToVideo() {
      this.previewVideo = false;
      this.$emit("changePreviewVideo", this.previewVideo);
    },
    getPeopleInfo(item) {
      return item.split("/").slice(0, 3).join("/");
    },
    checkScollToBottom() {
      if (
        this.videoInfo.length + 1 >=
        this.$store.state.movieInfoByYear.count
      ) {
        return;
      }

      const ctop = this.containerObj.scrollTop;
      if (
        this.containerObj.scrollHeight -
          this.containerObj.offsetHeight -
          ctop <=
        10
      ) {
        this.showLoadVideo = true;
        this.getVideoByYear();
      }
    },
    getVideoByYear() {
      const year = this.$store.state.curSelectYear;
      this.offset++;
      this.$store
        .dispatch("getMovieInfoByTime", {
          time: year,
          offset: this.offset,
          limit: 20,
        })
        .then((res) => {
          res.data.rows.forEach((ele) => {
            this.$set(ele, "open", false);
            this.videoInfo.push(ele);
          });
          this.videoInfo.push(...res.data.rows);
          this.showLoadVideo = false;
        });
    },
    throttle(fn, time) {
      let timer = null;
      return function () {
        if (!timer) {
          timer = setTimeout(() => {
            timer = null;
            fn();
          }, time);
        }
      };
    },
    listenScroll() {
      this.containerObj = document.getElementsByClassName("allvideoby-year")[0];
      this.containerObj.addEventListener(
        "scroll",
        this.throttle(this.checkScollToBottom, 500)
      );
      this.cbottom = this.containerObj.getBoundingClientRect().height;
    },
    setInfoToVideo() {
      this.videoInfo.forEach((ele) => {
        this.$set(ele, "open", false);
      });
    },
  },
  watch: {
    "$store.state.movieInfoByYear": function () {
      this.containerObj.scrollTo(0, 0);
      this.videoInfo = this.$store.state.movieInfoByYear.rows;
      this.offset = 1;
      this.setInfoToVideo();
    },
    isPreviewVideo: function () {
      this.previewVideo = this.isPreviewVideo;
    },
  },
  mounted() {
    this.listenScroll();
  },
};
</script>

<style lang="scss" scoped>
$dark: #131325;

.allvideoby-year::-webkit-scrollbar-track {
  -webkit-box-shadow: inset 0 0 6px rgba(0, 0, 0, 0.3);
  border-radius: 10px;
  background-color: #f5f5f5;
}

.allvideoby-year::-webkit-scrollbar {
  width: 12px;
  background-color: #f5f5f5;
}

.allvideoby-year::-webkit-scrollbar-thumb {
  border-radius: 10px;
  -webkit-box-shadow: inset 0 0 6px rgba(0, 0, 0, 0.3);
  background-color: #9e9e9e;
}

.allvideoby-year {
  height: 100%;
  width: 100%;
  overflow-y: auto;
  position: relative;

  .view-back {
    position: absolute;
    left: 5%;
    width: 1.5rem;
    cursor: pointer;
  }

  .allvideoby-year-view {
    min-height: 94%;
    background-color: $dark;
    display: flex;
    padding-top: 3%;
    padding-bottom: 3%;

    .view-video-container {
      padding-left: 3%;
      .view-video {
        width: 100%;
        height: 100%;
        object-fit: contain;
      }
    }

    .view-video-info {
      padding: 0px 1.5rem;
      font-family: "Montserrat";
      font-weight: bold;
      width: 65%;
      line-height: 1.1rem;
      display: flex;
      flex-direction: column;
      justify-content: center;

      .view-title {
        font-size: 1rem;
        color: #fff;
        letter-spacing: 1px;
      }

      .view-director {
        margin-top: 3%;
        font-size: 0.8rem;
        font-weight: normal;
        color: rgb(201, 201, 201);
      }

      .view-actor {
        font-size: 0.8rem;
        font-weight: normal;
        color: rgb(201, 201, 201);
        margin-top: 2%;
      }

      .view-summary {
        font-size: 0.8rem;
        color: rgb(201, 201, 201);
        font-weight: normal;
        margin-top: 2%;
      }
    }
  }

  .flex-row {
    display: flex;
    flex-flow: row;
    align-items: center;
  }
  .flex-column {
    display: flex;
    flex-flow: column;
  }
  .center {
    padding-top: 3%;
  }
  .list {
    border-radius: 3px;
    overflow: hidden;
    & .card {
      cursor: pointer;
      margin-bottom: 10px;
      perspective: 600px;
      transition: all 0.1s;
      & .bottom {
        height: 0px;
        overflow: hidden;
        font-size: 0.8rem;
        color: rgb(201, 201, 201);
        font-weight: normal;
      }
      &.open {
        padding: 5%;
        height: auto;
        & .bottom {
          margin-top: 10px;
          height: 100%;
          overflow: visible;
        }
        & .video {
          transform: rotateY(50deg);
          box-shadow: -10px 10px 10px 2px rgba(0, 0, 0, 0.2),
            -2px 0px 0px 0px #888;
          transition: all 0.5s;
          transition-delay: 0.05s;
        }
        & .info {
          transform: translate(0, -10px);
        }
        & .members {
          padding: 15px 20px;
          border-radius: 4px;
          align-self: flex-start;
        }
      }
      & button.simple {
        cursor: pointer;
        color: #ccc;
        border: none;
        outline: none;
        border-radius: 4px;
        background-color: #1ea94b;
        padding: 15px 20px;
        font-family: "Montserrat";
        font-weight: bold;
        transition: all 0.1s;
        &:hover {
          box-shadow: 0px 15px 20px -5px rgba(0, 0, 0, 0.3);
          transform: translate(0, -2px);
        }
      }
      background-color: lighten($dark, 8%);
      box-shadow: 0px 2px 10px rgba(0, 0, 0, 0.2);
      overflow: hidden;
      height: 10vh;
      & .video {
        transition: all 0.5s;
        width: 120px;
        box-shadow: 0px 2px 10px rgba(0, 0, 0, 0.3);
        overflow: hidden;
      }
      & .info {
        transition: all 0.2s;
        min-width: 200px;
        padding: 0px 1.5rem;
        font-family: "Montserrat";
        font-weight: bold;
        width: 65%;
        line-height: 1.1rem;
        & .title {
          font-size: 1rem;
          color: #fff;
          letter-spacing: 1px;
        }
        & .director {
          margin-top: 3%;
          font-size: 0.8rem;
          font-weight: normal;
          color: rgb(201, 201, 201);
          text-overflow: ellipsis;
          white-space: nowrap;
          overflow: hidden;
        }
        &.director:hover {
          text-overflow: none;
          white-space: none;
          overflow: none;
        }
        & .actor {
          font-size: 0.8rem;
          font-weight: normal;
          color: rgb(201, 201, 201);
          text-overflow: ellipsis;
          white-space: nowrap;
          overflow: hidden;
        }
        &.actor:hover {
          text-overflow: none;
          white-space: none;
          overflow: none;
        }
      }
      & .members {
        transition: all 0.1s;
        padding: 40px;
        font-family: "Montserrat";
        color: #ccc;
        background-color: lighten($dark, 5%);
        & .current {
          font-weight: bold;
          margin-right: 10px;
        }
        & .max {
          opacity: 0.5;
          margin-left: 10px;
        }
      }
    }

    .load-video {
      height: 4vh;
      text-align: center;
      line-height: 4vh;
      color: #fff;
    }
  }
}
</style>