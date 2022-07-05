<template>
  <div class="page-cart">
      <div class="columns is-multiline">
          <div class="column is-12">
              <h1 class="title">Cart</h1>
          </div>

          <div class="column is-12 box">
              <table class="table is-fullwidth" v-if="cartTotalLength">
                <thead>
                    <tr>
                        <th>Product</th>
                        <th>Price</th>
                        <th></th>
                        <th>Total</th>
                        <th></th>
                    </tr>
                </thead>
                <tbody>
                     <CartRecord
                            v-for="item in cart.items"
                            v-bind:key="item.product"
                            v-bind:inititalItem="item"
                            v-on:removeItem="removeItem"
                    />
                </tbody>
              </table>
              <p v-else> You don`t have any products in your card ...</p>
          </div>
          <div class="column is-12 box">
              <h2 class="subtitle">Summary</h2>
              <strong>${{ cartTotalPrice.toFixed(2) }}</strong>, {{ cartTotalLength }} items
              <hr>
              <router-link to="/cart/checkout" class="button is-dark"> Proceed to checkout </router-link>
          </div>
      </div>
  </div>
</template>

<script>
import CartRecord from '@/components/CartRecord.vue'
// import axios from 'axios'
export default {
    name : "CartView",
    components: {
        CartRecord
    },
    data() {
        return {
            cart: {
                items: []
            }
        }
    },
    mounted() {
        this.cart = this.$store.state.cart
    },
    computed: {
        cartTotalLength() {
            return this.cart.items.reduce((acc, curVal) => {
                return acc += curVal.quantity
            }, 0)
        },
        cartTotalPrice() {
            return this.cart.items.reduce((acc, curVal) => {
                return acc += (curVal.quantity * curVal.product.price)
            }, 0)
        }
    },
    methods: {
        removeItem(item) {
            this.cart.items = this.cart.items.filter(i => i.product.id !== item.product.id)
        }
    }

}
</script>

<style>

</style>