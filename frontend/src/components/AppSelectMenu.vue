<script setup>
/* eslint-disable */
import { onMounted, ref } from "vue";
import IconCheck from './icons/IconCheck.vue';
import IconUnfoldMore from './icons/IconUnfoldMore.vue';
import IconUnfoldLess from './icons/IconUnfoldLess.vue';

// props
const props = defineProps({
    modelValue: {type: String},
    label: {type: String, default: 'Label'},
    placeholder: {type: String}
})

// emits
const emits = defineEmits(["update:modelValue"])

// refs
const openMenu = ref(false)
const root = ref(null)

// methods
const pop = (value) => {
    console.log(value)
}

const closeMenu = (e) => {
    if (!root.value.contains(e.target)) {
        openMenu.value = false;
    }
}

// hooks
onMounted(() => {
    document.addEventListener("click", closeMenu)
})
</script>

<template>
  <main ref="root" class="w-full">

    <div class="w-full flex flex-col gap-1">

        <label for="label" class="text-xs text-slate-200 font-normal md:text-sm">{{label}}</label>

        <div class="relative">
            <div :class="openMenu ? 'border-slate-200':'border-slate-600'" class="relative group rounded-md border transition-all duration-200 hover:border-slate-200">

                <input
                    type="text"
                    :id="label"
                    :name="label"
                    :placeholder="placeholder"
                    :value="props.modelValue"
                    @focus="openMenu = true"
                    @input="$emit('update:modelValue', $event.target.value)"
                    class="w-full bg-transparent text-xs text-slate-200 p-2 placeholder-slate-600 focus:outline-none" />

                <div class="absolute right-0 top-1">
                    <IconUnfoldLess v-if="openMenu" :class="openMenu ? 'fill-slate-200':'fill-slate-600'" class="w-5 h-5 transition-all duration-200 group-hover:fill-slate-200" />
                    <IconUnfoldMore v-else :class="openMenu ? 'fill-slate-200':'fill-slate-600'" class="w-5 h-5 transition-all duration-200 group-hover:fill-slate-200" />
                </div>
            </div>
            
            <!-- start of drop menu  -->
            <transition
                name="slide-menu"
                enter-from-class="-translate-y-10 opacity-0"
                enter-active-class="transition-all duration-200"
                leave-to-class="-translate-y-10 opacity-0"
                leave-active-class="transition-all duration-200">
                <div v-if="openMenu" class="absolute top-10 right-0 w-full h-40 bg-white rounded-md overflow-y-auto shadow-inner border-slate-200 z-20">
                    <button @click.prevent="pop(opt)" v-for="opt in [1,2,3,4,5,6,7,8,9]" :key="opt" type="button" class="w-full cursor-pointer p-2 flex items-center justify-between bg-transparent transition-all duration-200 group hover:bg-cyan-500">
                        <p class="text-slate-900 text-xs font-normal transition-all duration-200 group-hover:text-white md:text-sm">Text</p>
                        <IconCheck class="w-7 h-7 fill-transparent transition-all duration-200 group-hover:fill-white" />
                    </button>
                </div>
            </transition>
            <!-- end of drop menu  -->

        </div>
    </div>


  </main>
</template>