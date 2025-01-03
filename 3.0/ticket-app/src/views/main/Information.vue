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
        <el-button @click="dialogVisible = false" class="cancel-btn">取消</el-button>
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
/* Overall container layout */
.container {
  width: 70%; /* Adjust container width for better alignment */
  margin: 40px auto;
  padding: 40px; /* Increase padding for a larger container */
  background-color: #fff;
  border-radius: 12px; /* Slightly round corners */
  box-shadow: 0 4px 16px rgba(0, 0, 0, 0.1); /* Stronger shadow for depth */
}

/* Title style */
.title {
  text-align: center;
  font-size: 36px; /* Adjusted for better visibility */
  color: #333;
  margin-bottom: 40px;
  font-family: "华文彩云", sans-serif; /* Set font to 华文彩云 */
}

/* Form section styling */
.form {
  display: flex;
  flex-direction: column;
  gap: 25px; /* Increased gap between form items for better spacing */
}

/* Form item label styling */
.el-form-item {
  display: flex;
  align-items: center;
  justify-content: space-between;
  margin-bottom: 20px; /* Add some spacing between each form item */
}

/* Extended input field style */
.input-field {
  width: 100%; /* Make the input field extend the full width of the container */
  padding: 14px;
  border-radius: 8px;
  border: 1px solid #ccc;
  font-size: 16px;
  box-sizing: border-box;
}

/* Input focus effect */
.input-field:focus {
  border-color: #409EFF;
  box-shadow: 0 0 5px rgba(64, 158, 255, 0.5);
}

/* Button style */
.el-button {
  height: 50px;
  font-size: 16px;
  width: 160px; /* Increased button width */
  border-radius: 8px;
  padding: 0 25px; /* More padding for a better look */
}

/* Button group layout */
.button-group {
  display: flex;
  justify-content: space-between;
  margin-top: 30px; /* Increased space between form and buttons */
}

/* Cancel button style */
.cancel-btn {
  background-color: #f5f5f5;
  border: 1px solid #ccc;
  color: #333;
}

/* Submit button style */
.submit-btn {
  background-color: #409EFF;
  border-color: #409EFF;
  color: white;
}

/* Responsive design for smaller screens */
@media (max-width: 768px) {
  .container {
    width: 90%;
  }
  .input-field {
    width: 100%;
  }
  .button-group {
    flex-direction: column;
    align-items: center;
  }
  .cancel-btn, .submit-btn {
    width: 100%;
    margin: 10px 0;
  }
}
</style>
