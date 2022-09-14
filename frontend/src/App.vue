<template>
  <div id="app">
    <div id="nav">
      <router-link to="/">Home</router-link> |
      <router-link to="/create">Add Product</router-link> |
      <router-link to="/about">About</router-link>
    </div>
    <router-view/>
  </div>
</template>

<script>
import Product from '../src/components/ProductList.vue'
export default {
  name: 'App',
  components: {
    Product
  }
}
</script>
<style>
*{
  margin: 0px;
  padding: 0px;
}
body{
  background-color: #fcfcfc;
  text-align: center;
}
#nav {
    margin: 20px 0;
}
</style>
