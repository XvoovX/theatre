<template>
    <div class="index-board-list">
        <div class="index-board-item" v-for="(item, index) in buyData" :key="index"
            :class="['index-board-' + item.flag, { 'line-last': index % 2 !== 0 }]">
            <div class="index-board-item-inner">
                <h2>{{ item.title }}</h2>
                <p>{{ item.desc }}</p>
                <div class="index-board-button">
                    <router-link :to="'/concert/'+item.flag" class="button">查看详情</router-link>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
export default {
    name: 'HomeShowList',
    data() {
        return {
            buyData: [
                {
                    title: "音乐会",
                    desc: "音乐会描述",
                    flag: "open",
                },
                {
                    title: "演唱会",
                    desc: "演唱会描述",
                    flag: "logo",
                },
                {
                    title: "歌剧话剧",
                    desc: "歌剧话剧描述",
                    flag: "golife",
                },
                {
                    title: "曲苑杂坛",
                    desc: "曲苑杂坛描述",
                    flag: "heigh",
                },
            ]
        }
    }
}
</script>

<style scoped>
.index-board-list {
    overflow: hidden;
    margin-top: 15px;
}

.index-board-item {
    float: left;
    width: 400px;
    padding: 20px;
    background: #fff;
    box-shadow: 0 0 1px #ddd;
    padding: 20px;
    margin-right: 20px;
    margin-bottom: 20px;
}

.index-board-item-inner {
    min-height: 125px;
    padding-left: 120px;
}

.index-board-open .index-board-item-inner {
    background: url(../../../assets/concert2.jpg) no-repeat;
    background-size: 100px 140px;
}

.index-board-logo .index-board-item-inner {
    background: url(https://th.bing.com/th/id/OIP.shB-dNdxipkJOEAXL8BWFAHaKD?rs=1&pid=ImgDetMain) no-repeat;
    background-size: 100px 140px;
}

.index-board-golife .index-board-item-inner {
    background: url(https://th.bing.com/th/id/R.9bf61a9ed4d4a47ba91ec043a7ff5797?rik=bBT5w7NzNAGqXw&riu=http%3a%2f%2f5b0988e595225.cdn.sohucs.com%2fimages%2f20180810%2fe1c8651c86e34965a37435e2dca41c68.jpeg&ehk=F3OBiUaT9eD4D5EWIgUlFaMgm1xp0LUzN9pUECbznQU%3d&risl=&pid=ImgRaw&r=0) no-repeat;
    background-size: 100px 140px;
}

.index-board-heigh .index-board-item-inner {
    background: url(../../../assets/concert4.jpg) no-repeat;
    background-size: 100px 140px;
}

.index-board-item h2 {
    font-size: 18px;
    font-weight: bold;
    margin-bottom: 15px;
    color: #000;
}

.line-last {
    margin-right: 0;
}

.index-board-button {
    margin-top: 20px;
}

.lastest-news {
    min-height: 350px;
}

.new-item {
    display: inline-block;
    width: 230px;
    overflow: hidden;
    text-overflow: ellipsis;
    white-space: nowrap;
}

.button {
    background: #4f73c0;
    color: #fff;
    display: inline-block;
    padding: 10px 20px;
    cursor: pointer;
}
</style>


