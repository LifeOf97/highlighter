<template>
<!-- eslint-disable max-len -->
  <div id="nav" class="relative bg-white">
    <!-- start of top nav -->
    <nav
      ref="topNav"
      id="topNav"
      :class="[navPosition ? 'shadow-xl z-20' : 'z-20']"
      class="fixed top-0 left-0 w-full bg-teal-300 transition duration-700">
      <div class="py-6 w-11/12 mx-auto flex flex-col md:flex-row md:justify-between">
        <!-- logo -->
        <div class="flex-1 flex justify-between mb-1 md:mb-0">
          <h1 class="font-black text-2xl text-black tracking-tight">JustHighlight</h1>
          <button class="md:hidden focus:outline-none">
            <i
              @click="menu = !menu"
              class="fas fa-bars text-3xl text-gray-700 hover:text-red-500 transition duration-200"></i>
          </button>
        </div>
        <!-- start of version info, documentation url, and social links -->
        <!-- this div block is hidden on small screens and can only be seen with a toggle menu button -->
        <!-- which slides down/up on click -->
        <div
          :class="[menu ? 'translate-y-0 opacity-100' : '-translate-y-24 md:translate-y-0 opacity-0 md:opacity-100']"
          class="flex-1 flex justify-center items-center bg-gray-800 absolute top-0 left-0 w-full transition transform duration-300 h-24 md:relative md:block md:bg-transparent md:h-auto">
          <!-- start of version info -->
          <div class="flex justify-center md:justify-end">
            <div
              class="flex-initial flex place-items-center space-x-2 px-3 text-gray-600 border-r border-gray-600">
              <i class="fas fa-tag text-md"></i>
              <span class="font-bold text-sm">Version 1.0.1</span>
            </div>
            <!-- end of version info -->
            <!-- start of close nav button that is only avialable on small screens when the nav bar is open -->
            <button
              type="button"
              @click="menu = false"
              class="absolute top-0 right-0 mr-6 mt-2  focus:outline-none group md:hidden">
              <i class="fas fa-times text-transparent text-2xl font-bold bg-clip-text bg-gradient-to-br from-blue-600 via-pink-500 to-red-500"></i>
            </button>
            <!-- end of close nav button -->
            <!-- start of router links to docs and back to home page -->
            <div class="flex-initial flex items-center px-3">
              <div class="group hover:bg-white transition duration-500 rounded-lg">
                <router-link
                  v-if="routeName === 'Home'"
                  :to="{name: 'Docs'}"
                  :class="'flex px-2 py-1 justify-center items-center'">
                    <span @click="menu = false" class="font-semibold text-base text-white md:text-gray-900 group-hover:text-pink-500 transition duration-500">Docs</span>
                </router-link>
                <router-link
                  v-else
                  :to="{name: 'Home'}"
                  class="font-semibold text-base text-gray-900 px-2 py-1 group-hover:text-pink-500 transition duration-500">
                    <span @click="menu = false" class="font-semibold text-base text-white md:text-gray-900 group-hover:text-pink-500 transition duration-500">Home</span>
                  </router-link>
              </div>
              <!-- end of router links to docs and back to home page -->
              <!-- start of social links -->
              <div class="flex-initial flex place-items-center space-x-3 ml-3">
                <a href="https://github.com/d-kma" target="_blank" class="relative text-gray-600 hover:text-pink-500 group">
                  <i class="fab fa-github text-lg" title="github"></i>
                  <i class="absolute top-0 left-0 fab fa-github text-lg group-hover:animate-ping" title="github"></i>
                </a>
                <a href="https://twitter.com/DBlackerMan" target="_blank" class="relative text-gray-600 hover:text-pink-500 group">
                  <i class="fab fa-twitter text-lg" title="twitter"></i>
                  <i class="absolute top-0 left-0 fab fa-twitter text-lg group-hover:animate-ping" title="twitter"></i>
                </a>
              </div>
              <!-- end of social links -->
            </div>
            <!-- end of version info, documentation url and social links -->
          </div>
        </div>
      </div>
    </nav>
    <!-- end of top nav -->
    <!-- start of router view -->
    <div class="w-full" @click="menu = false">
      <router-view v-slot="{ Component }">
        <transition
          name="slideup"
          enter-from-class="opacity-0"
          enter-to-class=""
          enter-active-class="transition transform duration-500 ease-in"
          leave-from-class="opacity-0"
          leave-to-class=""
          leave-active-class="transition transform duration-500 ease-in">
          <keep-alive>
            <component :is="Component"></component>
          </keep-alive>
        </transition>
      </router-view>
    </div>
    <!-- end of router view -->
  </div>
</template>

<script>
import './assets/styles/tailwindstyled.css';

export default {
  name: 'App',
  data() {
    return {
      navPosition: 0,
      menu: false,
    };
  },
  computed: {
    routeName() {
      return this.$route.name;
    },
  },
  mounted() {
    window.addEventListener('scroll', this.scrollPosition);
    window.addEventListener('resize', this.screenResize);
  },
  methods: {
    scrollPosition() {
      if (window.pageYOffset > this.$refs.topNav.offsetTop) this.navPosition = window.pageYOffset;
      else this.navPosition = 0;
    },
    screenResize() {
      this.menu = false;
    },
  },
};
</script>
