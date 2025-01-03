<template>
  <HeaderNav></HeaderNav>
  <div class="detail-wrap">
    <div class="detail-left">
      <div class="product-board">
        <img src="../../assets/logo.png" alt="Logo" class="logo">
        <ul>
          <router-link tag="li" active-class="active" v-for="(item, index) in showNav" :key="index" :to="'/concert/' + item.id">
            {{ item.title }}
          </router-link>
        </ul>
      </div>
    </div>
    <div class="detail-right">
      <router-view></router-view>
    </div>
  </div>
</template>

<script>
import HeaderNav from '@/components/HeaderNav.vue';
export default {
  components: {
    HeaderNav,
  },
  data() {
    return {
      showNav: [
        { title: "音乐会", id: "open" },
        { title: "演唱会", id: "logo" },
        { title: "歌剧话剧", id: "golife" },
        { title: "曲苑杂坛", id: "heigh" },
      ]
    };
  },
  methods: {},
};

</script>

<style>
/* 主容器 */
.detail-wrap {
  display: flex;
  justify-content: space-between;
  padding: 20px;
  max-width: 1200px;
  margin: 0 auto;
  background-color: #f9f9f9;
  min-height: 100vh;
  width: 1200px; /* 合并 */
  overflow: hidden; /* 合并 */
  padding-top: 20px; /* 合并 */
}

/* 左侧导航栏 */
.detail-left {
  width: 150px; /* 调整左侧区域的宽度 */
  background-color: #fff;
  box-shadow: 2px 2px 15px rgba(0, 0, 0, 0.1);
  padding: 20px;
  border-radius: 8px;
  display: flex;
  flex-direction: column;
  align-items: center;
  float: left; /* 合并 */
  text-align: center; /* 合并 */
}

/* 图片样式 */
.product-board .logo {
  width: 130px; /* 调整图片大小 */
  height: auto;
  margin-bottom: 20px;
  object-fit: contain;
  align-self: center;
  display: block;
}

/* 导航列表样式 */
.product-board ul {
  list-style: none;
  padding: 0;
  margin: 0;
  width: 100%;
  margin-top: 20px; /* 合并 */
}

.product-board li {
  width: 100%;
  margin-bottom: 15px;
}

.product-board a {
  display: block;
  padding: 12px 20px;
  text-align: left;
  font-size: 16px;
  color: #333;
  text-decoration: none;
  border-radius: 4px;
  transition: background-color 0.3s, color 0.3s;
  cursor: pointer; /* 合并 */
}

.product-board a:hover, .product-board a.active {
  background-color: #4fc0be;
  color: white;
}

/* 右侧内容区域 */
.detail-right {
  flex: 1;
  margin-left: 20px;
  padding: 20px;
  background-color: #fff;
  border-radius: 8px;
  box-shadow: 2px 2px 10px rgba(0, 0, 0, 0.1);
  float: left; /* 合并 */
  width: 980px; /* 合并 */
}

.sales-board {
  background: #fff;
}

/* 销售面板样式 */
.sales-board-intro h2 {
  font-size: 20px;
  padding: 20px;
}

.sales-board-intro p {
  background: #f7fcff;
  padding: 10px 20px;
  color: #999;
  line-height: 1.8;
}

.sales-board-form {
  padding: 10px 20px;
  font-size: 14px;
}

.sales-board-line {
  clear: both;
  padding-bottom: 20px;
}

.sales-board-line-left {
  display: inline-block;
  margin-right: 10px;
}

.sales-board-line-right {
  display: inline-block;
  width: 75%;
}

.sales-board-des {
  border-top: 20px solid #fff;
  background: #fff;
  padding: 15px 20px;
}

.sales-board-des p {
  line-height: 1.6;
}

.sales-board-des h2 {
  font-size: 20px;
  padding-bottom: 15px;
}

.sales-board-des h3 {
  font-size: 20px;
  font-weight: bold;
  padding: 20px 0 10px 0;
}

.sales-board-des li {
  padding: 5px 0;
}

.sales-board-table {
  width: 100%;
  margin-top: 20px;
}

.sales-board-table th {
  background: #4fc08d;
  color: #fff;
}

.sales-board-table td {
  border: 1px solid #f0f2f5;
  padding: 15px;
}

/* 响应式设计：适配手机端 */
@media (max-width: 768px) {
  .detail-wrap {
    flex-direction: column;
    align-items: center;
  }

  .detail-left {
    width: 100%;
    margin-bottom: 20px;
  }

  .detail-right {
    width: 100%;
    margin-left: 0;
  }

  .product-board .logo {
    width: 120px;
    margin-bottom: 15px;
  }
}
</style>
