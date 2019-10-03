import Vue from 'vue';
import App from './App.vue';
import VueSocketIO from 'vue-socket.io';

// Contains the player color definitions, to paint the body background
import "@/assets/css/globals.css"
import "@/assets/css/clouds.less"
import vuetify from './plugins/vuetify';
import router from './router';
import store from './store';
//import { sync } from 'vuex-router-sync'

Vue.config.productionTip = false

Vue.use(vuetify);
//Vue.use(VueSocketIO, `//${window.location.host}`, store);
Vue.use(VueSocketIO, 'http://localhost:5000', store);
/*Vue.use(new VueSocketIO({
      debug: true,
      connection: 'http://localhost:5000',
      params: {
        query: 'example=value',
        type: ['websocket']
    },
      vuex: {
        store,
        actionPrefix: 'SOCKET_',
        mutationPrefix: 'SOCKET_'
      },
    })
  );//*/

new Vue({
  vuetify,
  router,
  store,
  render: h => h(App),

}).$mount('#app')
