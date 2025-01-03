<template>
  <HeaderNav></HeaderNav>
  <div class="container">
    <h1 class="title">个人信息</h1>
    <div class="form">
      <el-form label-width="90px" :model="editorForm" ref="addForm">
        <el-form-item label="真实姓名：">
          <el-input v-model="editorForm.RealName" class="input-field"></el-input>
        </el-form-item>
        <el-form-item label="性别：">
          <el-input v-model="editorForm.Gender" class="input-field"></el-input>
        </el-form-item>
        <el-form-item label="身份证号：">
          <el-input v-model="editorForm.IDcard" class="input-field"></el-input>
        </el-form-item>
        <el-form-item label="住址：">
          <el-input v-model="editorForm.Address" class="input-field"></el-input>
        </el-form-item>
        <el-form-item label="电话号码：">
          <el-input v-model="editorForm.Account" class="input-field"></el-input>
        </el-form-item>
        <el-form-item label="电子邮箱：">
          <el-input v-model="editorForm.Email" class="input-field"></el-input>
        </el-form-item>
      </el-form>
      <div class="button-group">
        <el-button type="primary" @click="editorSubmit" class="submit-btn">确定</el-button>
      </div>
    </div>
  </div>
</template>


<script>
import { ref, onBeforeUnmount } from 'vue';
import { ElMessageBox } from 'element-plus'
import eventBus from "@/utils/eventBus.js";
const dialogVisible = ref(false)
import { mapState, mapGetters } from 'vuex';
const qs = require('qs');
import HeaderNav from '@/components/HeaderNav.vue'

export default {
  components: {
    HeaderNav
  },
  computed: {
    ...mapGetters('login', ['getUserID']),
    ...mapState('login', ['user']),
  },
  mounted() {

    console.log(this.editorForm)
    
    var Info = JSON.parse(localStorage.getItem('ticket'))
    console.log(Info.data.userID);
    var id = Info.data.userID;
    this.$api.getUser({UserID:String(Info.data.userID)}).then((res) => {
        if (res.data.code == 2000) {
          this.editorForm.RealName = res.data.data.RealName;
          this.editorForm.Gender = res.data.data.Gender;
          this.editorForm.IDcard = res.data.data.IDCard;
          this.editorForm.Address = res.data.data.Address;
          this.editorForm.Account = res.data.data.Account;
          this.editorForm.Email = res.data.data.Email;
          this.editorForm.UserID = id;
          this.$message({
            message: "请求成功",
            type: "success"
          });
        } else {
          this.$message({
            message: "请求失败",
            type: "error"
          });
        }
      });

  },
  methods: {
    editorSubmit() {
      // this.editorForm.AdminID = this.getAdminID
      const formData = qs.stringify(this.editorForm);
      console.log(formData)
      this.$api.editorUser(formData, {
        headers: {
          'Content-Type': 'application/x-www-form-urlencoded'
        }
      }).then((res) => {
        console.log(res.data);
        if (res.data.code == 2000) {
          this.$message({
            message: "编辑成功",
            type: "success"
          });
        } else {
          this.$message({
            message: "编辑失败",
            type: "error"
          });
        }
      });
    }
  },
  data() {
    return {
      editorForm: {
        RealName: "",
        Gender: "",
        IDcard: "",
        Address: "",
        Account: "",
        Email: "",
        UserID: "",
      }
    }
  }
}

</script>

<style scoped>
/* 整体容器布局 */
.container {
  width: 70%; /* 调整容器宽度，使其对齐更好 */
  margin: 40px auto;
  padding: 40px; /* 增加内边距，容器更大 */
  background-color: #fff;
  border-radius: 12px; /* 略微圆角 */
  box-shadow: 0 4px 16px rgba(0, 0, 0, 0.1); /* 增强阴影效果，增加深度 */
}

/* 标题样式 */
.title {
  text-align: center;
  font-size: 36px; /* 调整字体大小，增强可见性 */
  color: #333;
  margin-bottom: 40px;
  font-family: "华文彩云", sans-serif; /* 设置字体为华文彩云 */
}

/* 表单部分样式 */
.form {
  display: flex;
  flex-direction: column;
  gap: 25px; /* 增加表单项之间的间隙 */
}

/* 表单项标签样式 */
.el-form-item {
  display: flex;
  align-items: center;
  justify-content: space-between;
  margin-bottom: 20px; /* 增加每个表单项之间的间距 */
}

/* 输入框样式 */
.input-field {
  width: 100%; /* 输入框扩展至容器的全部宽度 */
  padding: 14px;
  border-radius: 8px;
  border: 1px solid #ccc;
  font-size: 16px;
  box-sizing: border-box; /* 确保内边距和宽度一致 */
}

/* 输入框聚焦时的样式 */
.input-field:focus {
  border-color: #409EFF;
  box-shadow: 0 0 5px rgba(64, 158, 255, 0.5); /* 增加聚焦时的边框和阴影效果 */
}

/* 按钮样式 */
.el-button {
  height: 50px;
  font-size: 16px;
  width: 160px; /* 增加按钮宽度 */
  border-radius: 8px;
  padding: 0 25px; /* 增加内边距，使按钮更美观 */
}

/* 按钮组的布局 */
.button-group {
  display: flex;
  justify-content: center; /* 按钮居中对齐 */
}

/* 提交按钮样式 */
.submit-btn {
  background-color: #409EFF;
  border-color: #409EFF;
  color: white;
  width: 160px; /* 保持固定宽度，确保按钮一致性 */
  font-size: 18px; /* 略微增大按钮文字 */
}

/* 小屏幕的响应式设计 */
@media (max-width: 768px) {
  .container {
    width: 90%; /* 在小屏幕下，容器宽度扩大到 90% */
  }
  .input-field {
    width: 100%; /* 输入框宽度自适应 */
  }
  .button-group {
    flex-direction: column;
    align-items: center; /* 垂直排列按钮并居中 */
  }
  .submit-btn {
    width: 100%; /* 小屏幕下按钮占满全宽 */
    margin: 10px 0; /* 增加按钮之间的间距 */
  }
}
</style>
