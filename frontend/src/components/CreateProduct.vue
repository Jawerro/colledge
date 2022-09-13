<template lang="pug">
form.form-horizontal(@submit="submitForm")
  .form-group
     .col-3
       label.form-product Product
     .col-9
       input.form-input(type="text" v-model="product" placeholder="Type note title...")
  .form-group
    .col-3
      label.form-price Price
    .col-9
      textarea.form-input(v-model="price" rows=8 placeholder="Type your note...")
  .form-group
    .col-3
      label.form-deployer Deployer
    .col-9
      textarea.form-input(v-model="deployer" rows=8 placeholder="Type your note...")
  .form-group
    .col-3
    .col-9
      button.btn.btn-primary(type="submit") Create
</template>
<script>
export default {
  name: 'create-product',
  data () {
    return {
      product: '',
      price: 0,
      deployer: ''
    }
  },
  methods: {
    submitForm (event) {
      this.createProduct()
      // Т.к. мы уже отправили запрос на создание заметки строчкой выше,
      // нам нужно теперь очистить поля title и body
      this.product = ''
      this.price = 0
      this.deployer = ''
      // preventDefault нужно для того, чтобы страница
      // не перезагружалась после нажатия кнопки submit
      event.preventDefault()
    },
    createProduct () {
      // Вызываем действие `createProduct` из хранилища, которое
      // отправит запрос на создание новой заметки к нашему API.
      this.$store.dispatch('createProduct', {
        product: this.product,
        price: this.price,
        deployer: this.deployer
      })
    }
  }
}
</script>
