<template>
  <div class="allvideo-detail">
    <div class="center list flex-column" v-show="!isPreviewVideo">
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
          <div
            class="release-date"
            :style="video.open ? openInfoStyle : closeInfoStyle"
          >
            <span>上映日期: </span>{{ video.release_date }}
          </div>
          <div class="bottom">{{ video.summary }}</div>
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
  name: "AllVideoDetail",
  props: {
    isPreviewVideo: Boolean,
    videoInfo: Array,
    showLoadVideo: Boolean,
    containerClassName: String,
  },
  data() {
    return {
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
    getPeopleInfo(item) {
      if (item.length === 0) return "";
      return item.split("/").slice(0, 3).join("/");
    },
    checkScollToBottom() {
      if (
        this.videoInfo.length + 1 >=
        this.$store.state.movieInfoByYear.count
      ) {
        return;
      }

      const ctop = this.container.scrollTop;
      if (
        this.container.scrollHeight - this.container.offsetHeight - ctop <=
        10
      ) {
        this.$emit("changeShowLoadVideoState", true);
        this.$parent.getVideoByYear();
      }
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
      if (this.containerClassName.length === 0) return;
      this.container = document.getElementsByClassName(
        this.containerClassName
      )[0];
      this.container.addEventListener(
        "scroll",
        this.throttle(this.checkScollToBottom, 500)
      );
      this.cbottom = this.container.getBoundingClientRect().height;
    },
  },
  mounted() {
    this.$nextTick(this.listenScroll);
  },
  destroyed() {
    this.container.removeEventListener(
      "scroll",
      this.throttle(this.checkScollToBottom, 500)
    );
  },
};
</script>

<style lang="scss" scoped>
$dark: #131325;

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
    height: 16vh;
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
</style>
