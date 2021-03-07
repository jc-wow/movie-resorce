<template>
  <div class="allvideoby-year-view" v-if="isPreviewVideo">
    <div class="outer" @click="backToVideo">
      <div class="inner">
        <label>Back</label>
      </div>
    </div>
    <div class="view-video-container">
      <img
        class="view-video"
        :src="$store.state.searchVideo.cover"
        referrerpolicy="no-referrer"
      />
    </div>
    <div class="view-video-info">
      <div class="view-title">
        {{ $store.state.searchVideo.title }}
        <a
          class="allvideo-detail-doubanlink"
          :href="$store.state.searchVideo.url"
          target="_blank"
          v-if="$store.state.searchVideo.url"
        >
          <img src="../../assets/douban.jpg" width="23" height="23" />
        </a>
        <a
          class="allvideo-detail-imdblink"
          :href="$store.state.searchVideo.imdb"
          target="_blank"
          v-if="$store.state.searchVideo.imdb"
        >
          <img src="../../assets/imdb.jpg" width="23" height="23" />
        </a>
      </div>
      <div class="view-director">
        <span>导演：</span>{{ $store.state.searchVideo.director }}
      </div>
      <div class="view-actor">
        <span>演员：</span>{{ $store.state.searchVideo.actor }}
      </div>
      <div class="view-release-date">
        <span>上映日期：</span>{{ $store.state.searchVideo.release_date }}
      </div>
      <div class="view-summary">
        {{ $store.state.searchVideo.summary }}
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "AllvideobyYearView",
  props: {
    videoInfo: Array,
  },
  data() {
    return {
      isPreviewVideo: false,
    };
  },
  methods: {
    backToVideo() {
      this.$store.commit("getIsPreviewVideoState", false);
    },
  },
  watch: {
    "$store.state.isPreviewVideo": function () {
      this.isPreviewVideo = this.$store.state.isPreviewVideo;
    },
  },
};
</script>

<style lang="scss" scoped>
.outer {
  position: relative;
  margin: auto;
  width: 2rem;
  cursor: pointer;
  position: absolute;
  left: 2%;
}

.inner {
  width: inherit;
  text-align: center;
}

label {
  font-size: 0.8em;
  line-height: 2.5em;
  text-transform: uppercase;
  color: #fff;
  transition: all 0.3s ease-in;
  opacity: 0;
  cursor: pointer;
}

.inner:before,
.inner:after {
  position: absolute;
  content: "";
  height: 1px;
  width: inherit;
  background: #ffc107;
  left: 0;
  transition: all 0.3s ease-in;
}

.inner:before {
  top: 50%;
  transform: rotate(45deg);
}

.inner:after {
  bottom: 50%;
  transform: rotate(-45deg);
}

.outer:hover label {
  opacity: 1;
}

.outer:hover .inner:before,
.outer:hover .inner:after {
  transform: rotate(0);
}

.outer:hover .inner:before {
  top: 0;
}

.outer:hover .inner:after {
  bottom: 0;
}
.allvideoby-year-view {
  min-height: 94%;
  background-color: #131325;
  display: flex;
  padding-top: 3%;
  padding-bottom: 3%;

  .view-back {
    position: absolute;
    left: 5%;
    width: 1.5rem;
    cursor: pointer;
  }

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
      display: flex;
      img {
        border-radius: 11.5px;
      }
      a {
        margin-left: 1%;
      }
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

    .view-release-date {
      font-size: 0.8rem;
      font-weight: normal;
      color: rgb(201, 201, 201);
      margin-top: 2%;
    }
  }
}
</style>
