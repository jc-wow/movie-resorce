<template>
  <div class="alldiscuss">
    <div class="alldiscuss-tipboard">
      <!-- <h1>{{ tipBoard }}</h1> -->
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
            <el-col :span="12">想法</el-col>
            <el-col class="col-2" :span="5">作者</el-col>
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
          <el-row
            type="flex"
            style="height: 100%; cursor: pointer"
            align="middle"
          >
            <el-col :span="12">{{ discuss.title }}</el-col>
            <el-col class="col-2" :span="5">{{ discuss.author }}</el-col>
            <el-col class="col-3" :span="3" style="font-size: 0.8rem">{{
              discuss.reply === 0 ? "" : discuss.reply
            }}</el-col>
            <el-col
              class="col-4"
              :span="4"
              style="font-size: 0.8rem; color: #5d5e5f"
            >
              <span>{{ utils.formatDate(discuss.updated_at) }}</span>
            </el-col>
          </el-row>
        </li>
        <el-divider style="height: 0.5px"></el-divider>
      </ul>
    </div>
    <div class="alldiscuss-page">
      <el-pagination
        layout="prev, pager, next"
        :total="totalDiscuss"
        :background="pageBg"
        :page-size="20"
        :current-page.sync="reqParam.page"
        @current-change="changePage"
        @prev-click="changePage"
        @next-click="changePage"
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
      // tipBoard: "Only in their dreams can men be truly free",
      tipBorard: "",
    };
  },
  methods: {
    addDiscuss() {
      this.$store.commit("getSelectedDiscuss", "add");
    },
    getDiscuss() {
      const curPage = sessionStorage.getItem("alldiscussOffset");
      if (curPage) this.reqParam.page = parseInt(curPage);
      ("getAllDiscuss", this.reqParam).then((res) => {
        this.discussList = res.data.rows;
        this.totalDiscuss = res.data.count;
      });
    },
    showDetailDiscuss(val) {
      this.$store.commit("getSelectedDiscuss", val);
      sessionStorage.setItem("curdiscuss", JSON.stringify(val));
    },
    changePage(val) {
      this.reqParam.page = val;
      sessionStorage.setItem("alldiscussOffset", val);
      this.getDiscuss();
    },
  },
  created() {
    this.getDiscuss();
  },
};
</script>

<style lang="scss" scoped>
.alldiscuss {
  min-height: 92vh;
  padding-top: 8vh;
  background-image: linear-gradient(
    to bottom,
    rgb(185, 185, 185),
    rgb(200, 200, 200) 30%,
    rgb(220, 220, 220)
  );
  .alldiscuss-tipboard {
    height: 30vh;
    display: flex;
    flex-direction: column;
    justify-content: center;
    text-align: center;
  }

  .alldiscuss-container {
    font-size: 1rem;
    min-height: 52vh;

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
        font-size: 0.8rem;
        color: #44464f;
      }
    }

    .el-divider {
      background-color: #a0a2a7;
      margin: 1.3vh 0;
      height: 0.5px;
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
