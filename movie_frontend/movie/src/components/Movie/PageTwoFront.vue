<template>
  <div class="allvideos-category">
    <div class="allvideos-category-content">
      <div
        class="allvideos-category-content-title"
        :class="{ covertextfadein: coverTextFadein }"
      >
        <span id="cover-title">{{ coverData.title }}</span>
        <span id="cover-rd">{{ coverData.release_date }}</span>
      </div>
    </div>
    <el-image
      class="allvideos-category-cover"
      :class="{ fadein: isFadein }"
      :src="coverData.cover"
      referrerpolicy="no-referrer"
      fit="contain"
    ></el-image>
  </div>
</template>

<script>
export default {
  name: "AllVideosCategory",
  props: {},
  data() {
    return {
      coverData: {},
      isFadein: true,
      coverTitle: "",
      coverTextFadein: true,
    };
  },
  methods: {
    getCover() {
      this.$store.dispatch("getRandomMovie").then((res) => {
        if (res.success) {
          this.isFadein = true;
          this.coverTextFadein = true;
          this.coverData = res.data[0];
        }
      });
    },
    // random change cover
    changeCover() {
      if (this.randomCoverTimer) clearInterval(this.getCover);
      this.randomCoverTimer = setInterval(() => {
        this.isFadein = false;
        this.coverTextFadein = false;
        this.getCover();
      }, 30000 + 5 * Math.random());
    },
    getCoverTitle() {
      if (Object.keys(this.coverData).length === 0) return;
      if (this.coverData.release_date.length === 0) {
        return this.coverData.title;
      } else {
        return (
          this.coverData.title +
          "\xa0\xa0\xa0\xa0\xa0\xa0\xa0" +
          this.coverData.release_date
        );
      }
    },
  },
  beforeMount() {
    this.getCover();
    this.changeCover();
  },
  destroyed() {
    if (this.randomCoverTimer) clearInterval(this.randomCoverTimer);
    if (this.getCoverTimer) clearInterval(this.getCoverTimer);
  },
};
</script>

<style lang='scss'>
@keyframes fadein {
  0% {
    opacity: 0;
  }
  100% {
    opacity: 0.5;
  }
}

@keyframes textfadein {
  0% {
    opacity: 0;
  }
  100% {
    opacity: 1;
  }
}

.allvideos-category {
  height: 100%;
  position: relative;
  display: flex;
  align-items: center;
  flex-direction: column;

  .allvideos-category-content {
    width: 80%;
    height: 10%;
    display: flex;
    position: absolute;
    margin-left: 10%;

    .allvideos-category-content-title {
      width: 100%;
      span {
        display: block;
        color: #fff;
        text-align: center;
        font-size: 1rem;
        text-overflow: ellipsis;
        white-space: nowrap;
        overflow: hidden;
        width: 100%;
      }

      #cover-rd {
        margin-top: 1%;
      }
    }
  }

  .covertextfadein {
    animation: textfadein 6s ease;
  }
  .allvideos-category-cover {
    height: 88%;
    width: 80%;
    opacity: 0.5;
    position: absolute;
    top: 10%;
    margin-left: 10%;
  }
  .fadein {
    animation: fadein 6s ease;
  }
}
</style>
