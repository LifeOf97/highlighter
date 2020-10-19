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
        :appear="true"
        enter-from-class="-translate-y-3"
        enter-to-class=""
        enter-active-class="transition transform duration-200"
        leave-from-class=""
        leave-to-class="-translate-y-3"
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
  name: 'TextSelectMenu',
  props: {
    options: { type: Array, required: true },
    label: { type: String, required: false, default: 'label' },
    placeholder: { type: String, required: false, default: '---' },
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
      this.selected = item;
      // emit an event along side the selected option.
      this.$emit('option-selected', item);
      // when a menu option is selected, close the menu.
      // this.menu = false;
    },
    toggleMenuBtn(value) {
      // event captured from the BaseInputDrop component
      this.menu = value;
    },
  },
};
</script>
