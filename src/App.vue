<template>
  <div id="app">
    <router-view></router-view>
  </div>
</template>

<script>
import router from './router';
import store from './store';

export default {
  name: 'app',
  router,
  store
}
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  margin-top: 60px;
}
</style>
