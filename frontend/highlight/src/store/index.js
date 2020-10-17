import { createStore } from 'vuex';
import axios from 'axios';

const languagesUrl = 'http://192.168.1.101:8000/languages/';
const formatsUrl = 'http://192.168.1.101:8000/formats/';
const stylesUrl = 'http://192.168.1.101:8000/styles/';

export default createStore({
  state: {
    languages: [],
    formats: [],
    styles: [],
  },
  mutations: {
    updateLanguages(state, payload) {
      state.languages = payload.languages;
    },
    updateFormats(state, payload) {
      state.formats = payload.formats;
    },
    updateStyles(state, payload) {
      state.styles = payload.styles;
    },
  },
  actions: {
    // action to fetch all available languages.
    fetchLanguages(context) {
      axios.get(languagesUrl)
        .then((response) => context.commit('updateLanguages', { languages: response.result.data }))
        .catch((error) => console.log(error));
    },
    // action to fetch all available formats.
    fetchFormats(context) {
      axios.get(formatsUrl)
        .then((response) => context.commit('updateLanguages', { formats: response.result.data }))
        .catch((error) => console.log(error));
    },
    // action to fetch all available styles.
    fetchStyles(context) {
      axios.get(stylesUrl)
        .then((response) => context.commit('updateLanguages', { styles: response.result.data }))
        .catch((error) => console.log(error));
    },
  },
  modules: {
  },
});
