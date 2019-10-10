import Vue from 'vue';
import App from './App.vue';
import VueSocketIOExt from 'vue-socket.io-extended';
import io from 'socket.io-client';

// Contains the player color definitions, to paint the body background
import "@/assets/css/globals.css"
import "@/assets/css/clouds.less"
import vuetify from './plugins/vuetify';
import router from './router';
import store from './store';
//import { sync } from 'vuex-router-sync'

Vue.config.productionTip = false

Vue.use(vuetify);

const socket = io('http://localhost:5000');

Vue.use(VueSocketIOExt, socket, { store });

new Vue({
  vuetify,
  router,
  store,
  render: h => h(App),

}).$mount('#app')
