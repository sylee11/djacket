<template>
  <div id="wrapper">
    <nav class="navbar is-dark">
      <div class="navbar-brand">
        <router-link to="/" class="navbar-item"><strong>Djackets</strong></router-link>
        <a class="navbar-burger" aria-label="menu" aria-expanded="false" data-target="navbar-menu">
          <span aria-hidden="true"></span>
          <span aria-hidden="true"></span>
          <span aria-hidden="true"></span>
        </a>
      </div>

      <div class="navbar-menu" id="navbar-menu">
        <div class="navbar-start">
          <div class="navbar-item">
            <form action="/products/search" method="get">
              <div class="field has-adddons">
                <input type="text" id="" class="input" name="query">
              </div>
            </form>
            <div class="button is-success">
                <span class="icon">
                  <i class="fas fa-search"></i>
                </span>
              </div>
          </div>
        </div>
        <div class="navbar-end">
          <router-link :to="{ name: 'category', params: { category_slug: 'summer' }}" class="navbar-item">Summer</router-link>
          <router-link :to="{ name: 'category', params: { category_slug: 'winter' }}" class="navbar-item">Winter</router-link>

          <div class="navbar-item">
            <div class="buttons">
              <router-link to="/my-account" class="button is-light" v-if="this.$store.state.isAuthenticated"> My Account </router-link>
              <router-link to="/log-in" class="button is-light" v-else> Login</router-link>

              <button class="button is-danger" v-if="this.$store.state.isAuthenticated" @click="logOut()"> Log out </button>
              <router-link to="/sign-up" class="button is-light" v-else> Sign Up</router-link>

              <router-link :to="{ name: 'cart'}" class="button is-success">
                <span class="icon"> <i class="fas fa-shopping-cart"></i> </span>
                <span >Cart ({{ cartTotalLength }})</span>
              </router-link>
            </div>
          </div>
        </div>
      </div>
    </nav>

    <section class="section">
      <router-view/>
    </section>

    <footer class="footer">
      <p class="has-text-centered">Copyright 2022</p>
    </footer>

  </div>
</template>

<script>
import axios from 'axios'
export default {
  data() {
    // eslint-disable-next-line 
    return { cart: {
        // eslint-disable-next-line 
        items: []
      }
    }
  },
  beforeCreate() {
    this.$store.commit('initializeStore')
    const token = this.$store.state.token
    console.log('ccccccccccccc', token);
    if(token) {
      axios.defaults.headers.common['Authorization'] = "Token " + token
    } else {
      axios.defaults.headers.common['Authorization'] = ''
    }
  },
  mounted() {
    this.cart = this.$store.state.cart
  },
  computed: {
    cartTotalLength() {
      let totalLength = 0
      for(let i = 0; i < this.cart.items.length; i++) {
        totalLength += this.cart.items[i].quantity
      }

      return totalLength
    }
  },
  methods: {
    logOut() {
      this.$store.commit('removeToken')
      localStorage.setItem('token', '')
      this.$router.push('/')
    }
  }
}
</script>

<style lang="scss">
@import '../node_modules/bulma';
</style>
