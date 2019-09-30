import Vue from 'vue';
import Vuex from 'vuex';
import createPersistedState from 'vuex-persistedstate'
import * as Cookies from 'js-cookie'

Vue.use(Vuex);
const inFifteenMinutes = new Date(new Date().getTime() + 15 * 60 * 1000);

export default new Vuex.Store({
  plugins: [createPersistedState({
    storage: {
      getItem: key => Cookies.get(key),
      // Please see https://github.com/js-cookie/js-cookie#json, on how to handle JSON.
      setItem: (key, value) => Cookies.set(key, value, { expires: inFifteenMinutes }),
      removeItem: key => Cookies.remove(key)
    }
  })],
  state: {
    connected: false,
    dictionaries: [],
    game: {},
    round_info: {},
    room: '',
    username: '',
    player_number: '',
    error: ''
  },
  getters: {
    player_word(state) {
      return state.round_info.player_info[state.player_number-1].round_word
    },
    round_number(state) {
      return state.round_number
    },
    isAdminPlayer(state,player_number) {
      return state.player_number == 1
    }
  },
  mutations: {
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
    set_turn(state, team) {
      state.turn = team;
    },
    set_game(state, game) {
      state.game = game;
    },
    set_room(state, room) {
      state.room = room;
    },
    set_username(state, username) {
      state.username = username;
    },
    set_player_number(state, player_number) {
      state.player_number = player_number;
    },
    reset_error(state) {
      state.room = '';
      state.error = '';
    },
    reset_room(state) {
      state.game = {};
    },
  },
});
