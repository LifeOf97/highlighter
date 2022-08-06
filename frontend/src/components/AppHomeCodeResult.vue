<script setup>
/* eslint-disable */
import { computed } from 'vue';
import { useHighlighterStore } from '../stores/highlight.js';
import IconLongLeft from './icons/IconLongLeft.vue';

// emits
const emits = defineEmits(["updateComponent"])

// stores
const highlighterStore = useHighlighterStore()

// computed
const code = computed(() => {
  try {
    return highlighterStore.highlighter.data.result.highlighted
  } catch (error) {
    return ""
  }
})
</script>

<template>
  <main class="-mt-20 w-11/12 mx-auto h-full bg-slate-700 shadow-slate-400 md:-mt-0 md:absolute md:-top-20 md:w-1/2 md:right-0 lg:right-10 xl:right-20">
    <div v-html="code" class="overflow-auto h-72 bg-slate-700 rounded-t-md p-4"></div>

    <div class="bg-slate-700 p-4 rounded-b-md">
      <button
        type="submit"
        @click.prevent="$emit('updateComponent', 'AppHomeCodeEditor')"
        class="text-sm group flex items-center gap-3 text-white px-4 py-2 rounded-md bg-slate-600 shadow-xl transition-all duration-200 hover:bg-slate-500 group-hover:animate-bounce md:text-sm">
          <IconLongLeft class="w-7 h-7 fill-slate-400 group-hover:animate-bounce-x" />
          <p>Editor</p>
      </button>
    </div>
  </main>
</template>