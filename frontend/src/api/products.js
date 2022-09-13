import { HTTP } from './common'

export const Product = {
  create (config) {
    return HTTP.post('/products/', config).then(response => {
      return response.data
    })
  },
  delete (product) {
    return HTTP.delete(`/products/${product.id}`)
  },
  list () {
    return HTTP.get('/products/').then(response => {
      return response.data
    })
  }
}
