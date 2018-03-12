<template>
  <div class="shortlist">
    <div v-for="product in products">
      <product :product="product" />
    </div>
  </div>
</template>

<script>

import Product from './Product';

export default {
  name: 'Shortlist',

  props: ['products'],

  components: {
    Product
  },

  data () {
    return {

    }
  },

  methods: {

  }
}
</script>

<style>

@import url('https://fonts.googleapis.com/css?family=Lato');

.shortlist {
  display: flex;
  flex-direction: column;
}

.shortlist figure {
  background: white;
  border-radius: 5px;
  -webkit-box-shadow: 0 10px 20px rgba(0,0,0,0.19), 0 6px 6px rgba(0,0,0,0.23);
  box-shadow: 0 10px 20px rgba(0,0,0,0.19), 0 6px 6px rgba(0,0,0,0.23);
  margin: 10px auto;
}

</style>
