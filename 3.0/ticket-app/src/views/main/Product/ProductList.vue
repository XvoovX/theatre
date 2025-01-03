<template>
    <el-table :data="tableData" style="width: 100%; margin-bottom: 20px;" border>
      <el-table-column label="订单ID" width="200" prop="OrderID" align="center"></el-table-column>
      <el-table-column label="订单时间" width="200" prop="PurchaseTime" align="center"></el-table-column>
      <el-table-column label="数量" width="200" prop="Quantity" align="center"></el-table-column>
      <el-table-column label="票ID" width="200" prop="TicketID" align="center"></el-table-column>
      <el-table-column label="账号ID" width="200" prop="UserID" align="center"></el-table-column>
      <el-table-column label="支付状态" width="200" prop="OrderStatus" align="center"></el-table-column>
      <el-table-column label="退票" align="center">
        <template #default="scope">
          <el-button size="small" type="danger" @click="handleRefund(scope.$index, scope.row)">退票</el-button>
        </template>
      </el-table-column>
    </el-table>
  </template>
  
  <script>
  import eventBus from "@/utils/eventBus.js";
  import { onMounted, onBeforeUnmount } from 'vue';
  import { mapState, mapGetters } from 'vuex';
  import { ElMessage, ElMessageBox } from 'element-plus'
  
  export default {
    data() {
      return {
        tableData: [],
        Form: {
          UserID: "666666",
          Page: 1,
        },
        currentPage: 1,
        totalCount: 0,
        totalPage: 1,
        refundOrder: {
          UserID: "",
          AdminID: "",
          RefundTime: "",
          RefundReason: "没时间",
          TicketStatus: "未处理",
          OrderID: "",
        }
      };
    },
    computed: {
      ...mapGetters('login', ['getUserID']),
      ...mapState('login', ['user']),
    },
    mounted() {
      this.Form.UserID = this.getUserID;
      const changePageHandler = this.changePageHandler;
      eventBus.on("changePage", changePageHandler);
      this.$api.selectOrder(this.Form).then(res => {
        if (res.data.code == 2000) {
          this.tableData = res.data.data;
          this.totalCount = res.data.totalCount;
          this.totalPage = res.data.totalPage;
        }
      });
      onBeforeUnmount(() => {
        eventBus.off("changePage", changePageHandler);
      });
    },
    methods: {
      changePageHandler(val) {
        this.currentPage = val;
        this.fetchData();
      },
      fetchData() {
        this.Form.Page = this.currentPage;
        this.$api.selectOrder(this.Form).then(res => {
          if (res.data.code == 2000) {
            this.tableData = res.data.data;
          }
        });
      },
      handleRefund(index, row) {
        this.refundOrder.OrderID = String(row.OrderID);
        this.refundOrder.UserID = JSON.parse(localStorage.getItem('ticket')).data.userID;
        const currentDate = new Date();
        const formattedDate = `${currentDate.getFullYear()}-${(currentDate.getMonth() + 1).toString().padStart(2, '0')}-${currentDate.getDate().toString().padStart(2, '0')}`;
        this.refundOrder.RefundTime = formattedDate;
        ElMessageBox.confirm('确定要退票吗?', 'Warning', {
          confirmButtonText: 'OK',
          cancelButtonText: 'Cancel',
          type: 'warning',
        })
        .then(() => {
          this.$api.refundOrder(this.refundOrder).then(res => {
            if (res.data.code == 2000) {
              this.$message({ message: "提交成功", type: "success" });
              this.fetchData();
            } else {
              this.$message({ message: "提交失败", type: "error" });
            }
          })
        })
        .catch(() => {
          ElMessage({ type: 'info', message: '取消退票' });
        });
      },
    },
  }
  </script>
  
  <style scoped>
  .el-table {
    margin-bottom: 20px;
  }
  
  .el-table__header-wrapper {
    background-color: #f9f9f9;
  }
  
  .el-table th {
    font-weight: bold;
    background-color: #f4f4f4;
    color: #333;
    text-align: center; /* 表头居中 */
  }
  
  .el-table td {
    font-size: 14px;
    text-align: center; /* 内容居中 */
  }
  
  .el-button--danger {
    margin-left: 5px;
  }
  </style>
  