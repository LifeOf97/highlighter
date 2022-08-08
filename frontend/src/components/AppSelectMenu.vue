<script setup>
/* eslint-disable */
import { onMounted, ref, computed } from "vue";
import IconCheck from './icons/IconCheck.vue';
import IconUnfoldMore from './icons/IconUnfoldMore.vue';
import IconUnfoldLess from './icons/IconUnfoldLess.vue';
import IconRefresh from "./icons/IconRefresh.vue";

// props
const props = defineProps({
    modelValue: {type: String},
    label: {type: String, default: 'Label'},
    placeholder: {type: String},
    options: {type: Array},
    required: {type: Boolean, default: true},
    loading: {type: Boolean, default: false},
    inputError: {type: String, default: null},
    inputInvalid: {type: Boolean, default: false},
    menuError: {type: String, default: null}
})

// emits
const emits = defineEmits(["update:modelValue", "refresh", "selectedOption"])

// refs
const openMenu = ref(false)
const selected = ref('')
const root = ref(null)

// computed
const filterOptions = computed(() => {
    // return filtered options containing the supplied string
    // return props.options.filter((item) => item.toLowerCase().indexOf(props.modelValue.toLowerCase()) !== -1);
    return props.options.filter((item) => item.toLowerCase().startsWith(props.modelValue.toLowerCase()));
})

// methods
const selectedOption = (option) => {
    selected.value = option
    emits('selectedOption', option)
    openMenu.value = false
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
            <div :class="openMenu ? 'border-slate-200':'border-slate-600'" class="relative group rounded-md border transition-all duration-200 hover:border-slate-200 group-invalid:bordre-red-500">

                <input
                    type="text"
                    :value="props.modelValue"
                    @input="$emit('update:modelValue', $event.target.value)"
                    :id="label"
                    :name="label"
                    :placeholder="placeholder"
                    :required="required"
                    @invalid="inputInvalid"
                    autocomplete="off"
                    @focus="openMenu = true"
                    class="w-full bg-transparent text-xs text-slate-200 p-2 placeholder-slate-600 focus:outline-none" />

                <div class="absolute right-0 top-1">
                    <IconUnfoldLess v-if="openMenu" :class="openMenu ? 'fill-slate-200':'fill-slate-600'" class="w-5 h-5 transition-all duration-200 group-hover:fill-slate-200" />
                    <IconUnfoldMore v-else :class="openMenu ? 'fill-slate-200':'fill-slate-600'" class="w-5 h-5 transition-all duration-200 group-hover:fill-slate-200" />
                </div>

            </div>
            <div v-if="inputError" class="w-full mt-2">
                <p class="text-xs text-red-500 font-normal">{{inputError}}</p>
            </div>
            
            <!-- start of drop menu  -->
            <transition
                name="slide-menu"
                enter-from-class="-translate-y-10 opacity-0"
                enter-active-class="transition-all duration-200"
                leave-to-class="-translate-y-10 opacity-0"
                leave-active-class="transition-all duration-200">
                <div v-if="openMenu" class="absolute top-10 right-0 w-full h-40 bg-white rounded-md overflow-y-auto shadow-inner border-slate-200 z-20 dark:bg-slate-200">
                    
                    <div v-if="props.loading" class="w-full h-full flex items-center justify-center">
                        <IconRefresh class="w-7 h-7 fill-slate-900 animate-spin" />
                    </div>

                    <div v-else-if="props.menuError" class="w-full h-full text-xs flex flex-col gap-1 items-center justify-center">
                        <p class="text-red-500 font-normal">{{props.menuError}}</p>
                        <button @click.prevent="$emit('refresh')" type="button" class="text-blue-500 hover:text-blue-600">Refresh</button>
                    </div>

                    <div v-else>
                        <TransitionGroup name="list">
                            <button @click.prevent="selectedOption(option)" v-for="option in filterOptions" :key="option" type="button" class="w-full cursor-pointer p-2 flex items-center justify-between bg-transparent transition-all duration-200 group hover:bg-cyan-500">
                                <p class="text-slate-900 text-xs font-normal transition-all duration-200 capitalize group-hover:text-white md:text-sm">{{option}}</p>
                                <IconCheck :class="selected == option ? 'fill-slate-900 group-hover:fill-white':'fill-transparent'" class="w-7 h-7 transition-all duration-200" />
                            </button>
                        </TransitionGroup>
                    </div>
                </div>
            </transition>
            <!-- end of drop menu  -->

        </div>
    </div>


  </main>
</template>