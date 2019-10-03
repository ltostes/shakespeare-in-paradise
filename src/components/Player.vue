<template>
  <div class="player">
    <h1>You are player: {{ player_number }}</h1>
    This is your word
  </div>
</template>

<script>
export default {
  name: 'Player',
  data: function () {
    return {
      player_number : this.$route.params.player_number
    }
  },
  mounted: function() {
        var new_number = this.$route.params.player_number;
        if (new_number) {
          this.$store.commit('change_player_color_by_order',new_number)
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
