import { createStore } from 'vuex';
import axios from 'axios';

// axios default
axios.defaults.baseURL = 'http://192.168.1.101:8000/highlighter/api';
// axios.defaults.baseURL = 'http://127.0.0.1:8000/highlighter/api';
axios.defaults.headers.post['Content-Type'] = 'application/json';
axios.defaults.headers.Accept = 'application/json; indent=4';
axios.defaults.timeout = 0;

export default createStore({
  state: {
    loading: false,
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
    // mutation to update the loading state.
    updateLoading(state, payload) {
      state.loading = payload.status;
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
    // action to fetch languages and then commit the mutation for all available languages.
    fetchLanguages(context) {
      axios.get('/options/languages/')
        .then((response) => context.commit('setLanguagesOptions', { languages: response.data.result }))
        .catch((error) => console.log(error.response));
    },
    // action to fetch and commit mutation for all available formats.
    fetchFormats(context) {
      axios.get('/options/formats/')
        .then((response) => context.commit('setFormatsOptions', { formats: response.data.result }))
        .catch((error) => console.log(error.response));
    },
    // action to fetch and commit mutation for all available styles.
    fetchStyles(context) {
      axios.get('/options/styles/')
        .then((response) => context.commit('setStylesOptions', { styles: response.data.result }))
        .catch((error) => console.log(error.response));
    },
    // action to commit the mutation to update the highlight objects data.
    highlightDetails(context, payload) {
      context.commit('toHighlight', payload);
    },
    // action to highlight the code.
    async highlightCode(context, payload) {
      // first, set the loading state to true, by committing the
      // updateLoading mutation and passing a status: true as payload.
      context.commit('updateLoading', { status: true });
      // then dispatch the highlightDetails action to update the
      // highlight object states, passing payload.highlight
      // data as its payload.
      await context.dispatch('highlightDetails', payload.highlight);
      // then get the highlight object data as the data to be sent
      // along side the post request.
      // NOTE: i used getters :).
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
          // then set the loading state back to false by commiting the
          // updateLoading mutation passing 'status: false' as its payload.
          context.commit('updateLoading', { status: false });
        })
        .catch((error) => {
          // if a request error occures, make sure to set the loading state back
          // to false and handle the error.
          context.commit('updateLoading', { status: false });
          console.log(error.response);
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
    // getter to get the loading state.
    getLoading(state) { return state.loading; },
    // getter to get the highlighted code result.
    getHighlighted(state) { return state.highlighted.result; },
  },
  // ###############
  // STATE MODULES
  // ###############
  modules: {
  },
});
