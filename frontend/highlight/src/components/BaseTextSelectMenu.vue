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
      <!-- base menu, activated with dropdown button -->
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
          :position="position"
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
    position: { type: String, required: false },
    label: { type: String, required: false, default: 'label' },
    placeholder: { type: String, required: true },
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
      // it also emits an event along side the selected option.
      this.$emit('option-selected', item);
      // when a menu option is selected, close the menu.
      this.menu = false;
    },
    toggleMenuBtn(value) {
      // this method is called when the 'toggle-menu-btn' event is captured from
      // the BaseInputDrop component this set the menu data object o true/false
      // that is show/hide.
      this.menu = value;
    },
  },
};
</script>
