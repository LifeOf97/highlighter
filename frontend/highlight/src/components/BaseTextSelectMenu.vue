<template>
<!-- eslint-disable max-len -->
    <div id="text-select-menu" class="relative">
      <!-- base input with dropdown button -->
      <base-input-drop
        :label="label"
        :placeholder="placeholder"
        :menuValue="menu"
        v-model="selected"
        @toggle-menu-btn="toggleMenuBtn"
        @focusin="menu = true"/>
      <!-- base menu, activated with dropdown button or when input is focused -->
      <transition
        name="slide-menu"
        enter-from-class="-translate-y-3 opacity-0"
        enter-to-class=""
        enter-active-class="transition transform duration-200"
        leave-from-class=""
        leave-to-class="-translate-y-3 opacity-0"
        leave-active-class="transition transform duration-200">
        <base-menu
          v-if="menu"
          :options="options"
          :filter="selected"
          @option-selected="menuOptionSelected" />
      </transition>
    </div>
</template>

<script>
import BaseInputDrop from './BaseInputDrop.vue';
import BaseMenu from './BaseMenu.vue';

export default {
  name: 'BaseTextSelectMenu',
  props: {
    options: { type: Array, required: true },
    placeholder: { type: String, required: true },
    label: { type: String, required: false, default: 'label' },
  },
  emits: ['option-selected'],
  components: { BaseInputDrop, BaseMenu },
  data() {
    return {
      menu: false,
      selected: '',
    };
  },
  methods: {
    menuOptionSelected(item) {
      // this method is called when an 'option-selected' event emitted from the
      // BaseMenu component is captured.
      this.selected = item;
      // it also emits an event passing in the selected option.
      this.$emit('option-selected', this.selected);
      // when a menu option is selected, close the menu.
      this.menu = false;
    },
    toggleMenuBtn(value) {
      // this method is called when the 'toggle-menu-btn' event is captured from
      // the BaseInputDrop component. This sets the menu data object to true/false
      // which toggles the show/hide state.
      this.menu = value;
      // it also emits an event passing in the selected option.
      this.$emit('option-selected', this.selected);
    },
  },
};
</script>
