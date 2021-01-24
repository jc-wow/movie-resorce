<template>
  <div class="allvideoby-year-view" v-if="isPreviewVideo">
    <img
      class="view-back"
      src="../../assets/back.svg"
      @click="backToVideo"
      v-show="videoInfo.length !== 0"
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
