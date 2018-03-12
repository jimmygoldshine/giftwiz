<template>
  <div class="product">
    <div class="remove" @click="removeProduct">
      <img src='../assets/cancel.png'>
    </div>
    <figure @click="viewDetails = !viewDetails">
      <div>
        <img :src="product.image">
      </div>
      <figcaption>
        <span>{{ product.name }}</span>
        <span class="price">£{{ product.price }}</span>
      </figcaption>
    </figure>
    <transition name="fade">
      <div class="product-details" v-if="viewDetails">
        <button><a :href="product.url">BUY GIFT</a></button>
        <p>Taking you to the retailers website</p>
        <h4>Product Details</h4>
        <span>{{ shorten(product.description) }}</span>
      </div>
    </transition>
  </div>
</template>

<script>

export default {
  name: 'Product',

  props: ['product'],

  data () {
    return {
      viewDetails: false
    }
  },

  methods: {
    shorten(description) {
      return description.split('.', 2).join('.') + '!'
    },
    removeProduct() {
      this.$emit('remove')
    }
  }
}
</script>

<style>

@import url('https://fonts.googleapis.com/css?family=Lato');

p {
  text-align: center;
}

a {
  color: white;
  text-decoration: none;
}

.product-details {
  margin: 20px 10px;
}

.fade-enter-to, .fade-leave {
  max-height: 550px;
  height: 100%;
}

.fade-enter-active, .fade-leave-active {
  transition: max-height 1s linear;
}
.fade-enter, .fade-leave-to {
  height: auto;
  max-height: 0;
}

.product {
  position: relative;
}

.remove {
  position: absolute;
  height: 25px;
  width: 25px;
  right: 2px;
  top: -5px;
}


</style>
