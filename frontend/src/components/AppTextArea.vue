<script setup>
/* eslint-disable */

// props
const props = defineProps({
    modelValue: { type: String },
    placeholder: { type: String, default: 'Enter your value...' },
    required: { type: Boolean, default: true },
})

// emits
const emits = defineEmits(["update:modelValue"])
</script>

<template>
    <textarea
        :value="modelValue"
        @input="$emit('update:modelValue', $event.target.value)"
        :required="required"
        v-bind="$attrs"
        :placeholder="placeholder"
        class="w-full h-full resize-none text-white text-xs font-normal bg-slate-600 p-4 focus:outline-none md:text-sm"
    ></textarea>
</template>
