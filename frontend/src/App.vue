<script setup>
/* eslint-disable */
import { onMounted, ref } from 'vue';
import { RouterView } from 'vue-router'
import { useHighlighterStore } from './stores/highlight.js';

// refs
const getTheme = ref(localStorage.theme)

// stores
const highlighterStore = useHighlighterStore()

onMounted(() => {
  if (localStorage.theme === 'dark' || (!('theme' in localStorage) && window.matchMedia('(prefers-color-scheme: dark)').matches)) {
    highlighterStore.theme = 'dark'
  } else {
    highlighterStore.theme = 'light'
  }
})
</script>

<template>
  <main :class="highlighterStore.theme">
    <RouterView />
  </main>
</template>
