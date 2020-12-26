<template>
<!-- eslint-disable max-len -->
  <div id="home" class="mt-16 w-full h-full md:h-screen bg-white dark:bg-blueGray-800 overflow-x-hidden py-4">
    <!-- top nav and hero div -->
    <header id="header" class="w-full bg-cyan-300 dark:bg-coolGray-900 shadow-sm">
      <!-- start of hero div -->
      <div class="h-66 w-11/12 mx-auto flex pt-6 md:pt-10">
        <div class="flex-1 text-5xl md:text-6xl font-black tracking-tighter">
          <p ref="hero" class="inline-flex p-0 text-transparent bg-clip-text bg-gradient-to-tr from-blue-600 via-pink-500 to-red-500">Just</p><br>
          <p ref="hero1" class="inline-flex p-0 text-transparent bg-clip-text bg-gradient-to-tr from-blue-600 via-pink-500 to-red-500">Highlight</p>
          <p ref="hero2" class="inline-flex p-0 text-transparent bg-clip-text bg-gradient-to-tr from-blue-600 via-pink-500 to-red-500">Your</p>
          <p ref="hero3" class="inline-flex p-0 text-transparent bg-clip-text bg-gradient-to-tr from-blue-600 via-pink-500 to-red-500">Code!</p>
        </div>
      </div>
      <!-- end of hero div -->
    </header>
    <!-- end of top nav and hero div -->
    <!-- start of editor div -->
    <aside id="editor" class="md:absolute w-full mx-auto h-auto flex justify-end z-10">
      <div ref="editor" class="w-11/12 mx-auto md:mx-0 md:w-6/12 xl:mr-12 rounded-lg shadow-2xl dark:shadow-white-lg overflow-hidden -mt-20">
        <keep-alive>
          <component :is="active" @update:component="updateComponent"></component>
        </keep-alive>
      </div>
    </aside>
    <!-- end of eitor div -->
    <!-- start of info div -->
    <aside id="info" class="w-11/12 mx-auto mt-8 md:mt-2 md:py-12 flex flex-wrap justify-between md:flex-col md:space-y-8">
      <div ref="info" class="flex-initial mb-5 md:mb-0">
        <h3 class="text-2xl font-black text-black dark:text-gray-200">Syntax Highlighter.</h3>
        <p class="text-sm text-gray-400 dark:text-blueGray-500 font-medium leading-5">
          JustHighlight is a code snippet <br/>
          syntax highlighter, that can be used <br/>
          in your blog apps, websites and more.
        </p>
      </div>
      <div ref="info1" class="flex-initial mb-5 md:mb-0">
        <h3 class="text-2xl font-black text-black dark:text-gray-200">Support & Styling.</h3>
        <p class="text-sm text-gray-400 dark:text-blueGray-500 font-medium leading-5">
          It supports over 400 programming <br>
          languages and text formats.
        </p>
      </div>
      <div ref="info2" class="flex-initial mb-5 md:mb-0">
        <h3 class="text-2xl font-black text-black dark:text-gray-200">Availability & Usage.</h3>
        <p class="text-sm text-gray-400 dark:text-blueGray-500 font-medium leading-5">
          It is available over an API, <br>
          it can be used along side any frontend <br>
          framework that can make requests to an api
        </p>
      </div>
    </aside>
    <!-- end of info div -->
    <base-footer />
  </div>
</template>

<script>
import gsap from 'gsap';
import CodeEditor from './CodeEditor.vue';
import CodeResult from './CodeResult.vue';
import BaseFooter from '../components/BaseFooter.vue';

export default {
  name: 'Home',
  components: { CodeEditor, CodeResult, BaseFooter },
  data() {
    return {
      current: 'CodeEditor',
    };
  },
  mounted() {
    this.gsapAnim1();
  },
  computed: {
    active() {
      return this.current;
    },
  },
  methods: {
    updateComponent(value) {
      // method to update the editor component
      this.current = value;
    },
    gsapAnim1() {
      // this method is to create a little gsap animation on the page.
      // get all refs needed for gsap animation, using object destructuring.
      const {
        hero, hero1, hero2, hero3,
        info, info1, info2, editor,
      } = this.$refs;
      // gsap timeline: using gsap timeline we organize the animation accordingly
      // from the bigtext to the editor and then the info's.
      const tl = gsap.timeline();
      tl.from([hero, hero1, hero2, hero3], {
        duration: 1.5, y: -50, opacity: 0, scale: 0.4, delay: 0.7, ease: 'elastic', stagger: 0.6,
      })
        .from(editor, {
          duration: 0.7, opacity: 0, y: 100,
        })
        .from([info, info1, info2], {
          duration: 0.5, y: 40, skewX: 5, opacity: 0, stagger: 0.3, delay: 1,
        });
    },
  },
};
</script>
