<template>
    <div class="page-category">
        <div class="columns is-multiline">
            <h2 class="is-size-2 has-text-centered">{{category.name}}</h2>
        </div>
        <div
            class="column is-3"
            v-for="product in category.products"
            v-bind:key="product.id"
        >   
            <Product-box  :product="product"/>
        </div>
    </div>
</template>

<script>
import axios from 'axios'
import { toast } from 'bulma-toast'
import ProductBox from '../components/ProductBox.vue'

export default {
    name: 'CategoryView',
    data() {
        return {
            category: {
                products: []
            }
        }
    },
    components: {
        ProductBox
    },
    mounted() {
        this.getCategory()
    },
    watch: {
    $route(to) {
      if(to.name === 'category') {
        this.getCategory()
      }
    }
  },
    methods: {
        async getCategory(){
            const categorySlug = this.$route.params.category_slug

            await axios.get(`api/v1/categories/${categorySlug}`)
                .then(res => {
                    this.category = res.data

                    document.title = this.category.name + ' | Djackets'
                })
                .catch( err => {
                    console.log(err);
                    toast({
                        message: 'Has error from server',
                        type: 'is-success',
                        dismissible: true,
                        pauseOnHover: true,
                        duration: 2000,
                        position: 'bottom-right'
                    })
                })
        }
    }
}
</script>

<style>

</style>