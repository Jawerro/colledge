<template lang="pug">
#app
    .card(v-for="product in products")
    .card-header
        button.btn.btn-clear.float-right(@click="deleteNote(note)")
        .card-product {{ product.product }}
        .card-price {{ product.price }}
    .card-deployer {{ product.deployer }}
</template>
<script>
import { mapGetters } from 'vuex'
export default {
  name: 'product-list',
  computed: mapGetters(['products']),
  methods: {
    deleteProduct (product) {
      // Вызываем действие `deleteNote` из нашего хранилища, которое
      // попытается удалить заметку из нашех базы данных, отправив запрос к API
      this.$store.dispatch('deleteProduct', product)
    }
  },
  beforeMount () {
    // Перед тем как загрузить страницу, нам нужно получить список всех
    // имеющихся заметок. Для этого мы вызываем действие `getNotes` из
    // нашего хранилища
    this.$store.dispatch('getProduct')
  }
}
</script>
<style>
header {
  margin-top: 50px;
}
</style>
