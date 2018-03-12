import Vue from 'vue'
import App from './App'

Vue.config.productionTip = false

var vm = new Vue({
  el: '#app',
  components: { App },
  template: '<App/>'
})
