<template>
  <div class="alldiscuss">
    <div class="alldiscuss-tipboard">
      <h1>{{ tipBoard }}</h1>
    </div>
    <div class="alldiscuss-container">
      <div class="alldiscuss-container-nav">
        <el-row>
          <el-col :span="2" :offset="22" type="flex">
            <el-button
              icon="el-icon-plus"
              size="small"
              plain
              @click="addDiscuss"
              >发言</el-button
            >
          </el-col>
        </el-row>
      </div>
      <ul>
        <li class="alldiscuss-title">
          <el-row type="flex" align="bottom" style="height: 100%">
            <el-col :span="13">想法</el-col>
            <el-col class="col-2" :span="4">作者</el-col>
            <el-col class="col-3" :span="3">回应</el-col>
            <el-col class="col-4" :span="4">
              <span>回应时间</span>
            </el-col>
          </el-row>
        </li>
        <li
          class="discuss-item"
          v-for="(discuss, index) in discussList"
          :key="'dis' + index"
          @click="showDetailDiscuss(discuss)"
        >
          <el-divider></el-divider>
          <el-row type="flex" style="height: 100%; cursor: pointer">
            <el-col :span="13">{{ discuss.title }}</el-col>
            <el-col class="col-2" :span="4">{{ discuss.author }}</el-col>
            <el-col class="col-3" :span="3"></el-col>
            <el-col
              class="col-4"
              :span="4"
              style="font-size: 0.8rem; color: #5d5e5f"
            >
              <span>{{ utils.formatDate(discuss.updated_at) }}</span>
            </el-col>
          </el-row>
        </li>
        <el-divider></el-divider>
      </ul>
    </div>
    <div class="alldiscuss-page">
      <el-pagination
        layout="prev, pager, next"
        :total="totalDiscuss"
        :background="pageBg"
        :page-size="20"
        hide-on-single-page
      ></el-pagination>
    </div>
  </div>
</template>

<script>
export default {
  name: "alldiscuss",
  data() {
    return {
      pageBg: true,
      discussList: [],
      reqParam: {
        page: 1,
        limit: 20,
      },
      totalDiscuss: 0,
      tipBoard: "Only in their dreams can men be truly free",
    };
  },
  methods: {
    addDiscuss() {
      this.$store.commit("getSelectedDiscuss", "add");
    },
    getDiscuss() {
      return this.$store.dispatch("getAllDiscuss", this.reqParam);
    },
    showDetailDiscuss(val) {
      this.$store.commit("getSelectedDiscuss", val);
      sessionStorage.removeItem("discussDetail");
    },
  },
  mounted() {
    this.getDiscuss().then((res) => {
      this.discussList = res.data.rows;
      this.totalDiscuss = res.data.count;
    });
  },
};
</script>

<style lang="scss" scoped>
.alldiscuss {
  background-image: linear-gradient(to left, #bdbbbe 0%, #9d9ea3 100%),
    radial-gradient(
      88% 271%,
      rgba(255, 255, 255, 0.25) 0%,
      rgba(254, 254, 254, 0.25) 1%,
      rgba(0, 0, 0, 0.25) 100%
    ),
    radial-gradient(
      50% 100%,
      rgba(255, 255, 255, 0.3) 0%,
      rgba(0, 0, 0, 0.3) 100%
    );
  background-blend-mode: normal, lighten, soft-light;

  .alldiscuss-tipboard {
    height: 30vh;
    display: flex;
    flex-direction: column;
    justify-content: center;
    text-align: center;
  }

  .alldiscuss-container {
    font-size: 0.9rem;
    height: 100vh;

    .alldiscuss-container-nav {
      height: 5vh;
      width: 70%;
      margin: auto;

      .el-col {
        text-align: right;
        cursor: pointer;

        .el-button {
          width: 70px;
        }
      }
    }

    ul {
      padding: 0;
      width: 70%;
      margin: auto;
      list-style-type: none;

      .col-3 {
        text-align: center;
      }

      .col-4 {
        text-align: right;
      }

      .alldiscuss-title {
        height: 4vh;
        font-size: 0.85rem;
        color: #44464f;
      }
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