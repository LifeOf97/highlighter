<script setup>
/* eslint-disable */
import AppSelectMenu from './AppSelectMenu.vue';
</script>

<template>
  <main class="bg-slate-800 -mt-20 w-11/12 mx-auto h-96 rounded-lg shadow-slate-400 md:-mt-0 md:absolute md:-top-20 md:w-1/2 md:right-0 lg:right-10 xl:right-20">

    <div class="w-full flex flex-col">

      <div class="w-full flex flex-col gap-3 p-4 border-b border-slate-700 sm:flex-row lg:gap-7">
        <AppSelectMenu label="Language" />
        <AppSelectMenu label="Format" />
        <AppSelectMenu label="Style" />
      </div>

    </div>

  </main>
</template>