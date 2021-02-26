<template>
  <div class="allvideoby-year">
    <AllvideobyYearView :videoInfo="videoInfo"></AllvideobyYearView>
    <AllVideoDetail
      :isPreviewVideo="isPreviewVideo"
      :videoInfo="videoInfo"
      :showLoadVideo="showLoadVideo"
      :containerClassName="containerClassName"
    ></AllVideoDetail>
  </div>
</template>

<script>
import AllvideobyYearView from "./AllVideoView";
import AllVideoDetail from "./AllVideoDetail";

export default {
  name: "AllVideosByYear",
  components: { AllvideobyYearView, AllVideoDetail },
  data() {
    return {
      videoInfo: [],
      showLoadVideo: false,
      offset: 1,
      isPreviewVideo: false,
      containerClassName: "allvideoby-year",
    };
  },
  methods: {
    getVideoByYear() {
      const searchMovieKey = this.$store.state.searchMovieKey;
      const year = this.$store.state.curSelectYear;
      this.offset++;
      this.$store
        .dispatch("getMovieInfoByTime", {
          time: searchMovieKey.length > 0 ? '' : year,
          offset: this.offset,
          limit: 20,
          searchMovieKey,
        })
        .then((res) => {
          res.data.rows.forEach((ele) => {
            this.$set(ele, "open", false);
            this.videoInfo.push(ele);
          });
          this.videoInfo.push(...res.data.rows);
          this.changeShowLoadVideoState(false);
        });
    },
    changeShowLoadVideoState(state) {
      this.showLoadVideo = state;
    },
    setInfoToVideo() {
      this.videoInfo.forEach((ele) => {
        this.$set(ele, "open", false);
      });
    },
  },
  watch: {
    "$store.state.movieInfoByYear": function () {
      this.containerDOM.scrollTo(0, 0);
      this.videoInfo = this.$store.state.movieInfoByYear.rows;
      this.offset = 1;
      this.setInfoToVideo();
    },
    "$store.state.isPreviewVideo": function () {
      this.isPreviewVideo = this.$store.state.isPreviewVideo;
    },
  },
  mounted() {
    this.containerDOM = document.getElementsByClassName("allvideoby-year")[0];
  },
};
</script>

<style lang="scss" scoped>
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

}
</style>
