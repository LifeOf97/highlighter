<template>
<!-- eslint-disable max-len -->
    <div class="w-full shadow-2xl rounded-md h-70 flex flex-col justify-between bg-blueGray-700 dark:bg-blueGray-300">
      <div v-if="getLoading" class="h-full w-full flex items-center justify-center">
        <i class="fas fa-spinner text-4xl text-white animate-spin"></i>
      </div>
      <div v-else class="overflow-y-auto overscroll-x-auto h-68">
        <div v-html="getHighlighted"></div>
      </div>
      <div class="w-full flex justify-start items-center p-2 bg-blueGray-700 dark:bg-blueGray-200">
        <button
          type="submit"
          @click="$emit('update:component', 'CodeEditor')"
          class="px-2 py-1 bg-gradient-to-tr from-blue-600 via-pink-500 to-red-500 shadow-lg rounded-lg inline-flex place-items-center space-x-2
          hover:from-red-500 hover:via-pink-500 hover:to-blue-600 transition duration-500 ease-out focus:outline-none">
            <i class="fas fa-long-arrow-alt-left text-lg text-black"></i>
            <span class="font-semibold text-base text-white">Editor</span>
          </button>
      </div>
    </div>
</template>

<script>
import { mapGetters } from 'vuex';

export default {
  name: 'CodeResult',
  data() {
    return {
      state: true,
    };
  },
  computed: {
    ...mapGetters(['getHighlighted', 'getLoading']),
  },
};
</script>
