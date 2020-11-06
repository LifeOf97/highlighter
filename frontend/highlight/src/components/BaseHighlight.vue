<template>
  <div v-bind="$attrs">
    <slot v-if="loading" name="sourcecode">
    </slot>
    <div v-else v-html="highlighted"></div>
    </div>
</template>

<script>
import axios from 'axios';

const highlightApi = 'http://127.0.0.1:8000/highlighter/api/highlight/';

export default {
  name: 'BaseHighlight',
  props: ['language'],
  inheritAttrs: false,
  data() {
    return {
      loading: true,
      highlighted: '',
      highlight: {
        code: this.$slots.sourcecode()[0].children.trim(),
        style: 'paraiso-dark',
        format: 'html',
      },
    };
  },
  mounted() {
    this.logSom();
    this.quickHighlight();
  },
  methods: {
    // this method is used to highlight code snippet.
    async quickHighlight() {
      // first set loading to true
      this.loading = true;
      // then get the code snippet and its values needed for highlighting.
      const data = {
        code: this.highlight.code,
        style: this.highlight.style,
        getFormat: this.highlight.format,
        language: this.language,
      };
      // then make a post request to the highlighter api endpoint along side the
      // data to be highlighted.
      await axios.post(highlightApi, data)
        // get the highlighted data fron the successfull response and assign it to
        // the highlighted data object and also set the loading data to false.
        .then((response) => {
          this.highlighted = response.data.result.data;
          this.loading = false;
        })
        // if any error what so ever, console that shit for debuging.
        .catch((error) => { console.log(error.response); });
    },
    logSom() {
      console.log(this.$slots.sourcecode()[0].children.trim());
    },
  },
};
</script>
