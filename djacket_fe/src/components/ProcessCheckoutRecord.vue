<template>
    <tr>
        <td> {{item.product.name}} </td>
        <td> ${{ item.product.price }} </td>
        <td>
            {{item.quantity}} 
        </td>
        <td> $ {{ getItemTotal(item).toFixed(2)}}</td>
    </tr>
</template>

<script>
export default {
    name: 'ProcessCheckoutRecord',
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
    }
}
</script>

<style>

</style>