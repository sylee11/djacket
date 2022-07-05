<template>
  <div class="page-sign-up">
      <class class="columns">
          <div class="column is-4 is-offset-4">
              <h1 class="title">Log in</h1>
              <form action="" @submit.prevent="event => submitLogin()">
                  <div class="field">
                      <label for="">Username</label>
                      <clas class="control">
                          <input type="text" id="" class="input" v-model="username">
                      </clas>
                  </div>

                   <div class="field">
                      <label for="">Password</label>
                      <clas class="control">
                          <input type="password" id="" class="input" v-model="password">
                      </clas>
                  </div>
                   <div class="field">
                      <clas class="control">
                          <button class="button is-dark"> Log in</button>
                      </clas>
                  </div>

                  <div class="notification is-danger" v-if="errors.length">
                      <p v-for="er in errors" v-bind:key="er"> {{er}} </p>
                      
                  </div>

                  <hr>

                  Or <router-link to="/sign-up"> click here </router-link> to sign up!
              </form>
          </div>
      </class>
  </div>
</template>

<script>
import axios from 'axios'
export default {
    name: 'logIn',
    data() {
        return{
            username : '',
            password : '',
            errors : []
        }
    },
    mounted() {
        const isAuthend = this.$store.state.isAuthenticated
        const token = this.$store.state.token
        console.log(isAuthend, token);
    },
    methods: {
        submitLogin(){
            this.errors = []
            if (this.username && this.password){
                const formData = {
                    username: this.username,
                    password: this.password
                }
                axios.post('api/v1/token/login/', formData)
                    .then(res => {
                        const dataRes = res.data
                        this.$store.commit('saveToken', dataRes.auth_token)
                        localStorage.setItem('token', dataRes.auth_token)
                        
                        const path = this.$route.query.to || '/cart'

                        this.$router.push(path)
                    })
                    .catch(err => {
                        console.log('ee', err);
                    })
            } else {
                this.errors.push('Username or password is not empty')
            }
        }
    }
}
</script>

<style>

</style>