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
        <el-row class="discuss-detail-reply-info">
          <el-col :span="2" style="margin-left: 0.5%"
            ><span class="discuss-detail-reply-info1">{{
              item.author
            }}</span></el-col
          >
          <el-col :span="19"
            ><span>{{ utils.formatDate(item.updated_at) }}</span></el-col
          >
        </el-row>
        <div class="discuss-detail-reply-rereply-content" v-if="item.reply">
          <span
            class="discuss-detail-rereply-author"
            style="margin-left: 0.5%"
            >{{ item.reply_author + "说：" }}</span
          >
          <span>{{ extractContent(item.reply) }}</span>
        </div>
        <div class="discuss-detail-reply-content" v-html="item.content"></div>
        <div class="discuss-detail-reply-rereply">
          <span
            :style="{
              backgroundColor: item.mouseover ? '#fff' : null,
              fontSize: '0.8rem',
            }"
            @mousemove="hoverRereply($event, item)"
            @mouseleave="leaveRereply($event, item)"
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
        replyView.author + "说："
      }}</span>
      <i
        class="el-icon-close"
        :style="{
          cursor: 'pointer',
          position: 'absolute',
          right: '1%',
          backgroundColor: isHoverCloseReply ? '#929292' : '#fff',
          color: isHoverCloseReply ? '#fff' : '#000',
        }"
        @mousemove="hoverCloseReply"
        @mouseleave="leaveCloseReply"
        @click="delReply"
      ></i>
      <span style="display: block; word-break: break-word">{{
        replyView.content
      }}</span>
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
      isHoverCloseReply: false,
      updateReplyParam: {
        rid: 0,
        reply: "",
        reReplyAuthor: "",
        reReplyEmail: "",
        content: "",
        author: "",
      },
    };
  },
  methods: {
    hoverRereply(e, item) {
      if (e.currentTarget.textContent === "回应") {
        item.mouseover = true;
      }
    },
    leaveRereply(e, item) {
      if (e.currentTarget.textContent === "回应") {
        item.mouseover = false;
      }
    },
    hoverCloseReply() {
      this.isHoverCloseReply = true;
    },
    leaveCloseReply() {
      this.isHoverCloseReply = false;
    },
    delReply() {
      this.showReplyView = false;
      this.isHoverCloseReply = false;
    },
    // click reply
    clickRereply(item) {
      this.replyInfo = item;
      this.showReplyView = true;
      window.scrollTo({
        top: document.body.scrollHeight,
        left: 0,
      });
      this.replyView.author = item.author;
      this.replyView.content = this.extractContent(item.content);
    },
    extractContent(val) {
      return val.replace(/\<.*?\>/g, "");
    },
    changePage(val) {
      this.getRepParam.offset = val;
      sessionStorage.setItem("discussRepOffset", val);
      window.scrollTo(0, 0);
      this.getReply();
    },
    editorHtml(val) {
      this.replyContent = val;
    },
    // update discuss relpy
    updateDiscuss() {
      this.author =
        this.$store.state.userInfo.author ||
        JSON.parse(sessionStorage.getItem("userInfo")).author;
      this.email =
        this.$store.state.userInfo.email ||
        JSON.parse(sessionStorage.getItem("userInfo")).email;

      const reqParam = {
        reReplyAuthor: this.replyInfo ? this.replyInfo.author : null,
        reReplyEmail: this.replyInfo ? this.replyInfo.email : null,
        rid: this.getRepParam.rid,
        content: this.replyContent,
        reply: this.replyInfo ? this.replyInfo.content : null,
        author: this.author,
        email: this.email,
      };

      if (!this.checkUserinfo()) return;
      this.$store.dispatch("createDiscussReply", reqParam).then((res) => {
        if (res.success) {
          this.showReplyView = false;
          this.saveUserinfo();
          this.getReply();
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
          author: this.author,
          email: this.email,
        })
      );
    },
    getReply() {
      this.loading = true;
      this.$store.dispatch("getDiscussReply", this.getRepParam).then((res) => {
        this.reply = res.data.rows;
        this.totalReply = res.data.count;
        this.reply.forEach((ele, index) => {
          this.$set(ele, "mouseover", false);
        });
        this.loading = false;
      });
    },
    getData() {
      this.getRepParam.offset =
        parseInt(sessionStorage.getItem("discussRepOffset")) || 1;
      this.getRepParam.rid =
        this.$store.state.selectedDiscuss.id ||
        sessionStorage.getItem("discussid");
      sessionStorage.setItem("discussid", this.getRepParam.rid);
      this.discuss =
        Object.keys(this.$store.state.selectedDiscuss).length === 0
          ? JSON.parse(sessionStorage.getItem("curdiscuss"))
          : this.$store.state.selectedDiscuss;
      this.getReply();
    },
    clearEditor() {
      const element = document.getElementsByClassName("ql-editor");
      element[0].innerHTML = "";
    },
  },
  created() {
    window.scrollTo(0, 0);
    this.getData();
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
      font-size: 0.8rem;
      font-weight: 400;
      opacity: 0.7;

      .discuss-detail-time {
        margin-left: 2%;
      }
    }

    .discuss-detail-content {
      margin-top: 7%;
      font-size: 0.9rem;
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
      font-size: 0.9rem;
      font-weight: 400;
      opacity: 0.7;
      display: flex;
      align-items: center;

      .discuss-detail-reply-info1 {
        line-height: 1.7rem;
        margin-right: 4%;
        opacity: 1;
      }
    }
  }
  .discuss-detail-reply-rereply-content {
    font-size: 0.9rem;
    overflow: hidden;
    text-overflow: ellipsis;
    display: -webkit-box;
    -webkit-line-clamp: 4;
    -webkit-box-orient: vertical;
    margin-top: 1%;
    border-radius: 5px;
    background-color: #fff;
    line-height: 1.5rem;
  }
  .discuss-detail-reply-content {
    font-size: 0.9rem;
    word-break: break-word;
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
    font-size: 1rem;
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
    font-size: 0.9rem;
    position: relative;
    border-radius: 5px;

    span {
      margin-left: 0.5%;
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