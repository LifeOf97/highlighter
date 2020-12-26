<template>
<!-- eslint-disable max-len -->
    <div
      class="absolute top-0 mt-16 w-40 h-56 overflow-y-auto bg-white dark:bg-blueGray-800 rounded-md shadow-white-xl z-10">
      <ul>
        <li
          v-for="(item, index) in filterOptions"
          :key="index"
          :class="[selected === item ? 'bg-teal-200 dark:bg-blueGray-600' : 'bg-transparent']"
          class="block hover:bg-teal-200 dark:hover:bg-blueGray-600">
            <button
              type="button"
              @click="optionSelected(item)"
              class="inline-flex focus:outline-none justify-between items-center w-full h-full px-2 py-1 text-left">
                <span class="text-gray-800 dark:text-gray-400 text-base font-medium truncate">{{item}}</span>
                <i :class="[selected === item ? 'text-black' : 'text-transparent']" class="fas fa-check text-md"></i>
            </button>
        </li>
      </ul>
    </div>
</template>

<script>
export default {
  name: 'BaseMenu',
  inheritAttrs: false,
  props: {
    options: { type: Array, required: true },
    filter: { type: String, required: false },
    // position: { type: String, required: false },
  },
  emits: ['option-selected'],
  data() {
    return {
      selected: '',
    };
  },
  computed: {
    filterOptions() {
      // return filtered options containing the supplied string
      return this.options.filter((item) => item.toLowerCase().indexOf(this.filter.toLowerCase()) !== -1);
    },
  },
  methods: {
    optionSelected(item) {
      // method called when an option is clicked. This updates the selected data object
      // and also emits an event along side the option selected.
      this.selected = item;
      this.$emit('option-selected', item);
    },
  },
};
</script>
