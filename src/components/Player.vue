<template>
  <div class="player">
      <h1 >Word: {{player_word()}}</h1>
      <i>Round: {{round_number()}}</i>
      <span v-if="isAdminPlayer">Now you see me</span>
  </div>
</template>

<script>
import { mapGetters, mapState, mapMutations } from 'vuex';

export default {
  name: 'player',
  computed: {
    ...mapState(['room', 'username','player_number']),
    ...mapGetters(['player_word','round_number','isAdminPlayer'])
  },
  mounted() {
    if (!this.username) this.set_username('#unknown');
    if (!this.room) this.set_room(this.$route.params.room);
    if (!this.player_number) this.set_player_number(this.$route.params.player_number);
    const params = {
      username: this.username,
      room: this.room,
      player_number: this.player_number,
    };
  },
  methods: {
    ...mapMutations(['set_room', 'set_username','set_player_number']),
  },
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h1, h2 {
  font-weight: normal;
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
