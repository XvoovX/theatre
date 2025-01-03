<template>
    <div class="open">
        <div class="sales-board">
            <div class="sales-board-intro">
                <h2>黑神话·悟空</h2>
                <p class="concert-description">
                    《黑神话·悟空》是基于热门游戏《黑神话·悟空》改编的戏剧表演。故事聚焦于孙悟空这一经典角色的崛起与命运之争。作为一名被压制的神话英雄，悟空从一只天生强大的猴子开始，因抗天而被囚禁五百年，最终展开了他的复仇与救赎之路。
                </p>
                <p class="concert-description">
                    在这场舞台剧中，观众将经历孙悟空从五行山下的沉寂到战斗场上的威猛，见证他如何突破命运的枷锁，在险恶的天地间与众多神仙、妖怪、甚至自己的内心世界进行抗争。这场戏剧表演融合了传统的中国神话故事与现代戏剧创意，利用壮丽的舞美、华丽的武打、以及丰富的情感表现，为观众呈现出一个全新的《西游记》故事。
                </p>
            </div>
            <div class="sales-board-form">
                <div class="sales-board-line-left">购买数量：</div>
                <div class="sales-board-line-right">
                    <Counter></Counter>
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
                    value: '2021-06-01',
                    id: 1
                },
                {
                    value: '2021-07-01',
                    id: 2
                },
                {
                    value: '2021-08-01',
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
    text-align: center;
    font-size: 18px;
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