<script setup>
/* eslint-disable */
import { RouterLink } from 'vue-router';
</script>

<template>
  <main>
    <RouterLink :to="{name: 'home'}">
        <p class="font-black text-xl text-slate-700 dark:text-slate-200 md:text-2xl">JustHighLight</p>
    </RouterLink>
  </main>
</template>