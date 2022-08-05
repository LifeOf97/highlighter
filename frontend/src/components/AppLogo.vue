<script setup>
/* eslint-disable */
import { RouterLink } from 'vue-router';
</script>

<template>
  <main>
    <RouterLink :to="{name: 'home'}">
        <p class="font-black text-xl text-slate-500 dark:text-white md:text-2xl">JustHighLight</p>
    </RouterLink>
  </main>
</template>