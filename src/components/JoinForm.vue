<template>
  <v-container>
  <v-fade-transition appear>
              <v-row>
                <v-col cols="12">
                  <v-btn @click.stop="joinGame">Join game</v-btn>
                </v-col>
              </v-row>
                </v-fade-transition>
          <!-- <v-text-field label="Username" v-model="username" required></v-text-field> -->
          <v-alert type="error" :value="showInputError" transition="slide-y-reverse-transition">
            Room ID required to join.
          </v-alert>
          <v-alert type="error" :value="showRoomInexistentError" transition="slide-y-reverse-transition">
            Room doesn't exist
          </v-alert>

          <v-container fluid width='50' :visible="showInput">
            <v-text-field
              label="Enter Room ID"
              v-model="room_num"
              :rules="[rules.required]"
              mask="AAAAA"
              @input="reset_error"
            ></v-text-field>
          </v-container>
        </v-container>
</template>

<script>
import { mapMutations, mapState } from "vuex";

export default {
  name: "create-form",
  data() {
    return {
      // username: '',
      room_num: null,
      showInputError: false,
      showInput: false,
      rules: {
        required: value => !!value || "Required."
      }
    };
  },
  computed: {
    ...mapState(["error"]),
    room_id() {
      return this.room_num.toUpperCase();
    },
    showRoomInexistentError(){
      return this.error == 'Unable to join room. Room does not exist.';
    }
  },
  methods: {
    ...mapMutations(["set_username", "set_room","reset_error"]),
    joinGame() {
      // this.set_username(this.username);
      this.showInputError = false;
      if (this.room_num) {
        const params = {
          room: this.room_num,
        };
        this.$socket.client.emit('join', params);
      } else {
        this.showInputError = true;
      }
    }
  }
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h3 {
  margin: 40px 0 0;
}
a {
  color: #42b983;
}

</style>
