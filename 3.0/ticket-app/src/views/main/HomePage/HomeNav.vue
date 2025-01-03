<template>
    <div class="index-left-block">
        <h2 class="h2">全部演出</h2>
        <div v-for="(product, index) in showList" :key="index">
            <h3 class="h3">{{ product.title }}</h3>
            <ul>
                <li v-for="(item, index) in product.list" :key="index" class="list-item" @click="handleClick(item)">
                    <div class="name">
                        {{ item.name }}
                    </div>
                    <div class="separator"></div>
                    <div v-if="item.hot" class="hot-tag-container">
                        <span class="hot-tag">HOT</span>
                    </div>
                </li>
            </ul>
        </div>
    </div>
</template>

<script>
export default {
    data() {
        return {
            showList: [
                {
                    title: "演唱会",
                    list: [
                        { id: 1, name: "李宇春2024巡演", url: "/concert/logo", hot: true },
                        { id: 2, name: "五月天2024年巡演", url: "/concert/logo", hot: false },
                        { id: 3, name: "周杰伦世界巡演", url: "/concert/logo", hot: true },
                    ]
                },
                {
                    title: "话剧歌剧",
                    list: [
                        { id: 1, name: "剧场版《哈利·波特与魔法石》", url: "/concert/golife", hot: false },
                        { id: 2, name: "百老汇经典剧《歌剧魅影》", url: "/concert/golife", hot: true },
                        { id: 3, name: "经典话剧《霸王别姬》", url: "/concert/golife", hot: true },
                    ]
                },
                {
                    title: "音乐会",
                    list: [
                        { id: 1, name: "拉赫玛尼诺夫钢琴协奏曲", url: "/concert/open", hot: false },
                        { id: 2, name: "维也纳爱乐2024音乐会", url: "/concert/open", hot: true },
                        { id: 3, name: "莫扎特与贝多芬的经典", url: "/concert/open", hot: false },
                    ]
                },
                {
                    title: "展览休闲",
                    list: [
                        { id: 1, name: "莫奈与印象派的辉煌", url: "/concert/heigh", hot: true },
                        { id: 2, name: "梵高:星夜与阳光", url: "/concert/heigh", hot: false },
                        { id: 3, name: "未来科技艺术展", url: "/concert/heigh", hot: true },
                    ]
                },
                {
                    title: "舞蹈芭蕾",
                    list: [
                        { id: 1, name: "芭蕾舞剧《天鹅湖》", url: "", hot: false },
                        { id: 2, name: "现代舞《寻找光明》", url: "", hot: true },
                        { id: 3, name: "北京芭蕾舞团《胡桃夹子》", url: "", hot: true },
                    ]
                },
            ]
        }
    },
    methods: {
    handleClick(item) {
      if (item.url.startsWith('http')) {
        window.location.href = item.url;  // External URL跳转
      } else {
        this.$router.push(item.url);  // 内部跳转
      }
    }
  }
}
</script>

<style scoped lang="less">
.index-left-block {
    margin: 20px;
    background: #fff;
    border-radius: 8px;
    box-shadow: 0 0 15px rgba(0, 0, 0, 0.1);
    padding: 15px;
}

.index-left-block .h2 {
    background: #4f73c0;
    color: #fff;
    padding: 12px 20px;
    border-radius: 6px;
    margin-bottom: 20px;
    font-size: 18px;
    font-weight: bold;
}

.index-left-block .h3 {
    font-weight: bold;
    color: #333;
    font-size: 16px;
    margin: 10px 0;
}

.index-left-block ul {
    padding-left: 15px;
    margin-top: 10px;
}

.index-left-block .list-item {
    padding: 10px;
    border-bottom: 1px solid #ddd;
    display: flex;
    justify-content: space-between;
    align-items: center;
    transition: background-color 0.3s ease;
}

.index-left-block .list-item:hover {
    background-color: #f5f5f5;
}

.index-left-block li a {
    color: #333;
    text-decoration: none;
    font-size: 14px;
}

.index-left-block .name {
    flex-grow: 1;
}

.index-left-block .separator {
    border-left: 1px solid #ddd;
    height: 20px;
    margin: 0 10px;
}

.index-left-block .hot-tag-container {
    display: flex;
    justify-content: flex-end;
    align-items: center;
}

.index-left-block .hot-tag {
    background-color: red;
    color: white;
    padding: 2px 6px;
    border-radius: 4px;
    font-size: 12px;
    font-weight: bold;
}

.index-left-block li:last-child {
    border-bottom: none;
}
</style>
