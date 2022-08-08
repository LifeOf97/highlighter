<script setup>
/* eslint-disable */
import IconGithub from './icons/IconGithub.vue';
import IconTwitter from './icons/IconTwitter.vue';
import IconLinkedin from './icons/IconLinkedin.vue';

// datas
const year = new Date().getFullYear()
</script>

<template>
    <main class="w-full h-full border-t border-slate-200 py-7 dark:border-slate-700">
        <div class="w-11/12 mx-auto flex flex-col gap-3 items-center justify-between md:flex-row md:gap-0 md:w-10/12">

            <div class="order-1 text-xs text-slate-500 font-medium">
                <p>JustHighLight &copy; {{ year }}</p>
            </div>

            <div class="order-3 flex items-center gap-5">
                <a href="https://github.com/realestKMA" target="_blank" rel="noopener noreferrer" class="relative group">
                    <IconGithub class="absolute top-0 w-6 h-6 fill-slate-400 z-10" />
                    <IconGithub class="w-6 h-6 fill-rose-500 dark:fill-cyan-500 group-hover:animate-ping" />
                </a>
                <a href="https://twitter.com/realestKMA" target="_blank" rel="noopener noreferrer" class="relative group">
                    <IconTwitter class="absolute top-0 w-6 h-6 fill-slate-400 z-10" />
                    <IconTwitter class="w-6 h-6 fill-rose-500 dark:fill-cyan-500 group-hover:animate-ping" />
                </a>
                <a href="https://linkedin.com/in/realestKMA/" target="_blank" rel="noopener noreferrer" class="relative group">
                    <IconLinkedin class="absolute top-0 w-6 h-6 fill-slate-400 z-10" />
                    <IconLinkedin class="w-6 h-6 fill-rose-500 dark:fill-cyan-500 group-hover:animate-ping" />
                </a>
            </div>

            <div class="order-2 flex gap-2 items-center text-xs text-slate-500 md:order-3">
                <p>Developed by the</p>
                <a href="https://github.com/realestKMA" target="_blank" class="text-blue-500 hover:text-blue-600">
                    RealestKMA
                </a>
                <p>from the</p>
                <p class="font-bold">234
                    <flag iso="ng" />
                </p>
            </div>

        </div>
    </main>
</template>