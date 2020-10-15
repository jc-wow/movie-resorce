<template>
  <div class="login">
    <div class="login-user login-section">
      <label>昵称:</label>
      <el-input v-model="author"></el-input>
      <span>（必填哦）</span>
    </div>
    <div class="login-email login-section">
      <label>邮箱:</label>
      <el-input v-model="email"></el-input>
      <span>（必填哦）</span>
    </div>
    <!-- <div class="login-confirm login-section">
      <label>是否记住？</label>
      <el-checkbox v-model="checked" size="medium"></el-checkbox>
    </div> -->
  </div>
</template>

<script>
export default {
  name: "login",
  data() {
    return {
      email: "",
      author: "",
      // checked: false,
    };
  },
  watch: {
    email: function () {
      this.$store.commit("getUserInfo", { email: this.email });
    },
    author: function () {
      this.$store.commit("getUserInfo", { author: this.author });
    },
  },
};
</script>

<style lang="scss" scoped>
.login {
  height: 100%;
  width: 100%;

  span {
    color: #1414e5;
    font-size: 0.8rem;
  }

  .login-section {
    margin-top: 3%;

    label {
      margin-right: 2%;
      font-size: 0.8rem;
    }

    .el-input {
      width: 40%;
			font-size: 1rem;
    }
  }

  .login-user {
    padding-top: 3%;
    margin-top: 0;
  }
}
</style>