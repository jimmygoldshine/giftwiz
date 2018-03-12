<template>
  <div class='full-width'>
    <h3 @click="gifts">Gifts</h3>
    <h1 @click="home">Giftwiz</h1>
    <h3 @click="viewShortlist">Shortlist({{ shortlist.length }})</h3>
  </div>
</template>

<script>

export default {

  name: 'NavBar',

  props: ['shortlist'],

  methods: {
    home() {
      this.$emit('home')
    },
    viewShortlist() {
      this.$emit('shortlist')
    },
    gifts() {
      this.$emit('carousel')
    }
  }

}

</script>

<style>

  h1, h2 {
    margin: 10px 0;
  }

  .full-width {
    display: flex;
    justify-content: space-between;
    z-index: 1;
    width: 90%;
    margin: 0 auto;
    max-width: 500px;
  }

  .full-width * {
    text-align: center;
    width: 33%;
  }




</style>
