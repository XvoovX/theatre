<template>
    <div class="open">
      <div class="sales-board">
        <div class="sales-board-intro">
          <h2>五月天演唱会</h2>
          <p class="concert-description">
            2025年5月1日，五月天将在上海虹口足球场举办一场震撼的演唱会，为歌迷们带来一场狂欢的音乐盛宴。全新的演唱会舞台，配合精心编排的曲目，绝对是一次不容错过的音乐体验！
          </p>
          <p class="concert-description">
            五月天是华语乐坛最具影响力的摇滚乐队之一，他们的音乐跨越世代，触动了无数粉丝的心灵。这一次，他们将带着全新专辑《人生无限公司》来袭，让我们共同期待这场音乐的狂欢。
          </p>
        </div>
  
        <div class="sales-board-form">
          <div class="sales-board-line">
            <div class="sales-board-line-left">购买数量：</div>
            <div class="sales-board-line-right">
              <input v-model="postData.Quantity" class="input-field narrow-input" />
            </div>
          </div>
          <div class="sales-board-line">
            <div class="sales-board-line-left">票档：</div>
            <div class="sales-board-line-right">
              <Type :selecterData="selecterData" />
            </div>
          </div>
          <div class="sales-board-line">
            <div class="sales-board-line-left">场次</div>
            <div class="sales-board-line-right">
              <Timer :timerData="timerData" />
            </div>
          </div>
  
          <el-button @click="handleConfirmTicket" class="buy-btn">购票</el-button>
          <TicketDialog :visible="ticketDialogVisible" :timerData="timerData" :selecterData="selecterData" :username="username" @confirm="handleConfirmTicket" @close="handleCloseTicket"></TicketDialog>
          <ConfirmTicketDialog v-if="showConfirmDialog" :paymentInfo="paymentInfo" :qrCode="qrCode" :orderID="orderID" @paymentComplete="handlePaymentComplete" @cancel="handleCancel" />
        </div>
  
        <div class="divider"></div>

        <div class="sales-board-des">
          <h3>购票须知</h3>
          <ul>
            <li>每笔订单最多购买4张、每个账号最多购买4张。</li>
            <li>支持多种票品验票后入场，如证件电子票。</li>
            <li>本项目支持有条件退款，若需要收取退票手续费，将以用户实际支付票款为基准收取。</li>
            <li>儿童一律凭票入场</li>
          </ul>
          <h3>观演须知</h3>
          <ul>
            <li>演出时长约90分钟</li>
            <li>请于演出前约120分钟入场</li>
            <li>请携带有效证件入场</li>
            <li>请勿携带食品、酒水等物品入场</li>
          </ul>
        </div>
      </div>
    </div>
</template>
  
