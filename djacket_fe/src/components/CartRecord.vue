<template>
    <tr>
        <td><router-link to="item.product.get_absolute_url"> {{item.product.name}} </router-link></td>
        <td> ${{ item.product.price }} </td>
        <td>
            {{item.quantity}} 
            <button @click="incrementQuantity(item)">+</button>
            <button @click="decrementQuantity(item)">-</button>
        </td>
        <td> $ {{ getItemTotal(item).toFixed(2)}}</td>
        <td><button class="delete" @click="removeItem(item)"></button></td>
    </tr>
</template>

<script>
export default {
    name: 'CartRecord',
    props: {
        inititalItem: Object
    },
    data() {
        console.log(this.inititalItem);
        return {
            item: this.inititalItem
        }
    },
    methods: {
        getItemTotal(item) {
            return item.quantity * item.product.price
        },
        incrementQuantity(item) {
            item.quantity +=1
            this.updateLocalStorage()

        },
        decrementQuantity(item) {
            if (item.quantity > 0){
                item.quantity -=1
                this.updateLocalStorage()
            } else {
                this.removeItem(item)
            }
        },
        removeItem(item) {
            this.$emit('removeItem', item)
            this.updateLocalStorage()
        },
        updateLocalStorage(){
            localStorage.setItem('cart', JSON.stringify(this.$store.state.cart))
        }
    }
}
</script>

<style>

</style>