<template>
  <div class="confirm-dialog">
    <div class="dialog-content">
      <p class="payment-info">支付信息：{{ paymentInfo }}</p>
      <img :src="qrCode" alt="二维码" class="qr-code" />
    </div>
    <div class="button-group">
      <el-button type="primary" @click="handlePaymentComplete">支付完成</el-button>
      <el-button type="danger" @click="handleCancel">取消</el-button>
    </div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  props: {
    paymentInfo: {
      type: String,
      required: true,
    },
    qrCode: {
      type: String,
      required: true,
    },
    orderID: {
      type: Number,
      required: true,
    },
  },
  methods: {
    handlePaymentComplete() {
      const formData = new URLSearchParams();
      formData.append('OrderID', this.orderID);
      formData.append('OrderStatus', '已支付');

      axios
        .put('http://127.0.0.1:5000/orders', formData)
        .then((response) => {
          console.log('支付完成', response.data);
          this.$emit('paymentComplete');
        })
        .catch((error) => {
          console.error('支付完成失败', error);
        });
    },
    handleCancel() {
      this.$emit('cancel');
    },
  },
};
</script>

<style scoped>
.confirm-dialog {
  display: flex;
  flex-direction: column;
  align-items: center;
  padding: 20px;
  background-color: #fff;
  border-radius: 10px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
  max-width: 400px;
  margin: auto;
  margin-top: 60px; /* 控制支付窗体与上方按钮的间距 */
}

.dialog-content {
  text-align: center;
  margin-bottom: 20px;
}

.payment-info {
  font-size: 16px;
  font-weight: bold;
  color: #333;
  margin-bottom: 10px;
}

.qr-code {
  width: 150px;
  height: 150px;
  border: 1px solid #ccc;
  border-radius: 8px;
}

.button-group {
  display: flex;
  justify-content: space-around;
  width: 100%;
}

.el-button {
  width: 120px;
  font-size: 14px;
}
</style>
