<template>
  <div class="pagination-container">
    <el-pagination 
      layout="prev, pager, next, jumper"
      :total="total"
      @size-change="handleSizechange"
      @current-change="handleCurrentChange"
      v-model="currentPage"
      style="text-align: center;"
    />
  </div>
</template>

<script>
import eventBus from "@/utils/eventBus.js";
import { mapState, mapGetters } from 'vuex';

export default {
  data() {
    return {
      currentPage: 1,
      total: 1,
      count: 0,
      Form: {
        UserID: "666666",
      },
    };
  },
  computed: {
    ...mapGetters('login', ['getUserID']),
    ...mapState('login', ['user']),
  },
  methods: {
    handleSizechange() {
      // 页大小变化逻辑
    },
    handleCurrentChange(val) {
      eventBus.emit('changePage', val);
    },
  },
  mounted() {
    this.Form.UserID = this.getUserID;
    this.$api.selectOrder(this.Form).then(res => {
      if (res.data.code == 2000) {
        this.total = res.data.totalPage * 10;
        this.count = res.data.totalCount;
      }
    });
  },
}
</script>

<style scoped>
.pagination-container {
  margin-top: 20px;
  text-align: center;
}
</style>
