<script setup>
/* eslint-disable */
import AppLogo from './AppLogo.vue';
import { RouterLink } from 'vue-router';
import IconTag from './icons/IconTag.vue';
import IconGithub from './icons/IconGithub.vue';
</script>

<template>
  <main class="w-full py-7 flex items-center justify-between">

    <div class="flex items-center">
        <AppLogo />
    </div>

    <div class="flex items-center gap-2 divide-x divide-slate-600">

        <div class="flex items-center gap-2 mr-4">
            <div class="flex items-center gap-1">
                <IconTag class="w-6 h-6 fill-slate-500" />
                <p class="text-sm text-slate-600 font-normal">Version 1.0.0</p>
            </div>
        </div>

        <div class="pl-4 flex items-center gap-2">
            <RouterLink :to="{name: 'docs'}" class="text-slate-900 font-medium px-4 py-1 rounded-md bg-transparent transition-all duration-200 hover:bg-white hover:text-rose-500">
                Docs
            </RouterLink>

            <a href="https://github.com/realestKMA/highlighter" target="_blank" rel="noopener noreferrer" class="relative group">
                <IconGithub class="absolute top-0 w-6 h-6 fill-slate-400 z-10" />
                <IconGithub class="w-6 h-6 fill-rose-500 group-hover:animate-ping" />
            </a>
        </div>

    </div>

  </main>
</template>