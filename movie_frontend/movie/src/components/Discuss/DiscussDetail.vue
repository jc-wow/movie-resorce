<template>
  <div class="discuss-detail">
    <section
      class="discuss-detail-section"
      style="height: 100vh"
      v-show="loading"
    ></section>
    <section class="discuss-detail-section" v-show="!loading">
      <header class="discuss-detail-header">
        <h1>{{ discuss.title }}</h1>
      </header>
      <div class="discuss-detail-info">
        <span>来自：</span>
        <span>{{ discuss.author }}</span>
        <span class="discuss-detail-time">{{
          utils.formatDate(discuss.updated_at)
        }}</span>
      </div>
      <article
        v-html="discuss.content"
        class="discuss-detail-content"
      ></article>
    </section>
    <el-divider></el-divider>
    <div class="discuss-detail-reply">
      <div
        :id="'discuss-detail-reply_' + index"
        v-for="(item, index) in reply"
        :key="'reply_' + index"
      >
        <div class="discuss-detail-reply-info">
          <span class="discuss-detail-reply-info1">{{ item.author }}</span>
          <span>{{ utils.formatDate(item.updated_at) }}</span>
        </div>
        <div class="discuss-detail-reply-content" v-html="item.content"></div>
        <div class="discuss-detail-reply-rereply">
          <span
            :style="{ backgroundColor: item.mouseover ? '#fff' : null }"
            @mousemove="hover($event, item)"
            @mouseleave="leave($event, item)"
            @click="clickRereply(item)"
            >回应</span
          >
        </div>
      </div>
    </div>
    <el-pagination
      layout="prev, pager, next"
      :total="totalReply"
      :background="pageBg"
      :page-size="20"
      hide-on-single-page
      :current-page.sync="getRepParam.offset"
      @current-change="changePage"
      @prev-click="changePage"
      @next-click="changePage"
    ></el-pagination>
    <p class="discuss-detail-edit">发表想法：</p>
    <p class="discuss-detail-viewreply" v-if="showReplyView">
      <span class="discuss-detail-viewreply-author">{{
        replyView.author + "："
      }}</span>
      {{ replyView.content }}
    </p>
    <div class="discuss-detail-newreply">
      <Editor :height="editorHeight" @editorHtml="editorHtml"></Editor>
      <el-button
        plain
        size="small"
        style="float: right; margin-top: 2%"
        @click="updateDiscuss"
        >发表</el-button
      >
    </div>
    <div class="discuss-detail-login">
      <Login></Login>
    </div>
  </div>
</template>

<script>
import Editor from "../common/Editor";
import Login from "../common/Login";
import { loginMixin } from "../../mixin/loginMixin.js";

