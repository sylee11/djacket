<template>
        <div class="box">
          <figure class="image mb-4">
            <img :src="product.get_thumnail" alt="thumnail">
          </figure>

          <h3 class="is-size-4"> {{ product.name }} </h3>
          <p class="is-size-6 has-text-grey"> ${{ product.price }} </p>

          <router-link v-bind:to="product.get_absolute_url" class="button is-dark mt-4">Views details</router-link> 
        </div>
</template>

<script>
export default {
    name: "ProductBox",
    props: {
        product: {}
    },

}
</script>

<style>

</style>