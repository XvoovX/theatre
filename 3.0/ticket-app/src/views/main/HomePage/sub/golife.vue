<template>
    <div class="open">
        <div class="sales-board">
            <div class="sales-board-intro">
                <h2>罗密欧与朱丽叶</h2>
                <p class="concert-description">
                    《罗密欧与朱丽叶》是莎士比亚的经典爱情悲剧。故事讲述了两个相爱的年轻人罗密欧与朱丽叶，他们来自敌对的家庭，因而被命运逼得走向一场无法避免的悲剧。尽管两人的爱情真挚，但社会的偏见和仇恨使得他们无法共度一生，最终在一场误会中相继离世。这个故事探讨了爱情、仇恨、命运与牺牲。
                </p>
                <p class="concert-description">
                    《罗密欧与朱丽叶》不仅是一个悲伤的爱情故事，更是对人性深刻的探讨。它让我们思考爱与恨、命运与选择的关系。2025年，让我们一同走进剧场，感受这段永恒的爱情故事，见证两颗心在纷乱世界中的交汇与碰撞。无论你是莎士比亚的忠实粉丝，还是初次接触这段经典，我们都邀请你来共同体验这场震撼心灵的舞台盛宴。
                </p>
            </div>
            <div class="sales-board-form">
                <div class="sales-board-line-left">购买数量：</div>
                <div class="sales-board-line-right">
                    <input v-model="postData.Quantity" />
                </div>
            </div>
            <div class="sales-board-form">
                <div class="sales-board-line-left">票档：</div>
                <div class="sales-board-line-right">
                    <Type :selecterData="selecterData"></Type>
                </div>
            </div>
            <div class="sales-board-form">
                <div class="sales-board-line-left">场次</div>
                <div class="sales-board-line-right">
                    <Timer :timerData="timerData"></Timer>

                </div>
            </div>
            <el-button @click="showTicketDialog">购票</el-button>
            <TicketDialog :visible="ticketDialogVisible" :timerData="timerData" :selecterData="selecterData"
                :username="username" @confirm="handleConfirmTicket" @close="handleCloseTicket">
            </TicketDialog>
            <ConfirmTicketDialog v-if="showConfirmDialog" :paymentInfo="paymentInfo" :qrCode="qrCode" :orderID="orderID"
                @paymentComplete="handlePaymentComplete" @cancel="handleCancel" />
        </div>

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
                {
                    value: "内场前排",
                    id: 1
                },
                {
                    value: "内场后排",
                    id: 2
                },
                {
                    value: "看台前排",
                    id: 3
                },
                {
                    value: "看台后排",
                    id: 4
                },
                {
                    value: "山顶位置",
                    id: 5
                }
            ],
            timerData: [
                {
                    value: '2022-06-01',
                    id: 1
                },
                {
                    value: '2022-07-01',
                    id: 2
                },
                {
                    value: '2023-08-01',
                    id: 3
                },
            ],
            ticketDialogVisible: false,
            username: this.$store.state.login.user.data.username,
            selectedTimer: null,
            selectedQuantity: 1,
            selectedType: null,
            postData: {
                UserID: this.$store.state.login.user.data.UserID,
                TicketID: String(32434),
                // timerData: ticketInfo.timerData,
                PurchaseTime: new Date().toLocaleString(),
                OrderStatus: "已支付",
                Quantity: String(1),
            },
            showConfirmDialog: false,
            paymentInfo: '', // 从后端获取的支付信息
            qrCode: '',
            orderID: ''// 从后端获取的二维码链接
        }
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
            // 设置购票信息
            this.username = this.$store.state.login.user.data.username
            console.log(this.username)// 设置默认值
            this.selectedTimer = null; // 设置默认值
            this.selectedQuantity = 1; // 设置默认值
            this.selectedType = null; // 设置默认值

            // 弹出购票对话框
            this.ticketDialogVisible = true;
        },

        handleConfirmTicket(ticketInfo) {
            // 处理确认购票逻辑，你可以在这里调用后端接口提交购票信息
            console.log("确认购票", ticketInfo);
            // 获取当前时间
            const currentDate = new Date();

            // 提取年、月、日
            const year = currentDate.getFullYear();
            const month = (currentDate.getMonth() + 1).toString().padStart(2, '0'); // 月份是从0开始的，因此要加1
            const day = currentDate.getDate().toString().padStart(2, '0');

            // 构建年月日字符串
            const formattedDate = `${year}-${month}-${day}`;

            console.log(formattedDate);

            // 创建一个空的 URLSearchParams 对象
            const formData = new URLSearchParams();

            // 添加键值对到对象中
            formData.append('UserID', this.postData.UserID);
            formData.append('TicketID', this.postData.TicketID);
            formData.append('PurchaseTime', this.postData.PurchaseTime);
            formData.append('OrderStatus', '未支付');
            formData.append('Quantity', this.postData.Quantity);
            // ... 添加其他键值对

            // 使用 fetch 发送 POST 请求
            fetch('http://127.0.0.1:5000/orders', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/x-www-form-urlencoded',
                },
                body: formData,
            })
                .then(response => response.json())
                .then(data => {
                    console.log('请求成功', data);
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
            // 处理取消购票逻辑
            console.log("取消购票");

            // 关闭购票对话框
            this.ticketDialogVisible = false;
        },



        handlePaymentComplete() {
            // 支付完成后的处理，可以关闭对话框或执行其他操作
            this.showConfirmDialog = false;
            // 在这里可以进行支付完成后的其他逻辑处理
        },
        handleCancel() {
            // 取消按钮的处理，可以关闭对话框或执行其他操作
            this.showConfirmDialog = false;
        },
    }
}
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
  align-items: flex-start;
  margin-bottom: 20px;
}

.sales-board-line {
  display: flex;
  justify-content: space-between;
  width: 100%;
  margin-bottom: 10px;
}

.sales-board-line .label {
  font-size: 16px;
  font-weight: bold;
  color: #333;
}

.sales-board-line .value {
  font-size: 16px;
  color: #666;
}

.counter-box .el-input__inner {
  text-align: center;  /* 让输入框中的数字居中 */
  font-size: 18px;  /* 增大数字的字体 */
}

.buy-btn {
  font-size: 14px;
  padding: 12px 25px;
  display: flex;
  justify-content: center;
  align-items: center;
  margin: 20px auto;
  min-width: 130px;
  height: 40px;
}

/* 购票须知样式 */
.sales-board-des h3 {
    font-size: 18px;
    font-weight: bold;
    color: #333;
    margin-top: 30px;
    margin-bottom: 10px;
}

/* 列表样式 */
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
    content: '•';  /* 自定义列表符号 */
    margin-right: 10px;
    color: #4fc08d;  /* 列表符号颜色 */
}
</style>