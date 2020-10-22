<template>
<!-- eslint-disable max-len -->
    <div id="text-editor">
        <textarea
          v-bind="$attrs"
          :value="modelValue"
          @input="$emit('update:modelValue', $event.target.value)">
        </textarea>
    </div>
</template>

<script>
export default {
  name: 'TextEditor',
  inheritAttrs: false,
  props: {
    modelValue: { type: String, required: false },
  },
};
</script>
