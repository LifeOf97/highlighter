<template>
<!-- eslint-disable max-len -->
  <div
    :class="[darkMode ? 'dark' : '']"
    id="nav" class="relative bg-white bg-scroll">
    <!-- start of top nav -->
    <nav
      ref="topNav"
      id="topNav"
      :class="[navPosition ? 'shadow-xl dark:shadow-white-xl z-20' : 'z-20']"
      class="fixed top-0 left-0 w-full bg-cyan-300 dark:bg-coolGray-900 transition duration-700">
      <div class="py-6 w-11/12 mx-auto flex flex-col md:flex-row md:justify-between">
        <!-- logo -->
        <div class="flex-1 flex justify-between mb-1 md:mb-0">
          <h1 class="font-black text-2xl text-black dark:text-white tracking-tight border-b-4 border-dotted border-black dark:border-white">JustHighlight</h1>
          <button class="md:hidden focus:outline-none">
            <i
              @click="menu = !menu"
              class="fas fa-bars text-3xl text-gray-600 hover:text-red-500 transition duration-200"></i>
          </button>
        </div>
        <!-- start of version info, documentation url, and social links -->
        <!-- this div block is hidden on small screens and can only be seen with a toggle menu button -->
        <!-- which slides down/up on click -->
        <div
          :class="[menu ? 'translate-y-0 opacity-100' : '-translate-y-24 md:translate-y-0 opacity-0 md:opacity-100']"
          class="flex-1 flex justify-center items-center bg-coolGray-700 dark:bg-blueGray-800 absolute top-0 left-0 w-full transition transform duration-300 h-24 md:relative md:block md:bg-transparent md:dark:bg-transparent md:h-auto">
          <!-- start of version info -->
          <div class="flex justify-center md:justify-end">
            <div
              class="flex-initial flex place-items-center space-x-2 px-3 text-gray-500 border-r border-gray-400">
              <i class="fas fa-tag text-md"></i>
              <span class="font-semibold text-sm">Version 1.0.1</span>
            </div>
            <!-- end of version info -->
            <!-- start of close nav button that is only avialable on small screens when the nav bar is open -->
            <button
              type="button"
              @click="menu = false"
              class="absolute top-0 right-0 mr-3 mt-1 focus:outline-none group md:hidden">
              <i class="fas fa-times text-transparent text-2xl font-bold bg-clip-text bg-gradient-to-br from-blue-600 via-pink-500 to-red-500"></i>
            </button>
            <!-- end of close nav button -->
            <!-- start of router links to docs and back to home page -->
            <div class="flex-initial flex items-center px-3">
              <div class="group hover:bg-white transition duration-500 rounded-lg">
                <!-- these route link is available when the current page is the Home page -->
                <router-link
                  v-if="routeName === 'Home'"
                  :to="{name: 'Docs'}"
                  :class="'flex px-2 py-1 justify-center items-center'">
                    <span @click="menu = false" class="font-semibold text-base text-white md:text-gray-800 md:dark:text-gray-200 group-hover:text-pink-500 transition duration-500">Docs</span>
                </router-link>
                <!-- these route link is available when the current page is the Docs page -->
                <router-link
                  v-else
                  :to="{name: 'Home'}"
                  class="'flex px-2 py-1 justify-center items-center'">
                    <span @click="menu = false" class="font-semibold text-base text-white md:text-gray-800 md:dark:text-gray-200 group-hover:text-pink-500 transition duration-500">Home</span>
                  </router-link>
              </div>
              <!-- end of router links to docs and back to home page -->
              <!-- start of social links -->
              <div class="flex-initial flex place-items-center space-x-3 ml-3">
                <a href="https://github.com/d-kma/highlighter" target="_blank" class="relative text-gray-500 hover:text-pink-500 dark:hover:text-pink-500 group">
                  <i class="fab fa-github text-lg" title="github"></i>
                  <i class="absolute top-0 left-0 fab fa-github text-lg group-hover:animate-ping" title="github"></i>
                </a>
                <a href="https://twitter.com/DBlackerMan" target="_blank" class="relative text-gray-500 hover:text-pink-500 dark:hover:text-pink-500 group">
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
    <div
      class="w-full" @click="menu = false">
      <router-view v-slot="{ Component }">
        <transition
          name="slideup"
          enter-from-class="opacity-0"
          enter-to-class=""
          enter-active-class="transition transform duration-100 dura ease-in"
          leave-from-class=""
          leave-to-class="opacity-0"
          leave-active-class="transition transform duration-100 ease-in">
          <keep-alive>
            <component :is="Component"></component>
          </keep-alive>
        </transition>
      </router-view>
    </div>
    <!-- end of router view -->
    <!-- start of button to toggle dark mode -->
    <div ref="darkModeTem" class="fixed bottom-0 right-0 mr-6 mb-6 md:mr-8 md:mb-8 z-50">
      <div class="relative w-6 h-12 rounded-xl bg-coolGray-900 dark:bg-cyan-300 shadow-xl dark:shadow-white-sm transition duration-300">
        <input type="checkbox" name="darkMode" id="darkMode" v-model="darkMode" class="cursor-pointer hidden focus:outline-none" />
        <label
          :class="[darkMode ? 'translate-y-6' : '']"
          for="darkMode" class="inline-block cursor-pointer w-5 h-5 rounded-full bg-white dark:bg-coolGray-900 mt-0.5 ml-0.5 transition transform duration-300">
            <div class="w-full h-full flex items-center justify-center text-sm">
              <i v-if="darkMode" class="far fa-sun text-yellow-400"></i>
              <i v-else class="fas fa-moon text-blueGray-500"></i>
            </div>
          </label>
      </div>
    </div>
    <!-- end of button to toggle dark mode -->
  </div>
</template>

<script>
import gsap from 'gsap';
import './assets/styles/tailwindstyled.css';

export default {
  name: 'App',
  data() {
    return {
      navPosition: 0,
      darkMode: false,
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
    this.gsapAnimDarkModeTem();
  },
  methods: {
    scrollPosition() {
      if (window.pageYOffset > this.$refs.topNav.offsetTop) this.navPosition = window.pageYOffset;
      else this.navPosition = 0;
    },
    screenResize() {
      this.menu = false;
    },
    gsapAnimDarkModeTem() {
      // method to apply gsap animation on the dark mode toggle button
      // get the template ref assigned to the dark mode template
      const { darkModeTem } = this.$refs;
      gsap.from(darkModeTem, {
        delay: 8, opacity: 0, scale: 0, duration: 1,
      });
    },
  },
};
</script>
