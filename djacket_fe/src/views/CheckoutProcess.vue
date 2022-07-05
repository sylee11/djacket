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
export default {
    name : 'CheckoutProcess',
    data() {
        return {
            cart: this.$store.state.cart,
            first_name: '',
            last_name: '',
            email: '',
            phone: '',
            address: '',
            zipcode: '',
            place: '',
            errors: [],
            cartTotalLength: 0,
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
         }
    }
}
</script>

<style>

</style>