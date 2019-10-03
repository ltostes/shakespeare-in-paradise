import Vue from 'vue';
import Vuex from 'vuex';

Vue.use(Vuex);

export default new Vuex.Store({
  state: {
    available_colors: ['Purple', 'Pink', 'Yellow', 'Blue', 'Orange', 'Red', 'Brown', 'Green', 'Gray', 'Black', 'White'],
    player_color: '',
    player_round_word: '',
    round_number: '',
    room:'',
    user_name: '',
  },
  getters: {
    get_player_color_by_order: (state) => (player_number) => {
      return state.available_colors[player_number-1]
    }
  },
  mutations: {
    change_player_color(state, new_color) {
      state.player_color = new_color
    },
    change_player_color_by_order(state, player_number) {
      this.commit('change_player_color',this.getters.get_player_color_by_order(player_number));
      document.body.className = state.player_color;
    },
    SOCKET_CONNECT(state) {
      state.connected = true;
    },
    SOCKET_DISCONNECT(state) {
      state.connected = false;
    },
    SOCKET_MESSAGE(state, message) {
      state.game = message;
      state.room = message.game_id;
      state.error = null;
    },
    SOCKET_JOIN_ROOM(state, message) {
      state.error = null;
      state.room = message.room;
    },
    SOCKET_LIST_DICTIONARIES: (state, message) => {
      state.dictionaries = message.dictionaries;
    },
    SOCKET_ERROR(state, message) {
      state.error = message.error;
    },
    set_room(state, room) {
      state.room = room;
    },
    set_username(state, username) {
      state.username = username;
    },
    reset_error(state) {
      state.room = '';
      state.error = '';
    },
  },
});
