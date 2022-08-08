<script setup>
/* eslint-disable */
import AppTopNav from '../components/AppTopNav.vue';
import AppDocsDetail from '../components/AppDocsDetail.vue';
</script>

<template>
  <main class="w-full h-full bg-white selection:bg-rose-500 selection:text-white dark:selection:bg-cyan-500">

    <header class="w-full bg-cyan-300 dark:bg-slate-900">
      <div class="w-11/12 mx-auto lg:w-10/12">
        <AppTopNav />
      </div>
    </header>

    <section class="w-full dark:bg-slate-800">
      <div class="w-11/12 mx-auto pt-10 md:w-7/12">
        <AppDocsDetail />
      </div>
    </section>

  </main>
</template>
