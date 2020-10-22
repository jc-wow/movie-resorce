export const loginMixin = {
  methods: {
    checkUserinfo() {
      if (this.email.length === 0 || this.author.length === 0) {
        this.$message({
          message: "邮箱不合法哦",
          type: "error",
          duration: 1500
        });
        return false;
      }
      if (!this.utils.testEmailValid(this.email)) {
        this.$message({
          message: "邮箱不合法哦",
          type: "error",
          duration: 1500
        });
        return false;
      }
      return true;
    }
  }
};
