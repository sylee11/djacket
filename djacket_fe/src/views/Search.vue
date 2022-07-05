<template>
  <div class="page-search">
    <h1 class="is-size-1 has-text-black">Search</h1>
    <div class="columns is-multiline">
        <div class="column is-12">
            <h2 class="is-size-5 has-text-grey">Search term: "{{query}}"</h2>
        </div>
        <div
            class="column is-3"
            v-for="product in products"
            v-bind:key="product.id"
        >   
            <Product-box  :product="product"/>
        </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import ProductBox from '@/components/ProductBox.vue'
export default {
    name: 'SearchView',
    data() {
        return {
            products: [],
            query: ''
        }
    },
    components: { ProductBox },
    mounted() {
        let uri = window.location.search.substring(1)
        let params = new URLSearchParams(uri)

        if (params.get('query')) {
            this.query = params.get('query')
            this.performSearch()
        }

    },
    methods: {
        async performSearch() {
            axios.post('api/v1/products/search', {'query': this.query})
                .then(res=>{
                    this.products = res.data
                })
                .catch(err=>{
                    console.log(err);
                })
        }
    }

}   
</script>

<style>

</style>