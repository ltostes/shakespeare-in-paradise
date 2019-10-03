import Vue from 'vue';
import Router from 'vue-router';
import Home from '@/components/Home';
import Bar from '@/components/Bar';
import Room from '@/components/Room';
import Player from '@/components/Player';

Vue.use(Router);

export default new Router({
  mode: 'history',
  routes: [
    {
      path: '/',
      name: 'Root',
      redirect: 'home',
    },
    {
      path: '/home',
      name: 'Home',
      component: Home,
    },
    {
      path: '/bar',
      name: 'Bar',
      component: Bar,
    },
    {
      path: '/:room/waiting',
      name: 'Room',
      component: Room,
    },
    {
      path: '/player/:player_number',
      name: 'Player',
      component: Player,
    }
    ]})
