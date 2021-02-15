<template>
<!-- eslint-disable max-len -->
    <div class="inline-flex flex-col">
      <!-- base input label -->
      <label class="font-black flex-initial text-sm text-gray-400 dark:text-gray-600">{{label}}</label>
      <!-- base input field and dropdown button -->
      <div
        :class="[isFocused ? 'border-gray-100 dark:border-gray-600' : 'border-gray-400']"
        class="relative border rounded-md mt-1 p-1 w-40 flex items-center hover:border-gray-100 dark:hover:border-gray-600">
        <input
          type="text"
          autocomplete="off"
          :value="modelValue"
          @input="emitValue"
          @focusin="focusin"
          @focusout="focusout"
          aria-haspopup="listbox"
          aria-required="true"
          class="bg-transparent text-sm text-white dark:text-gray-800 w-32 font-normal focus:outline-none placeholder-gray-400 dark:placeholder-gray-600" />
          <button @click="isActive = !isActive, toggleMenuBtn(isActive)" class="mb-1 absolute w-6 right-0 focus:outline-none">
            <i :class="[isActive ? 'text-gray-100 dark:text-gray-600' : 'text-gray-400']" class="fas fa-sort-down text-xl leading-4 hover:text-gray-100 dark:hover:text-gray-600"></i>
          </button>
      </div>
    </div>
</template>

<script>
export default {
  name: 'BaseInputDrop',
  props: {
    modelValue: { type: String, required: false },
    modelModifiers: { default: () => ({}) },
    label: { type: String, required: false, default: 'Label' },
    menuValue: { type: Boolean, required: false },
  },
  emits: ['input', 'focusin', 'focusout', 'toggle-menu-btn', 'update:modelValue'],
  data() {
    return {
      isActive: false,
      isFocused: false,
    };
  },
  watch: {
    menuValue(newValue) {
    // we watch for changes in the menuValue prop so as to react to changes
    // and update the isActive data object with the newvalue.
      this.isActive = newValue;
    },
  },
  methods: {
    emitValue(e) {
      let { value } = e.target;
      if (this.modelModifiers.lower) { // if the input binding has an lower modifier.
        value = value.toLowerCase();
      } else if (this.modelModifiers.capitalize) { // if the input binding has an capitalize modifier.
        value = value.charAt(0).toUpperCase() + value.slice(1).toLowerCase();
      } else if (this.modelModifiers.upper) { // if the input binding has an upper modifier.
        value = value.toUpperCase();
      }
      this.$emit('update:modelValue', value);
    },
    toggleMenuBtn(value) {
      // this method emits an event to toggle the menu option if available
      // to either display the menu or hide it by passing in the the current
      // state of the isActive data object value.
      this.$emit('toggle-menu-btn', value);
    },
    focusin() {
      // this method emits an event if the input field is focused-in and
      // sets the isFocused data object to true.
      this.$emit('focusin');
      this.isFocused = true;
    },
    focusout() {
      // this method emits an event if the input field is out of focus and
      // sets the isFocused data object to false.
      this.$emit('focusout');
      this.isFocused = false;
    },
  },
};
</script>
