<template>
  <div class="allvideoby-year">
    <div class="center list flex-column">
      <div
        class="card flex-row"
        :class="{ open: video.open }"
        v-for="(video, index) in videoInfo"
        :key="'video_' + index"
        @click="showVideoDetail(video)"
      >
        <img class="book" :src="video.cover" referrerpolicy="no-referrer" />
        <div class="flex-column info">
          <div class="title">{{ video.title }}</div>
          <div class="director">
            <span>导演：</span>{{ getPeopleInfo(video.director) }}
          </div>
          <div class="actor">
            <span>演员：</span>{{ getPeopleInfo(video.actor) }}
          </div>
          <div class="hidden bottom summary">{{ video.summary }}</div>
        </div>
        <div class="flex-column group">
          <!-- <div class="members">
              <span class="current">14</span> /
              <span class="max">30</span>
            </div>
            <div class="hidden bottom">
              <button class="simple">Join</button>
            </div> -->
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
  data() {
    return {
      videoInfo: [],
      showLoadVideo: false,
      offset: 1,
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
        0
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
					res.data.rows.forEach(ele => {
						this.$set(ele, "open", false);
						this.videoInfo.push(ele);
					})
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
			this.videoInfo = this.$store.state.movieInfoByYear.rows;
			this.setInfoToVideo();
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
        font-size: 0.7rem;
        color: #888;
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
        & .book {
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
      height: 90px;
      & .book {
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
          font-size: 0.9rem;
          color: #fff;
          letter-spacing: 1px;
        }
        & .director {
          margin-top: 3%;
          font-size: 0.7rem;
          font-weight: normal;
          color: #888;
        }
        & .actor {
          font-size: 0.7rem;
          font-weight: normal;
          color: #888;
        }
      }
      & .group {
        margin-left: auto;
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