<script>
  import Counter from '@/components/HomePage/counter.vue'
  import Type from '@/components/HomePage/type.vue'
  import Timer from '@/components/HomePage/timer.vue'
  import TicketDialog from './TicketDialog.vue'
  import axios from 'axios';
  import ConfirmTicketDialog from './ConfirmTicketDialog.vue';
  
  export default {
    name: 'Open',
    data() {
      return {
        selecterData: [
          { value: "内场前排", id: 1 },
          { value: "内场后排", id: 2 },
          { value: "看台前排", id: 3 },
          { value: "看台后排", id: 4 },
          { value: "山顶位置", id: 5 }
        ],
        timerData: [
          { value: '2021-06-01', id: 1 },
          { value: '2021-07-01', id: 2 },
          { value: '2021-08-01', id: 3 },
        ],
        ticketDialogVisible: false,
        username: this.$store.state.login.user.data.username,
        selectedTimer: null,
        selectedQuantity: 1,
        selectedType: null,
        postData: {
          UserID: JSON.parse(localStorage.getItem('ticket')).data.userID,
          TicketID: String(32434),
          PurchaseTime: new Date().toLocaleString(),
          OrderStatus: "已支付",
          Quantity: 1,
        },
        showConfirmDialog: false,
        paymentInfo: '',
        qrCode: '',
        orderID: ''
      };
    },
    components: {
      Counter,
      Type,
      Timer,
      TicketDialog,
      ConfirmTicketDialog,
    },
    methods: {
      showTicketDialog() {
        this.username = this.$store.state.login.user.data.username;
        this.selectedTimer = null;
        this.selectedQuantity = 1;
        this.selectedType = null;
        this.ticketDialogVisible = true;
      },
      handleConfirmTicket(ticketInfo) {
        const currentDate = new Date();
        const year = currentDate.getFullYear();
        const month = (currentDate.getMonth() + 1).toString().padStart(2, '0');
        const day = currentDate.getDate().toString().padStart(2, '0');
        const formattedDate = `${year}-${month}-${day}`;
  
        const formData = new URLSearchParams();
        formData.append('UserID', this.postData.UserID);
        formData.append('TicketID', this.postData.TicketID);
        formData.append('PurchaseTime', this.postData.PurchaseTime);
        formData.append('OrderStatus', '未支付');
        formData.append('Quantity', this.postData.Quantity);
  
        fetch('http://127.0.0.1:5000/orders', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/x-www-form-urlencoded',
          },
          body: formData,
        })
          .then(response => response.json())
          .then(data => {
            this.showConfirmDialog = true;
            this.paymentInfo = data.data.OrderStatus;
            this.qrCode = "https://img2.baidu.com/it/u=1443929167,3597244248&fm=253&fmt=auto&app=138&f=GIF?w=150&h=150";
            this.orderID = data.data.OrderID;
          })
          .catch(error => {
            console.error('请求失败', error);
          });
  
        this.ticketDialogVisible = false;
      },
      handleCloseTicket() {
        this.ticketDialogVisible = false;
      },
      handlePaymentComplete() {
        this.showConfirmDialog = false;
      },
      handleCancel() {
        this.showConfirmDialog = false;
      },
    }
  };
</script>
  
<style scoped>
.open {
  text-align: left;
  font-family: 'Arial', sans-serif;
  color: #333;
}
.sales-board {
  background: #fff;
  border-radius: 10px;
  padding: 20px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
  margin-bottom: 20px;
}
.sales-board-intro h2 {
  font-size: 28px;
  font-weight: bold;
  color: #333;
  margin-bottom: 15px;
  text-align: center;
}
.sales-board-intro .concert-description {
  font-size: 16px;
  line-height: 1.6;
  color: #666;
  margin-bottom: 15px;
  text-align: justify;
}
.sales-board-form {
  display: flex;
  flex-direction: column;
  margin-bottom: 20px;
}
.sales-board-line {
  display: flex;
  justify-content: flex-start;
  align-items: center;
  margin-bottom: 20px;
}
.sales-board-line-left {
  font-size: 16px;
  font-weight: bold;
  color: #333;
  width: 100px;
}
.sales-board-line-right {
  display: flex;
  justify-content: flex-start;
  flex: 1;
}
.input-field {
  width: 100%;
  padding: 8px; /* Adjusted for narrower height */
  font-size: 14px;
  border: 1px solid #ccc;
  border-radius: 5px;
}
.narrow-input {
  padding-top: 4px;
  padding-bottom: 4px;
}
.buy-btn {
  font-size: 14px;
  padding: 12px 25px;
  display: flex;
  justify-content: center;
  align-items: center;
  margin-top: 20px;
  width: 100%;
}
.divider {
  height: 0; /* 高度设置为0，由边框定义虚线 */
  border-top: 1px dashed #ccc; /* 设置虚线颜色和样式 */
  width: 100%; /* 分割线宽度 */
  margin: 70px auto 0px; /* 设置上边距60px，下边距40px */
}
.sales-board-des h3 {
  font-size: 18px;
  font-weight: bold;
  color: #333;
  margin-top: 30px;
  margin-bottom: 10px;
}
.sales-board-des ul {
  list-style: none;
  padding-left: 0;
}
.sales-board-des li {
  font-size: 14px;
  color: #666;
  line-height: 1.6;
}
.sales-board-des li:before {
  content: '•';
  margin-right: 10px;
  color: #4fc08d;
}
</style>
  