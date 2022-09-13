<template lang="pug">
#app
    section.container.grid-960
      .columns
        .column.col-2
        .column.col-8.col-md-12
          header.text-center
            h2 Create product
              create-product
          header.text-center
            h2 List of products
              product-list
        .column.col-2
</template>
<script>
import CreateProduct from './components/CreateProduct'
import ProductList from './components/ProductList'
export default {
  name: 'app',
  components: {
    'create-product': CreateProduct,
    'product-list': ProductList
  }
}
</script>
<style>
  @import url(https://fonts.googleapis.com/css?family=Eczar);
  @import url(https://fonts.googleapis.com/css?family=Work+Sans);
  body {
    font-family: "Work Sans", "Segoe UI", "Helvetica Neue", sans-serif;
  }
  h1, h2, h3, h4, h5, h6 {
    font-family: "Eczar", sans-serif;
  }
</style>
