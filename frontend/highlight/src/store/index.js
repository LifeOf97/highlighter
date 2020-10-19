import { createStore } from 'vuex';
import axios from 'axios';

// axios default
axios.defaults.baseURL = 'http://192.168.1.101:8000/highlighter/api/';
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
    // mutation to update the highlight objects state.
    toHighlight(state, payload) {
      state.highlight.code = payload.code;
      state.highlight.style = payload.style;
      state.highlight.format = payload.format;
      state.highlight.language = payload.language;
    },
    updateHighlighted(state, payload) {
      state.highlighted.result = payload.highlighted;
    },
  },
  actions: {
    // action to fetch and commit mutation for all available languages.
    fetchLanguages(context) {
      axios.get('options/languages/')
        .then((response) => context.commit('setLanguagesOptions', { languages: response.data.result }))
        .catch((error) => console.log(error));
    },
    // action to fetch and commit mutation for all available formats.
    fetchFormats(context) {
      axios.get('options/formats/')
        .then((response) => context.commit('setFormatsOptions', { formats: response.data.result }))
        .catch((error) => console.log(error));
    },
    // action to fetch and commit mutation for all available styles.
    fetchStyles(context) {
      axios.get('options/styles/')
        .then((response) => context.commit('setStylesOptions', { styles: response.data.result }))
        .catch((error) => console.log(error));
    },
    // action to update the highlight objects data.
    highlightDetails(context, payload) {
      context.commit('toHighlight', payload);
    },
    // action to highlight the code.
    async highlightCode(context, payload) {
      // first, set the loading state to true, by committing the
      // updateLoading mutation and passing the payload.loading
      // data as the payload.
      context.commit('updateLoading', payload.loading);
      // then dispatch the highlightDetails action to update the
      // highlight object states, passing the payload.highlight
      // data as its payload.
      await context.dispatch('highlightDetails', payload.highlight);
      // then get the highlight object datas as the data to be sent
      // along side the post request.
      // NOTE: i made used of getters, it could be more simple :).
      const data = {
        code: context.getters.getHighlightDetails.code,
        style: context.getters.getHighlightDetails.style,
        format: context.getters.getHighlightDetails.format,
        language: context.getters.getHighlightDetails.language,
      };
      // then make a post request to the highlighter api backend,
      // passing the data as payload to be highlighted.
      await axios.post('highlight/', data)
        .then((response) => {
          // on success, commit the updateHighlighted mutation along
          // side the its payload data to set the highlighted.result state to.
          context.commit('updateHighlighted', { highlighted: response.data.result.data });
          console.log(response.data);
          // then set the loading state back to false by commiting
          // the updateLoading mutation passing the false as its payload.
          context.commit('updateLoading', { status: false });
        })
        .catch((error) => {
          // if a request error occures, make sure to set the loading state back
          // to false.
          context.commit('updateLoading', { status: false });
          console.log(error.response);
        });
    },
  },
  getters: {
    // getter for state languages.
    getLanguages(state) { return state.options.languages; },
    // getter for state formats.
    getFormats(state) { return state.options.formats; },
    // getter for state styles.
    getStyles(state) { return state.options.styles; },
    // getter for state highlight.
    getHighlightDetails(state) { return state.highlight; },
  },
  modules: {
  },
});
