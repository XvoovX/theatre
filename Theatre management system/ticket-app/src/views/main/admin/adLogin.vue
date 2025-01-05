<template>
    <div class="login">
      <el-card class="box-card">
        <template #header>
          <div class="card-header">
            <span>欢迎管理员</span>
          </div>
        </template>
        <el-form :model="loginForm" status-icon :rules="rules" ref="loginForm">
          <el-form-item label="管理员账号" label-width="120px" prop="username">
            <el-input type="text" v-model="loginForm.Account"></el-input>
          </el-form-item>
          <el-form-item label="密码" label-width="120px" prop="password">
            <el-input type="password" v-model="loginForm.Password"></el-input>
          </el-form-item>
          <el-form-item>
            <el-button type="primary" @click="submitForm('loginForm')">提交</el-button>
          </el-form-item>
        </el-form>
      </el-card>
    </div>
</template>
  
  <script>
  import api from "@/api";
  import { mapMutations } from "vuex";
  import { h } from 'vue';
  
  export default {
    data() {
      var validatePassword = (rule, value, callback) => {
        if (value === '') {
          callback(new Error("请输入密码"));
        } else {
          callback();
        }
      };
  
      return {
        loginForm: {
          Account: "",
          Password: "",
        },
        rules: {
          Password: [
            {
              validator: validatePassword,
              trigger: 'blur',
            },
          ],
        },
      };
    },
    methods: {
      ...mapMutations("adminlogin", ["setAdmin"]),
      submitForm(formName) {
        this.$refs[formName].validate((valid) => {
          if (valid) {
            api.adminLogin(this.loginForm).then((res) => {
              if (res.data.code == 2000) {
                this.$message({
                  message: "登录成功",
                  type: "success",
                });
                this.setAdmin(res.data);
                localStorage.setItem("adminticket", JSON.stringify(res.data));
                this.$store.dispatch('adminlogin');
                this.$router.push("/admin");
              } else {
                this.$message({
                  message: res.data.message,
                  type: "error",
                });
              }
            });
          } else {
            this.$message({
              message: "请检查输入",
              type: "error",
            });
            return false;
          }
        });
      },
    },
  };
</script>
  
<style scoped>
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
    padding: 20px; /* 缩小上下间距 */
    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    border-radius: 10px;
  }
  
  .card-header {
    text-align: center;
    font-size: 28px; /* 增大字体大小 */
    color: #333;
    font-weight: bold;
    margin-bottom: 15px; /* 适当调整下方间距 */
  }
  
  .el-form-item {
    margin-bottom: 15px; /* 增加表单项间距 */
  }
  
  .el-form-item label {
    font-family: '华文彩云', sans-serif; /* 设置标签字体为华文彩云 */
    font-size: 16px;
    color: #333; /* 标签文字颜色 */
  }
  
  .el-input {
    width: 100%;
  }
  
  .el-button {
    width: 100%;
    height: 40px;
    font-size: 16px;
    background-color: #409EFF;
    border-color: #409EFF;
    transition: all 0.3s ease;
  }
  
  .el-button:hover {
    background-color: #66b1ff;
    border-color: #66b1ff;
  }
</style>
  