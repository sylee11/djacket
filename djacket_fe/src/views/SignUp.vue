<template>
  <div class="page-sign-up">
      <class class="columns">
          <div class="column is-4 is-offset-4">
              <h1 class="title">Sign Up</h1>
              <form action="" @submit.prevent="(event) => submitSignUp(event)">
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
                      <label for="">Repeat Password</label>
                      <clas class="control">
                          <input type="password" id="" class="input" v-model="passwordRepeat">
                      </clas>
                  </div>

                   <div class="field">
                      <clas class="control">
                          <button class="button is-dark"> Sign up</button>
                      </clas>
                  </div>

                  <div class="notification is-danger" v-if="errors.length">
                      <p v-for="er in errors" v-bind:key="er"> {{er}} </p>
                      
                  </div>

                  <hr>

                  Or <router-link to="/log-in"> click here </router-link> to login!
              </form>
          </div>
      </class>
  </div>
</template>

<script>
import axios from 'axios'
import { toast } from 'bulma-toast';
export default {
    name: 'signUp',
    methods: {
        submitSignUp(e) {
            console.log('clock', e);
            this.errors = []

            if (this.username === '') {
                this.errors.push('The username is not empty')
            }

            if (this.password !== this.passwordRepeat) {
                this.errors.push('Password and password repeat not match')
            }
            
            if (!this.errors.length) {
                const formData = {
                    username: this.username,
                    password: this.password
                }
                axios.post("api/v1/users/", formData)
                        .then(res => {
                            toast({
                                message: 'Account created',
                                type: 'is-success',
                                dismissible: true,
                                pauseOnHover: true,
                                duration: 2000,
                                position: 'bottom-right'
                            })
                            console.log(res.data);
                            this.$router.push('/log-in')
                        })
                        .catch(err => {
                            console.log(err.response);
                        })
            }
        }
    },
    data() {
        return{
            errors: [],
            username: '',
            password: '',
            passwordRepeat: '',
        }
    }
}
</script>

<style>

</style>