export default {
  name: "discussDetail",
  components: {
    Editor,
    Login,
  },
  mixins: [loginMixin],
  data() {
    return {
      discuss: {},
      editorHeight: "30vh",
      totalReply: 0,
      pageBg: true,
      reply: [
        {
          author: "",
          updated_at: "",
          content: "",
        },
      ],
      getRepParam: {
        rid: 0,
        offset: 1,
        limit: 20,
      },
      loading: false,
      replyView: {
        author: "",
        content: "",
      },
      showReplyView: false,
    };
  },
  methods: {
    hover(e, item) {
      if (e.currentTarget.textContent === "回应") {
        item.mouseover = true;
      }
    },
    leave(e, item) {
      if (e.currentTarget.textContent === "回应") {
        item.mouseover = false;
      }
    },
    // click reply
    clickRereply(item) {
      this.showReplyView = true;
      window.scrollTo({
        top: document.body.scrollHeight,
        left: 0,
        behavior: "smooth",
      });
      this.replyView.author = item.author;
      this.replyView.content = item.content.replace(/\<.*?\>/g, "");
    },
    changePage(val) {
      this.getRepParam.offset = val;
      sessionStorage.setItem("discussRepOffset", val);
      this.getReply();
    },
    // save data to sessionstorage in case refresh page
    saveData() {
      if (this.discuss && Object.keys(this.discuss) !== 0) {
        sessionStorage.setItem("discussDetail", JSON.stringify(this.discuss));
      }
      if (this.reply && this.reply.length !== 0) {
        sessionStorage.setItem(
          "discussReplyDetail",
          JSON.stringify(this.reply)
        );
        sessionStorage.setItem("totalReply", this.totalReply);
      }
    },
    editorHtml(val) {
      this.replyContent = val;
    },
    // update discuss relpy
    updateDiscuss() {
      if (!this.discuss) {
        this.discuss =
          Object.keys(this.$store.state.selectedDiscuss).length !== 0
            ? this.$store.state.selectedDiscuss
            : JSON.parse(sessionStorage.getItem("discussDetail"));
      }

      this.author = this.$store.state.userInfo.author;
      this.email = this.$store.state.userInfo.email;
      this.reqParam = {
        content: this.replyContent,
        rid: this.discuss.id,
        author: this.author,
        email: this.email,
      };

      if (!this.checkUserinfo()) return;
      this.$store.dispatch("createDiscussReply", this.reqParam).then((res) => {
        if (res.success) {
          this.$message({
            message: "恭喜，发表成功啦",
            type: "success",
            duration: 1500,
          });
          this.saveUserinfo();
          this.getReplyAfterCreate();
        }
      });
      this.clearEditor();
    },
    saveUserinfo() {
      if (sessionStorage.getItem("userInfo")) {
        sessionStorage.removeItem("userInfo");
      }
      sessionStorage.setItem(
        "userInfo",
        JSON.stringify({
          author: this.reqParam.author,
          email: this.reqParam.email,
        })
      );
    },
    // get reply after created a new one
    getReplyAfterCreate() {
      sessionStorage.removeItem("discussReplyDetail");
      sessionStorage.removeItem("totalReply");
      this.getReply();
    },
    getReply() {
      this.loading = true;
      this.getRepParam.rid = this.discuss.id;
      this.$store.dispatch("getDiscussReply", this.getRepParam).then((res) => {
        this.reply = res.data.rows;
        this.totalReply = res.data.count;
        this.reply.forEach((ele, index) => {
          this.$set(ele, "mouseover", false);
        });
        this.saveData();
        this.loading = false;
      });
    },
    getData() {
      const discuss = JSON.parse(sessionStorage.getItem("discussDetail"));
      const reply = JSON.parse(sessionStorage.getItem("discussReplyDetail"));
      const totalReply = JSON.parse(sessionStorage.getItem("totalReply"));
      const offset = parseInt(sessionStorage.getItem("discussRepOffset"));
      if (discuss && reply) {
        this.discuss = discuss;
        this.reply = reply;
        this.totalReply = totalReply;
        this.getRepParam.offset = offset;
      } else {
        this.discuss = this.$store.state.selectedDiscuss;
        this.rid = this.discuss.id;
        this.getReply();
      }
    },
    clearEditor() {
      const element = document.getElementsByClassName("ql-editor");
      element[0].innerHTML = "";
    },
    listenLeavePage() {
      window.onbeforeunload = () => {
        return "sure";
      };
    },
  },
  mounted() {
    window.scrollTo(0, 0);
    this.getData();
    this.listenLeavePage();
  },
  destroyed() {
    window.onbeforeunload = null;
  },
};
</script>

<style lang="scss">
.discuss-detail {
  min-height: 92vh;
  padding-top: 8vh;
  display: flex;
  flex-direction: column;
  align-items: center;
  background-image: linear-gradient(
    to bottom,
    rgb(185, 185, 185),
    rgb(200, 200, 200) 30%,
    rgb(220, 220, 220)
  );

  .discuss-detail-section {
    width: 60%;
    padding-top: 1%;

    .discuss-detail-header {
      text-align: center;
    }

    .discuss-detail-info {
      margin-top: 4%;
      font-size: 0.9rem;
      font-weight: 400;
      opacity: 0.7;

      .discuss-detail-time {
        margin-left: 2%;
      }
    }

    .discuss-detail-content {
      margin-top: 7%;
    }
  }
  .el-divider {
    width: 60%;
    height: 0.5px;
    background-color: #a0a2a7;
  }

  .discuss-detail-reply {
    width: 60%;
    font-size: 1rem;

    .discuss-detail-reply-info {
      background-color: #b3b3b3;
      font-size: 0.7rem;
      font-weight: 400;
      opacity: 0.7;

      .discuss-detail-reply-info1 {
        line-height: 1.7rem;
        margin-right: 4%;
        opacity: 1;
      }
    }
  }

  .discuss-detail-reply-rereply {
    cursor: pointer;
    display: flex;
    justify-content: flex-end;
    padding-bottom: 1%;
    width: 99%;
    font-size: 0.9rem;
    opacity: 0.6;
  }

  .discuss-detail-edit {
    width: 60%;
    font-size: 1.1rem;
    margin-top: 5%;
  }

  .discuss-detail-viewreply {
    width: 60%;
    overflow: hidden;
    text-overflow: ellipsis;
    display: -webkit-box;
    -webkit-line-clamp: 3;
    -webkit-box-orient: vertical;
    background-color: #fff;
    border-radius: 8px;

    .discuss-detail-viewreply-author {
      background-color: #409eff;
      color: #fff;
    }
  }

  .discuss-detail-newreply {
    width: 60%;
    min-height: 30vh;
  }

  .discuss-detail-login {
    height: 20vh;
    width: 60%;
  }
}
</style>