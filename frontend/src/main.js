import Vue from 'vue'
import Router from 'vue-router';

import App from './App.vue'
import { routes } from "./router/index.js";

Vue.use(Router);

const router = new Router({
  routes,
  mode: 'history',
});

Vue.config.productionTip = false

new Vue({
  router,
  render: h => h(App)
}).$mount('#app')
