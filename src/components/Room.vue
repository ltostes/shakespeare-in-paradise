<template>
  <div class="room">
    <h3>You are in room: {{ room }}</h3>
  </div>
</template>

<script>

import { mapMutations, mapState } from "vuex";

export default {
  name: 'Room',
  computed: {
      ...mapState(["room"]),
  },
  methods: {
    ...mapMutations(["set_username", "set_room"]),
  },
  mounted() {
    if (!this.username) this.set_username('#unknown');
    if (this.room != this.$route.params.room) {
      const params = {
        username: this.username,
        room: this.$route.params.room,
      };
      this.$socket.client.emit('join', params);
    }
  }
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
