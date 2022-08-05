<script setup>
/* eslint-disable */
import IconCheck from './icons/IconCheck.vue';
</script>

<template>
  <main class="w-full">

    <div class="w-full">

        <label for="label" class="text-slate-600 font-medium">{{label}}</label>

        <div class="relative">
            <input
                type="text"
                :id="label"
                :name="label"
                :placeholder="placeholder"
                class="w-full bg-transparent text-xs p-2 rounded-md border border-slate-600 placeholder-slate-600 hover:border-slate-400 md:text-sm" />

            <!-- start of drop menu  -->
            <div class="absolute top-10 right-0 w-full h-64 bg-white rounded-md overflow-y-auto shadow-xl">
                <button v-for="opt in [1,2,3,4,5,6,7,8,9]" :key="opt" type="button" class="w-full p-2 flex items-center justify-between bg-transparent transition-all duration-200 group hover:bg-cyan-500">
                    <p class="text-slate-900 text-xs font-normal transition-all duration-200 group-hover:text-white md:text-sm">Text</p>
                    <IconCheck class="w-7 h-7 fill-transparent transition-all duration-200 group-hover:fill-white" />
                </button>
            </div>
            <!-- end of drop menu  -->

        </div>
    </div>


  </main>
</template>