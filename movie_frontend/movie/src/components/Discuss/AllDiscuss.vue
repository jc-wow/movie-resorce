<template>
  <div class="alldiscuss">
    <div class="alldiscuss-tipboard">
      <h1>{{ tipBoard }}</h1>
    </div>
    <div class="alldiscuss-container">
      <div class="alldiscuss-container-nav"></div>
      <ul>
        <li v-for="(discuss, index) in discussList" :key="'dis' + index">
          <el-divider></el-divider>
          <span>{{ discuss }}</span>
        </li>
        <el-divider></el-divider>
      </ul>
    </div>
    <div class="alldiscuss-page">
      <el-pagination layout="prev, pager, next" :total="50"></el-pagination>
    </div>
  </div>
</template>

<script>
export default {
  name: "alldiscuss",
  data() {
    return {
      discussList: [
        "这是测试评论",
        "这是测试评论",
        "这是测试评论",
        "这是测试评论",
        "这是测试评论",
        "这是测试评论",
        "这是测试评论",
        "这是测试评论",
        "这是测试评论",
        "这是测试评论",
        "这是测试评论",
        "这是测试评论",
        "这是测试评论",
        "这是测试评论",
        "这是测试评论",
        "这是测试评论",
        "这是测试评论",
        "这是测试评论",
        "这是测试评论",
      ],
      tipBoard: "Only in their dreams can men be truly free",
    };
  },
};
</script>

<style lang="scss" scoped>
* {
  margin: 0;
  padding: 0;
}
.alldiscuss {
  background-color: #e4e4e1;
  background-image: radial-gradient(
      at top center,
      rgba(255, 255, 255, 0.03) 0%,
      rgba(0, 0, 0, 0.03) 100%
    ),
    linear-gradient(
      to top,
      rgba(255, 255, 255, 0.1) 0%,
      rgba(143, 152, 157, 0.6) 100%
    );
  background-blend-mode: normal, multiply;

  .alldiscuss-tipboard {
    height: 30vh;
    display: flex;
    flex-direction: column;
    justify-content: center;
    text-align: center;
  }

  .alldiscuss-container {
    font-size: 0.9rem;

    .alldiscuss-container-nav {
      height: 5vh;
      width: 75%;
      margin: auto;
    }

    ul {
      width: 75%;
      margin: auto;
      list-style-type: none;
    }
    .el-divider {
      background-color: #a0a2a7;
    }

    .el-divider--horizontal {
      margin: 1.3vh 0;
    }
  }

  .alldiscuss-page {
    display: flex;
    justify-content: center;
    margin-top: 1%;
    height: 8vh;
  }
}
</style>