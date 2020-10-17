<template>
    <div id="text-editor" class="">
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
  props: ['modelValue'],
  inheritAttrs: false,
};
</script>
