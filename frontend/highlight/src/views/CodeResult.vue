<template>
<!-- eslint-disable max-len -->
    <div class="w-full h-full shadow-2xl rounded-md overflow-hidden bg-gray-800">
      <div v-if="getLoading">
        Loading...
      </div>
      <div
        v-else
        v-html="getHighlight.result"
        class="px-3 py-2"></div>
    </div>
</template>

<script>
import { mapGetters, mapActions } from 'vuex';

export default {
  name: 'CodeResult',
  beforeMount() {
    this.highlightCode();
  },
  computed: {
    ...mapGetters(['getHighlighted', 'getLoading']),
  },
  methods: {
    ...mapActions(['highlightCode']),
  },
};
</script>
