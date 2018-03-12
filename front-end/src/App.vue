<template>
  <div class="app">
    <nav-bar :shortlist="shortlist" @home="showCriteria = true ; showCarousel = false; showShortlist = false"
    @shortlist="showCriteria = false; showCarousel = false; showShortlist = true"
    @carousel="showCriteria = false; showCarousel = true; showShortlist = false"
      />
    <div class="app-body">
      <transition name="fade">
        <criteria v-if="showCriteria" :anniversaries="anniversaries" @submittedCriteria="filterGifts" />
      </transition>
      <transition name="fade">
        <gifts v-if="showCarousel" :products="filteredProducts" :shortlist="shortlist" @shortlistedProduct="addToShortlist" @removedProduct="removeProduct" @viewShortlist="viewShortlist" />
      </transition>
      <transition name="fade">
        <shortlist v-if="showShortlist" :products="shortlist" />
      </transition>
    </div>
  </div>
</template>

<script>
import NavBar from './components/NavBar';
import Criteria from './components/Criteria';
import Gifts from './components/Gifts';
import Shortlist from './components/Shortlist';
import axios from 'axios';

export default {
  name: 'App',

  components: {
    NavBar,
    Criteria,
    Gifts,
    Shortlist,
  },

  data () {
    return {
      allProducts: [],
      anniversaries: [],
      showCriteria: true,
      showCarousel: false,
      showShortlist: false,
      filteredProducts: [],
      shortlist: []
    }
  },

  created() {
    this.fetch()
  },

  methods: {
    fetch: function() {
      axios.get('http://localhost:8000/products/')
        .then(response => {
          this.allProducts = response.data;
          this.allProducts.forEach(product => {
            if (!this.anniversaries.includes(product.anniversary)) this.anniversaries.push(product.anniversary)
          })
          this.anniversaries.sort((a, b) => a - b)
          window.dispatchEvent(new Event('resize'));
        })
        .catch(e => {console.log(e)})
    },

    filterGifts: function(criteria) {
      this.priceMap();
      this.filteredProducts = this.allProducts.filter((product) => {
        if (product.anniversary == criteria.anniversary && product.priceBracket == criteria.price) {
          return product
        }
      })
      this.showCarousel = true;
      this.showCriteria = false;
    },

    priceMap: function() {
      this.allProducts.sort((a, b) => {
        return parseInt(a.price) - parseInt(b.price)
      })
      this.allProducts.forEach((product, index) => {
        if (index < this.allProducts.length / 3) {
          product['priceBracket'] = 'cheap'
        } else if (index > (this.allProducts.length*2) / 3) {
          product['priceBracket'] = 'expensive'
        } else {
          product['priceBracket'] = 'average'
        };
      })
    },

    addToShortlist(product) {
      this.shortlist.push(product)
      if (this.filteredProducts.indexOf(product) < this.filteredProducts.length - 1) {
        this.filteredProducts.pop()
      } else {
        let lastItem = this.filteredProducts.pop()
        this.filteredProducts = this.filteredProducts.filter(p => p != product)
        window.dispatchEvent(new Event('resize'));
      }
    },

    removeProduct(product) {
      this.filteredProducts = this.filteredProducts.filter(p => p != product)
    },

    viewShortlist() {
      this.showShortlist = true;
      this.showCarousel = false;
      this.showCriteria = false;
    }
  }
}
</script>

<style>

@import url('https://fonts.googleapis.com/css?family=Lato');

body {
  background: #EDEDED;
  font-family: 'Lato', sans-serif;
  margin: 0 2px;
}

.full-width * {
  color: black;
}

button {
  display: table;
  color: white;
  background: #44c583;
  border: none;
  padding: 15px 20px;
  width: 175px;
  margin: 10px auto;
  border-radius: 5px;
  font-size: 1em;
  /* outline: none; */
}

figure {
  padding: 15px;
  margin: 0
}

figcaption {
  display: flex;
  justify-content: space-between;
  font-size: 1.2em;
  width: 100%;
}

span {
  display: inline-block;
}

figcaption > span:first-of-type {
  width: 75%;
}

.app {
  height: 100vh;
  display: flex;
  flex-flow: column;
}

.app-body {
  flex: 1 1 0;
  display: flex;
  flex-direction: column;
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

</style>
