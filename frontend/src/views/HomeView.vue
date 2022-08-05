<script setup>
/* eslint-disable */
import AppHomeHero from '../components/AppHomeHero.vue';
import AppHomeCodeEditor from '../components/AppHomeCodeEditor.vue';
import AppHomePoints from '../components/AppHomePoints.vue';
import AppHomeFooter from '../components/AppHomeFooter.vue';
</script>

<template>
  <main class="w-full h-full bg-white selection:bg-rose-500 selection:text-white">

    <header class="w-full bg-cyan-300">
      <AppHomeHero />
    </header>

    <aside class="relative h-full">
      <AppHomeCodeEditor />
    </aside>

    <section>
      <AppHomePoints />
    </section>

    <footer>
      <AppHomeFooter />
    </footer>

  </main>
</template>
