import Vue from 'vue'
import Vuex from 'vuex'
import { Product } from '../api/products.js'
import { ADD_PRODUCT, REMOVE_PRODUCT, SET_PRODUCTS } from './mutation-types.js'

Vue.use(Vuex)

const state = {
  products: []
}

const getters = {
  products: state => state.products
}

const mutations = {
  [ADD_PRODUCT] (state, product) {
    state.products = [product, ...state.products]
  },
  [REMOVE_PRODUCT] (state, { id }) {
    state.products = state.products.filter(product => {
      return product.id !== id
    })
  },
  [SET_PRODUCTS] (state, products) {
    state.products = products
  }
}

const actions = {
  createProduct ({ commit }, productData) {
    Product.create(productData).then(product => {
      commit(ADD_PRODUCT, product)
    })
  },
  deleteProduct ({ commit }, product) {
    Product.delete(product).then(response => {
      commit(REMOVE_PRODUCT, product)
    })
  },
  getProduct ({ commit }) {
    Product.list().then(products => {
      commit(SET_PRODUCTS, { products })
    })
  }
}

export default new Vuex.Store({
  state,
  getters,
  actions,
  mutations
})
