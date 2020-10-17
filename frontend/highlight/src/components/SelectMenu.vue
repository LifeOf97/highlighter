<template>
<!-- eslint-disable max-len -->
    <div>
        <label
          id="listbox-label"
          class="text-sm text-gray-500 font-medium">{{labelName}}:</label>
        <div class="relative w-32">
          <div class="w-full">
            <button
              type="button"
              @click="isActive = !isActive"
              :class="[isActive ? 'border-white' : 'border-gray-600']"
              class="inline-flex items-center justify-between w-full rounded-md py-1 focus:outline-none border mt-1 group hover:border-white transition duration-300">
                <span class="px-2 truncate text-sm text-gray-300 font-normal">{{selected}}</span>
                <i
                  :class="[isActive ? 'text-white' : 'text-gray-600']"
                  class="fas fa-sort-down fa-md mb-1 px-2 group-hover:text-white transition duration-300"></i>
            </button>
          </div>
          <!-- slide menu -->
          <transition
            name="slide"
            enter-from-class="-translate-y-3 opacity-0"
            enter-to-class=""
            enter-active-class="transition transform duration-300"
            leave-from-class=""
            leave-to-class="-translate-y-3 opacity-0"
            leave-active-class="transition transform duration-300">
            <ul v-if="isActive" class="absolute w-full h-32 left-0 top-0 mt-10 shadow-xl rounded-lg bg-white overflow-y-auto z-10">
              <li
                v-for="(item, index) in items"
                :key="index"
                :class="[selected === item ? 'bg-teal-200' : 'bg-transparent']"
                class="hover:bg-teal-200">
                  <button
                      @click="selectOption(item)"
                      type="button"
                      class="w-full px-2 py-1 flex justify-between items-center focus:outline-none">
                    <span class="text-sm font-normal">{{item}}</span>
                    <i
                      :class="[selected === item ? 'text-pink-600' : 'text-transparent']"
                      class="fas fa-check text-sm"></i>
                  </button>
              </li>
            </ul>
          </transition>
        </div>
    </div>
</template>

<script>
export default {
  name: 'SelectMenu',
  props: {
    options: { type: Array, required: false },
    labelName: { type: String, required: true },
  },
  data() {
    return {
      selected: 'Python',
      isActive: false,
      items: ['kool', 'kat', 'swerve', 'say', 'so', 'python'],
    };
  },
  methods: {
    selectOption(value) {
      this.selected = value;
      this.isActive = false;
    },
  },
};
</script>
