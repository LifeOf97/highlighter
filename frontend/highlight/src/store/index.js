import { createStore } from 'vuex';
import axios from 'axios';

// axios default
// axios.defaults.baseURL = 'http://192.168.1.101:8000/highlighter/api';
axios.defaults.baseURL = 'http://192.168.43.208:8000/highlighter/api';
// axios.defaults.baseURL = 'http://127.0.0.1:8000/highlighter/api';
axios.defaults.headers.post['Content-Type'] = 'application/json';
axios.defaults.headers.Accept = 'application/json; indent=4';
axios.defaults.timeout = 100000; // 100sec

export default createStore({
  state: {
    loading: {
      result: false,
      language: false,
      format: false,
      style: false,
    },
    options: {
      languages: [],
      formats: [],
      styles: [],
    },
    highlight: {
      code: '',
      style: '',
      format: '',
      language: '',
    },
    highlighted: {
      result: '',
    },
  },
  // #################
  // STATE MUTATION.
  // #################
  mutations: {
    // mutation to update the loading object states.
    updateLoadingResult(state, payload) {
      state.loading.result = payload.status;
    },
    updateLoadingLanguage(state, payload) {
      state.loading.language = payload.status;
    },
    updateLoadingFormat(state, payload) {
      state.loading.format = payload.status;
    },
    updateLoadingStyle(state, payload) {
      state.loading.style = payload.status;
    },
    // mutation to set/update the options.languages state.
    setLanguagesOptions(state, payload) {
      state.options.languages = payload.languages;
    },
    // mutation to set/update the options.formats state.
    setFormatsOptions(state, payload) {
      state.options.formats = payload.formats;
    },
    // mutation to set/update the options.styles state.
    setStylesOptions(state, payload) {
      state.options.styles = payload.styles;
    },
    // mutation to set/update the highlight objects state.
    toHighlight(state, payload) {
      state.highlight.code = payload.code;
      state.highlight.style = payload.style;
      state.highlight.format = payload.format;
      state.highlight.language = payload.language;
    },
    // mutation to set/update the highlighted object state.
    updateHighlighted(state, payload) {
      state.highlighted.result = payload.highlighted;
    },
  },
  // ###############
  // STATE ACTIONS
  // ###############
  actions: {
    // action to fetch languages.
    fetchLanguages(context) {
      // first we need to set the language loading state to true, which indicates
      // that the process is running. By commiting the updateLoadingLanguage mutation
      context.commit('updateLoadingLanguage', { status: true });
      // then make a get request to the languages api to retrieve the languages.
      axios.get('/options/languages/')
        .then((response) => {
          // commit the setLanguagesOptions mutation.
          context.commit('setLanguagesOptions', { languages: response.data.result });
          // also commit the updateLoadingLanguage mutation passing false as the payload.
          context.commit('updateLoadingLanguage', { status: false });
        })
        .catch((error) => console.log(error.response));
    },
    // action to fetch formats.
    fetchFormats(context) {
      // first we need to set the format loading state to true, which indicates
      // that the process is running. By commiting the updateLoadingFormat mutation
      context.commit('updateLoadingFormat', { status: true });
      // then make a get request to the formats api to retrieve the formats.
      axios.get('/options/formats/')
        .then((response) => {
          // commit the setFormatsOptions mutation.
          context.commit('setFormatsOptions', { formats: response.data.result });
          // also commit the updateLoadingFormat mutation passing false as the payload.
          context.commit('updateLoadingFormat', { status: false });
        })
        .catch((error) => console.log(error.response));
    },
    // action to fetch styles.
    fetchStyles(context) {
      // first we need to set the style loading state to true, which indicates
      // that the process is running. By commiting the updateLoadingStyle mutation
      context.commit('updateLoadingStyle', { status: true });
      // then make a get request to the styles api to retrieve the styles.
      axios.get('/options/styles/')
        .then((response) => {
          // commit the setStylesOptions mutation.
          context.commit('setStylesOptions', { styles: response.data.result });
          // also commit the updateLoadingStyle mutation passing false as the payload.
          context.commit('updateLoadingStyle', { status: false });
        })
        .catch((error) => console.log(error.response));
    },
    // action to commit the mutation to update the highlight objects data.
    highlightDetails(context, payload) {
      context.commit('toHighlight', payload);
    },
    // action to highlight the code snippet.
    async highlightCode(context, payload) {
      // first, set the result loading state to true, by committing the
      // updateLoadingResult mutation, passing {status: true} as payload.
      context.commit('updateLoadingResult', { status: true });
      // then dispatch the highlightDetails action which commits the
      // mutation necessary to update the highlight object states,
      // passing payload.highlight data as its payload.
      await context.dispatch('highlightDetails', payload.highlight);
      // then get the highlight object data as the data to be sent
      // along side the post request. NOTE: made use of getters vuex getters :).
      const data = {
        code: context.getters.getHighlightDetails.code,
        style: context.getters.getHighlightDetails.style,
        getFormat: context.getters.getHighlightDetails.format,
        language: context.getters.getHighlightDetails.language,
        noBackground: false,
      };
      // then make a post request to the highlighter api backend,
      // passing the data as payload to be highlighted.
      await axios.post('/highlight/', data)
        .then((response) => {
          // on success, commit the updateHighlighted mutation along
          // side its payload data to set/update the highlighted.result state.
          context.commit('updateHighlighted', { highlighted: response.data.result.highlighted });
          // then set the result loading state back to false by commiting the
          // updateLoadingResult mutation passing {'status: false'} as its payload.
          context.commit('updateLoadingResult', { status: false });
        })
        .catch((error) => {
          // if a request error occures, make sure to set the loading state back
          // to false and handle the error.
          context.commit('updateLoading', { status: false });
          console.log(error.response.data);
        });
    },
  },
  // ###############
  // STATE GETTERS
  // ###############
  getters: {
    // getter to get languages.
    getLanguages(state) { return state.options.languages; },
    // getter to get formats.
    getFormats(state) { return state.options.formats; },
    // getter to get styles.
    getStyles(state) { return state.options.styles; },
    // getter to get highlight.
    getHighlightDetails(state) { return state.highlight; },
    // getter to get the result loading state.
    getLoadingResult(state) { return state.loading.result; },
    // getter to get the language loading state.
    getLoadingLanguage(state) { return state.loading.language; },
    // getter to get the format loading state.
    getLoadingFormat(state) { return state.loading.format; },
    // getter to get the style loading state.
    getLoadingStyle(state) { return state.loading.style; },
    // getter to get the highlighted code result.
    getHighlighted(state) { return state.highlighted.result; },
  },
  // ###############
  // STATE MODULES
  // ###############
  modules: {
  },
});
