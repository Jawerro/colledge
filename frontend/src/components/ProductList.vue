<template>
  <div class="product-card">
    <div class="card">
    <p>{{ product }} </p>
    <p>{{ price }}</p>
    <p>{{ deployer }}</p>
    <button class="btn btn-primary">Read More</button>
    </div>
  </div>
</template>

<script>

export default {
  name: 'Product',
  props: ['product', 'price', 'deployer']
}
</script>

<style>
