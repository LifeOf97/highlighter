<script setup>
/* eslint-disable */
import { ref, computed, onBeforeMount } from 'vue';
import { useHighlighterStore } from '../stores/highlight';
import AppHomeHero from '../components/AppHomeHero.vue';
import AppHomeCodeEditor from '../components/AppHomeCodeEditor.vue';
import AppHomePoints from '../components/AppHomePoints.vue';
import AppHomeFooter from '../components/AppHomeFooter.vue';
import AppHomeCodeResult from '../components/AppHomeCodeResult.vue';

// stores
const highlighterStore = useHighlighterStore()

// datas
const tabs = {AppHomeCodeEditor, AppHomeCodeResult}

// refs
const tab = ref('AppHomeCodeEditor')

// computed
const activeComponent = computed(() => {
  return tabs[tab.value]
})

// hooks
onBeforeMount(() => {
  highlighterStore.getLanguages()
  highlighterStore.getFormats()
  highlighterStore.getStyles()
})
</script>

<template>
  <main class="w-full h-full bg-white selection:bg-rose-500 selection:text-white dark:selection:bg-cyan-500 dark:bg-slate-800">

    <header class="w-full bg-cyan-300 dark:bg-slate-900">
      <AppHomeHero />
    </header>

    <aside class="relative h-full">
      <KeepAlive>
        <component :is="activeComponent" @update-component="(n) => tab = n"></component>
      </KeepAlive>
    </aside>

    <section>
      <AppHomePoints />
    </section>

    <footer>
      <AppHomeFooter />
    </footer>

  </main>
</template>
