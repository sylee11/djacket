<template>
  <div class="home">
    <section class="hero is-medium is-dark mb-6">
      <div class="hero-body has-text-centered">
        <p class="title mb-6">
          WelCome to Djacket
        </p>
        <p class="subtitle">
          The best jacket store online
        </p>
      </div>
    </section>
    <div class="columns is-multiline">
      <div class="column is-12">
        <h2 class="is-size-2 has-text-centered"> Lastest Product</h2>
      </div>
      <div
        class="column is-3"
        v-for="product in lastestProducts"
        v-bind:key="product.id"
      >
        <ProductBox :product="product" />

      </div>
    </div>
  </div>
</template>

<script>
// @ is an alias to /src
import axios from 'axios';
import ProductBox from '../components/ProductBox.vue';

export default {
  name: 'HomeView',
  data() {
    return {
      lastestProducts: []
    }
  },
  components: {
    ProductBox
  },
  mounted() {
    this.getLastestProduct()
  },
  methods: {
    getLastestProduct() {
      axios.get('/api/v1/lastest-product').then(response => {
        this.lastestProducts = response.data
      }).catch(error => {
        console.log(error)
      })
    }
  }
}
</script>
