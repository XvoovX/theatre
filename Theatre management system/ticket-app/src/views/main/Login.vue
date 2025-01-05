<template>
  <div class="login">
    <el-card class="box-card">
      <template #header>
        <div class="card-header">
          <span>欢迎</span>
        </div>
      </template>
      <el-tabs v-model="currentIndex" class="demo-tabs" @tab-click="handleTabsClick" stretch>
        <el-tab-pane label="登录" name="login">
          <el-form :model="loginForm" status-icon :rules="rules" ref="loginForm">
            <el-form-item label="用户名" label-width="80px" prop="username">
              <el-input type="text" v-model="loginForm.username" placeholder="请输入用户名" />
            </el-form-item>
            <el-form-item label="密码" label-width="80px" prop="password">
              <el-input type="password" v-model="loginForm.password" placeholder="请输入密码" />
            </el-form-item>
            <el-form-item>
              <el-button type="primary" @click="submitForm('loginForm')">提交</el-button>
            </el-form-item>
          </el-form>
        </el-tab-pane>
        <el-tab-pane label="注册" name="register">
          <el-form :model="registerForm" status-icon :rules="rules" ref="registerForm">
            <el-form-item label="用户名" label-width="80px" prop="username">
              <el-input type="text" v-model="registerForm.username" placeholder="请输入用户名" />
            </el-form-item>
            <el-form-item label="邮箱" label-width="80px" prop="email">
              <el-input type="text" v-model="registerForm.email" placeholder="请输入邮箱" />
            </el-form-item>
            <el-form-item label="密码" label-width="80px" prop="password">
              <el-input type="password" v-model="registerForm.password" placeholder="请输入密码" />
            </el-form-item>
            <el-form-item label="确认密码" label-width="80px" prop="configurePassword">
              <el-input type="password" v-model="registerForm.configurePassword" placeholder="请再次输入密码" />
            </el-form-item>
            <el-form-item>
              <el-button type="primary" @click="submitForm('registerForm')">注册</el-button>
            </el-form-item>
          </el-form>
        </el-tab-pane>
      </el-tabs>
    </el-card>
  </div>
</template>

<script>
import api from "@/api";
import { mapMutations } from "vuex";
import { h } from 'vue';
import store from "../../store";

export default {
  data() {
    // 验证规则
    var validateUserName = (rule, value, callback) => {
      if (value === '') {
        callback(new Error("请输入用户名"));
      } else if (value.length < 4) {
        callback(new Error("用户名最少为4位"));
      } else {
        callback();
      }
    };

    var validateEmail = (rule, value, callback) => {
      const mailReg = /^([a-zA-Z0-9_-])+@([a-zA-Z0-9_-])+(.[a-zA-Z0-9_-])+/;
      if (!value) {
        return callback(new Error("请输入邮箱"));
      }
      setTimeout(() => {
        if (mailReg.test(value)) {
          callback();
        } else {
          callback(new Error("请输入正确的邮箱格式"));
        }
      }, 100);
    };

    var validatePassword = (rule, value, callback) => {
      if (value === '') {
        callback(new Error("请输入密码"));
      } else {
        callback();
      }
    };

    var validateConfigurePassword = (rule, value, callback) => {
      if (value === '') {
        callback(new Error("请再次输入密码"));
      } else if (value !== this.registerForm.password) {
        callback(new Error("两次密码输入不一致"));
      } else {
        callback();
      }
    };

    return {
      currentIndex: "login",
      loginForm: { username: "", password: "" },
      registerForm: { username: "", password: "", configurePassword: "", email: "" },
      activeTab: "login",
      rules: {
        username: [
          {
            validator: validateUserName,
            trigger: 'blur',
          },
        ],
        password: [
          {
            validator: validatePassword,
            trigger: 'blur',
          },
        ],
        configurePassword: [
          {
            validator: validateConfigurePassword,
            trigger: 'blur',
          },
        ],
        email: [
          {
            validator: validateEmail,
            trigger: 'blur',
          },
        ],
      },
    };
  },
  methods: {
    ...mapMutations("login", ["setUser"]),
    submitForm(formName) {
      this.$refs[formName].validate((valid) => {
        if (valid) {
          if (this.activeTab === "login") {
            api.login(this.loginForm).then((res) => {
              console.log(res.data);
              if (res.data.code === "2000") {
                this.$message({
                  message: "登录成功",
                  type: "success",
                });
                this.setUser(res.data);
                localStorage.setItem("ticket", JSON.stringify(res.data));
                this.$store.dispatch('login');
                this.$router.push('/');
              } else {
                const notification = {
                  title: "登录失败",
                  message: h(
                    "i",
                    { style: "color:teal" },
                    "用户名密码错误"
                  ),
                };
                this.$notify(notification);
              }
            });
          }
          if (this.activeTab === "register") {
            console.log(this.registerForm);
            api.register(this.registerForm).then((res) => {
              if (res.data.code === "2000") {
                const notification = {
                  title: "注册成功",
                  message: h(
                    "i",
                    { style: "color:teal" },
                    "请返回首页登录"
                  ),
                };
                this.$notify(notification);
                this.$router.push('/');
              } else {
                const notification = {
                  title: "注册失败",
                  message: h(
                    "i",
                    { style: "color:teal" },
                    "请重新填写信息"
                  ),
                };
                this.$notify(notification);
              }
            });
          }
        } else {
          return;
        }
      });
    },
    handleTabsClick(tab) {
      console.log(tab.props.name);
      this.activeTab = tab.props.name;
    },
  },
};
</script>

<style scoped lang="less">
.login {
  width: 400px;
  margin: 0 auto; /* 取消上方和下方的空白 */
  display: flex;
  justify-content: center; /* 水平居中 */
  align-items: center; /* 垂直居中 */
  height: 100vh; /* 设置高度为视口高度 */
  font-family: '华文彩云', sans-serif; /* 使用华文彩云字体 */
}

.box-card {
  padding: 20px;
  border-radius: 8px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
}

.card-header {
  text-align: center;
  font-size: 28px; /* 增加了标题字体大小 */
  color: #333;
  font-weight: bold;
  margin-bottom: 5px; /* 减少了欢迎文字与表单之间的间距 */
}

.demo-tabs {
  margin-top: 5px; /* 减少了Tab与表单之间的间距 */
}

.el-tabs__header {
  background-color: #f7f7f7;
  border-bottom: 2px solid #ddd;
}

.el-tabs__item {
  font-weight: bold;
}

.el-tabs__item.is-active {
  color: #409EFF;
}

.el-form-item {
  margin-bottom: 10px; /* 减少了表单项之间的间距 */
}

.el-form-item .el-input,
.el-form-item .el-button {
  width: 100%;
}

.el-button {
  height: 40px;
  line-height: 40px;
  background-color: #409EFF;
  border-color: #409EFF;
}

.el-button:hover {
  background-color: #66b1ff;
  border-color: #66b1ff;
}

.el-input {
  border-radius: 5px;
  box-shadow: none;
}

.el-input:focus {
  box-shadow: 0 0 5px rgba(64, 158, 255, 0.5);
}

.el-form-item .el-input__inner {
  padding: 10px;
  font-size: 14px;
}

.el-tabs__header {
  margin-bottom: 15px;
}

.el-button.primary {
  font-size: 16px;
}

.el-button:focus {
  outline: none;
}

.el-tabs__item {
  color: #333;
  font-size: 16px;
}

.el-tabs__item.is-active {
  color: #409EFF;
}
</style>
