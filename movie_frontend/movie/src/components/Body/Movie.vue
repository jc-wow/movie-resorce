<template>
  <div class="movie-info">
    <img class="movieInfo-menuLogo" src="../../assets/menu.svg" @click="showMenu" />
    <div class="movie-container">
      <Drip :data="dripPicInfo"></Drip>
    </div>
  </div>
</template>

<script>
import { mapState } from "vuex";
import Drip from "../common/Drip";

export default {
  name: "Movie",
  components: {
    Drip
  },
  data() {
    return {
      movieInfo: [],
      dripPicInfo: [],
			imageContainerHeight: 0,
			menu: false,
      requestParam: {
        page: 1,
        itemsPerPage: 10
      }
    };
  },
  methods: {
    getMoveInfo() {
      this.$store.dispatch("getMovieInfo", this.requestParam).then(() => {
        this.getHighestScoreMovie;
      });
    },
    getDripPicInfo() {
      this.movieInfo.forEach(ele => {
        this.dripPicInfo.push({
          url: ele.cover,
          info: {
            title: ele.title,
            director: ele.director,
            genre: ele.genre,
            produceArea: ele.produceArea
          }
        });
      });
    },
    getPositionOfScroll() {
      let windowHeight = $(window).height();
      let heightToBottomOfPage = 0.2 * windowHeight;
      let preDocHeight = 0;
      $(window).scroll(() => {
        let docHeight = $(document).height();
        let scrollTopHeight = $(window).scrollTop();
        if (
          scrollTopHeight + windowHeight > docHeight - heightToBottomOfPage &&
          docHeight > preDocHeight
        ) {
          this.getMoveInfo();
          preDocHeight = docHeight;
          this.requestParam.page += 1;
        }
      });
    },
    showMenu() {
      this.menu = true;
    }
  },
  computed: {
    ...mapState({
      getHighestScoreMovie(status) {
        this.movieInfo = status.movieInfo;
        this.getDripPicInfo();
      }
    })
  },
  created() {
    this.getMoveInfo();
  },
  mounted() {
    this.getPositionOfScroll();
  }
};
</script>

<style lang="scss" scoped>
.movie-info {
  background-color: #000;

  .movieInfo-menuLogo {
    position: absolute;
    height: 4%;
    margin: 2% 0 0 2%;
    z-index: 999;
  }

  .movie-container {
    height: 100%;
    width: 60%;
		margin-left: 10%;
  }
}
</style>
