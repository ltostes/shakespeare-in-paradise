<template>
  <div class="hello">
    <h1 class='Home'>Welcome to Shakespeare in Paradise!</h1>
    <div id="Clouds">
      <div class="Cloud Foreground"></div>
      <div class="Cloud Background"></div>
      <div class="Cloud Foreground"></div>
      <div class="Cloud Background"></div>
      <div class="Cloud Foreground"></div>
      <div class="Cloud Background"></div>
    </div>

      <v-container fluid class="pa-0">
        <v-row>
          <v-col cols="12">
            <v-btn>Create Game</v-btn>
          </v-col>
        </v-row>
      </v-container>
      <join-form></join-form>
    <router-view></router-view>
  </div>
</template>

<script>
import { mapMutations } from 'vuex';
import JoinForm from '@/components/JoinForm';

export default {
  name: 'Home',
  components: {
    JoinForm
  },
  mounted() {
    document.body.className = 'Home';
    this.reset_error();
  },
  methods: {
    ...mapMutations(['reset_error']),
  },
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h3 {
  margin: 40px 0 0;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
</style>
