import Vue from 'vue';
import Vuex from 'vuex';

Vue.use(Vuex);

import router from '@/router/index'

export default new Vuex.Store({
  state: {
    connected: false,
    available_colors: ['Purple', 'Pink', 'Yellow', 'Blue', 'Orange', 'Red', 'Brown', 'Green', 'Gray', 'Black', 'White'],
    player_color: '',
    player_round_word: '',
    round_number: '',
    room:'',
    user_name: '',
    game_status:'',
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
      console.log('Socket connected!');
    },
    SOCKET_DISCONNECT(state) {
      state.connected = false;
      console.log('Socket disconnected!');
    },
    SOCKET_MESSAGE(state, message) {
      state.game = message;
      state.room = message.game_id;
      state.error = null;
      console.log('New notification! ', message);
    },
    SOCKET_JOIN_ROOM(state, message) {
      state.error = null;
      state.room = message.room;
      console.log('Joined room: ', message.room);
      router.push({ name: 'Room', params: { room: state.room } });

    },
    SOCKET_LIST_DICTIONARIES: (state, message) => {
      state.dictionaries = message.dictionaries;
    },
    SOCKET_ERROR(state, message) {
      state.error = message.error;
      console.log('New error! ', message.error);
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
