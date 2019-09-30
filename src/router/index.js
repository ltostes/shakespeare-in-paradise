import Vue from 'vue'
import Router from 'vue-router'
import Home from '@/components/Home'
import Player from '@/components/Player'
//import Cheatsheet from '@/components/Cheatsheet'
//import Join from '@/components/Join'
//import WaitingRoom from '@/components/WaitingRoom'

Vue.use(Router)

export default new Router({
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
      path: '/:room/player/:player_number',
      name: 'Player',
      component: Player,
    },
    {
      path: '/:room/join',
      name: 'Join',
      component: Join,
    },
    {
      path: '/:room/waitingroom',
      name: 'WaitingRoom',
      component: WaitingRoom,
    },
    {
      path: '/:room/cheatsheet',
      name: 'Cheatsheet',
      component: Cheatsheet,
    },
  ]
})
