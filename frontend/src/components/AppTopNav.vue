<script setup>
/* eslint-disable */
import { RouterLink, useRoute } from 'vue-router';
import { ref, onMounted } from 'vue';
import { useHighlighterStore } from '../stores/highlight';
import AppLogo from './AppLogo.vue';
import IconTag from './icons/IconTag.vue';
import IconGithub from './icons/IconGithub.vue';
import IconSun from './icons/IconSun.vue';
import IconMoon from './icons/IconMoon.vue';
import IconSystem from './icons/IconSystem.vue';

// stores
const highlighterStore = useHighlighterStore()

// route
const route = useRoute()

// refs
const getTheme = ref(localStorage.theme)
const openTheme = ref(false)
const root = ref("")

// methods
const changeTheme = (value) => {
    highlighterStore.theme = value
    localStorage.theme = value
    getTheme.value = value
    openTheme.value = false
}

const closeTheme = (e) => {
    if (!root.value.contains(e.target)) {
        openTheme.value = false
    }
}

// hooks
onMounted(() => {
    document.addEventListener('click', closeTheme)
})
</script>

<template>
  <main ref="root" class="w-full py-7 flex items-center justify-between">

    <div class="flex items-center">
        <AppLogo />
    </div>

    <div class="flex items-center gap-2 divide-x divide-slate-600">

        <div class="flex items-center gap-4 mr-2">
            <div class="hidden items-center gap-1 md:flex">
                <IconTag class="w-6 h-6 fill-slate-400" />
                <p class="text-sm text-slate-600 font-normal dark:text-slate-400">Version 1.0.0</p>
            </div>
            
            <RouterLink v-if="route.name == 'home'" :to="{name: 'docs'}" class="text-slate-900 font-medium  transition-all duration-200 hover:text-white dark:text-slate-400 dark:hover:text-white">
                Docs
            </RouterLink>
            <RouterLink v-else-if="route.name == 'docs'" :to="{name: 'home'}" class="text-slate-900 font-medium  transition-all duration-200 hover:text-white dark:text-slate-400 dark:hover:text-white">
                Home
            </RouterLink>
        </div>

        <div class="pl-4 flex items-center gap-4">

            <div class="relative">
                <button type="button" @click="openTheme = !openTheme" class="flex items-center focus:outline-none">
                    <IconSun v-if="getTheme === 'light'" :class="openTheme ? 'fill-white':'fill-slate-400'" class="w-6 h-6 hover:fill-white" />
                    <IconMoon v-else-if="getTheme === 'dark'" :class="openTheme ? 'fill-white':'fill-slate-400'" class="w-6 h-6 hover:fill-white" />
                    <IconSystem v-else :class="openTheme ? 'fill-white':'fill-slate-400'" class="w-6 h-6 hover:fill-white" />
                </button>

                <transition
                    name="theme"
                    enter-from-class="scale-0 opacity-0"
                    enter-active-class="transition-all duration-200"
                    leave-to-class="scale-0 opacity-0"
                    leave-active-class="transition-all duration-200">
                        <div v-if="openTheme" class="absolute top-9 -left-10 w-28 flex flex-col bg-white rounded-md overflow-hidden shadow-xl z-20">
                            <button type="button" @click.prevent="changeTheme('light')" :class="getTheme == 'light' ? 'bg-cyan-200':'bg-transparent'" class="group flex items-center gap-3 px-2 py-2 hover:bg-cyan-200">
                                <IconSun :class="getTheme == 'light' ? 'fill-white':'fill-slate-400'" class="w-5 h-5 group-hover:fill-white" />
                                <p :class="getTheme == 'light' ? 'text-white':'text-slate-500'" class="text-xs font-normal md:text-sm group-hover:text-white">Light</p>
                            </button>
                            <button type="button" @click.prevent="changeTheme('dark')" :class="getTheme == 'dark' ? 'bg-cyan-200':'bg-transparent'" class="group flex items-center gap-3 px-2 py-2 hover:bg-cyan-200">
                                <IconMoon :class="getTheme == 'dark' ? 'fill-white':'fill-slate-400'" class="w-5 h-5 fill-slate-400 group-hover:fill-white" />
                                <p :class="getTheme == 'dark' ? 'text-white':'text-slate-500'" class="text-xs font-normal md:text-sm group-hover:text-white">Dark</p>
                            </button>
                            <button type="button" @click.prevent="changeTheme('system')" :class="getTheme == 'system' ? 'bg-cyan-200':'bg-transparent'" class="group flex items-center gap-3 px-2 py-2 hover:bg-cyan-200">
                                <IconSystem :class="getTheme == 'system' ? 'fill-white':'fill-slate-400'" class="w-5 h-5 fill-slate-400 group-hover:fill-white" />
                                <p :class="getTheme == 'system' ? 'text-white':'text-slate-500'" class="text-xs font-normal md:text-sm group-hover:text-white">System</p>
                            </button>
                        </div>
                </transition>
            </div>

            <a href="https://github.com/realestKMA/highlighter" target="_blank" rel="noopener noreferrer" class="relative group">
                <IconGithub class="absolute top-0 w-6 h-6 fill-slate-400 z-10" />
                <IconGithub class="w-6 h-6 fill-slate-500 group-hover:animate-ping dark:fill-cyan-500" />
            </a>
        </div>

    </div>

  </main>
</template>