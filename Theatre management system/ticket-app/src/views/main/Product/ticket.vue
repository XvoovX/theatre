<template>
  <HeaderNav></HeaderNav>
  <div class="order">
    <ProductList></ProductList>
    <ProductPagination></ProductPagination>
  </div>
</template>

<script>
import HeaderNav from '@/components/HeaderNav.vue';
import ProductList from './ProductList.vue';
import ProductPagination from './ProductPagination.vue';

export default {
  components: {
    HeaderNav,
    ProductList,
    ProductPagination,
  },
  data() {
    return {};
  },
}
</script>

<style scoped>
.order {
  width: 80%;
  margin: 0 auto;
  padding-top: 15px;
}

@media (max-width: 768px) {
  .order {
    width: 100%;
    padding: 10px;
  }
}
</style>
