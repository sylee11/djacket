<template>
    <div class="page-cart">
        <div class="columns is-multiline">
            <div class="column is-12">
                <h1 class="title">Checkout</h1>
            </div>
            <div class="column is-12 box">
                <table class="table is-fullwidth" >
                    <thead>
                        <tr>
                            <th>Product</th>
                            <th>Price</th>
                            <th>Quantity</th>
                            <th>Total</th>
                        </tr>
                    </thead>
                    <tbody>    
                        <ProcessChekoutRecord
                            v-for="item in cart.items"
                            v-bind:key="item.product"
                            v-bind:inititalItem="item"
                            v-on:removeItem="removeItem"
                        />
                        <tr>
                            <td> Total</td>
                            <td></td>
                            <td></td>
                            <td> $ {{ getItemTotal().toFixed(2)}}</td>
                        </tr>
                    </tbody>
                </table>
            </div>
             <div class="column is-12 box">
                <h2 class="subtitle">Shipping details</h2>

                <p class="has-text-grey mb-4">* All fields are required</p>

                <div class="columns is-multiline">
                    <div class="column is-6">
                        <div class="field">
                            <label>First name*</label>
                            <div class="control">
                                <input type="text" class="input" v-model="first_name">
                            </div>
                        </div>

                        <div class="field">
                            <label>Last name*</label>
                            <div class="control">
                                <input type="text" class="input" v-model="last_name" required>
                            </div>
                        </div>

                        <div class="field">
                            <label>E-mail*</label>
                            <div class="control">
                                <input type="email" class="input" v-model="email">
                            </div>
                        </div>

                        <div class="field">
                            <label>Phone*</label>
                            <div class="control">
                                <input type="text" class="input" v-model="phone">
                            </div>
                        </div>
                    </div>

                    <div class="column is-6">
                        <div class="field">
                            <label>Address*</label>
                            <div class="control">
                                <input type="text" class="input" v-model="address">
                            </div>
                        </div>

                        <div class="field">
                            <label>Zip code*</label>
                            <div class="control">
                                <input type="text" class="input" v-model="zipcode">
                            </div>
                        </div>

                        <div class="field">
                            <label>Place*</label>
                            <div class="control">
                                <input type="text" class="input" v-model="place">
                            </div>
                        </div>
                    </div>
                </div>

                <div class="notification is-danger mt-4" v-if="errors.length">
                    <p v-for="error in errors" v-bind:key="error">{{ error }}</p>
                </div>

                <hr>

                <div id="card-element" class="mb-5"></div>

                <template v-if="getItemTotal">
                    <hr>

                    <button class="button is-dark" @click="submitForm">Pay with Stripe</button>
                </template>
            </div>
        </div>
    </div>
</template>

<script>
import ProcessChekoutRecord from '@/components/ProcessCheckoutRecord.vue'
import axios from 'axios'
export default {
    name : 'CheckoutProcess',
    data() {
        return {
            cart: {
                items: []
            },
            first_name: '',
            last_name: '',
            stripe: {},
            card: {},
            email: '',
            phone: '',
            address: '',
            zipcode: '',
            place: '',
            errors: [],
        }
    },
    mounted() {
        this.cart = this.$store.state.cart
        if (this.cartTotalLength > 0) {
            this.stripe = window.Stripe('pk_test_51LI8d7LSpjtp1yOao4XaHnaziuZ3PuGi5zHMIV0r0lVmLMrD1af8E5k9AcVoeNHSZKovCmzMqt5XbbLaWy693qvn00cg8jMZ3R')
            const elements = this.stripe.elements();
            this.card = elements.create('card', { hidePostalCode: true })
            this.card.mount('#card-element')
        }
    },
    components: {
        ProcessChekoutRecord
    },
    methods: {
        getItemTotal() {
            return this.cart.items.reduce((curVal, item) => {
                return item.quantity * item.product.price + curVal 
            }, 0)
        },
         submitForm() {
             this.errors = []
             if (!this.first_name) {
                 this.errors.push('First name is required')
             }

             if (!this.errors.length) {
                 this.stripe.createToken(this.card).then(result => {                    
                    if (result.error) {
                        this.errors.push('Something went wrong with Stripe. Please try again')
                        console.log(result.error.message)
                    } else {
                        this.stripeTokenHandler(result.token)
                    }
                })
             }
         },
         async stripeTokenHandler(token) {
            const items = []
            for (let i = 0; i < this.cart.items.length; i++) {
                const item = this.cart.items[i]
                const obj = {
                    product: item.product.id,
                    quantity: item.quantity,
                    price: item.product.price * item.quantity
                }
                items.push(obj)
            }
            const data = {
                'first_name': this.first_name,
                'last_name': this.last_name,
                'email': this.email,
                'address': this.address,
                'zipcode': this.zipcode,
                'place': this.place,
                'phone': this.phone,
                'items': items,
                'stripe_token': token.id
            }
            await axios
                .post('/api/v1/checkout/', data)
                .then(response => {
                    this.$store.commit('clearCart')
                    this.$router.push('/cart/success')
                    console.log(response);
                })
                .catch(error => {
                    this.errors.push('Something went wrong. Please try again')
                    console.log(error)
                })
        }
    },
    computed: {
        cartTotalPrice() {
            return this.cart.items.reduce((acc, curVal) => {
                return acc += curVal.product.price * curVal.quantity
            }, 0)
        },
        cartTotalLength() {
            return this.cart.items.reduce((acc, curVal) => {
                return acc += curVal.quantity
            }, 0)
        }
    }
}
</script>

<style>

</style>