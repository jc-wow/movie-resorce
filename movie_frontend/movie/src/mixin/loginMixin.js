export const loginMixin = {
  methods: {
    checkUserinfo() {
      if (this.email.length === 0 || this.author.length === 0) {
        this.$message.error("昵称和邮箱不能为空哦");
        return false;
      }
      if (!this.utils.testEmailValid(this.email)) {
        this.$message.error("邮箱不合法哦");
        return false;
      }
      return true;
    },
  },
};
