<template>
<!-- eslint-disable max-len -->
  <div id="home" class="w-full h-full bg-white overflow-x-hidden">
    <!-- top nav and hero div -->
    <header id="header" class="w-full bg-teal-200 shadow-sm">
      <!-- start of hero div -->
      <div class="h-66 w-11/12 mx-auto flex pt-6 md:pt-10">
        <div class="flex-1 text-5xl md:text-6xl font-black tracking-tighter">
          <p class="p-0 text-transparent bg-clip-text bg-gradient-to-tr from-blue-600 via-pink-500 to-red-500">Just</p>
          <p class="p-0 text-transparent bg-clip-text bg-gradient-to-tr from-blue-600 via-pink-500 to-red-500">Highlight Your Code!</p>
        </div>
      </div>
      <!-- end of hero div -->
    </header>
    <!-- end of top nav and hero div -->
    <!-- start od editor div -->
    <aside id="editor" class="md:absolute w-full mx-auto h-auto flex justify-end">
      <div class="w-11/12 mx-auto md:mx-0 md:w-6/12 xl:mr-12 bg-gray-800 rounded-b-md border-t border-gray-600 rounded-md shadow-2xl overflow-hidden -mt-20">
        <code-editor />
      </div>
    </aside>
    <!-- end of eitor div -->
    <!-- start of info div -->
    <aside id="info" class="w-11/12 mx-auto mt-8 md:py-12 flex flex-wrap justify-between md:flex-col md:space-y-12">
      <div class="flex-initial flex-grow mb-12 md:mb-0">
        <h3 class="text-2xl font-black text-black">Syntax Highlighter.</h3>
        <p class="text-sm text-gray-600 font-medium leading-5">
          JustHighlight is a code snippet <br/>
          syntax highlighter, that can be used <br/>
          in your blog apps, websites and more.
        </p>
      </div>
      <div class="flex-initial flex-grow mb-12 md:mb-0">
        <h3 class="text-2xl font-black text-black">Support & Styling.</h3>
        <p class="text-sm text-gray-600 font-medium leading-5">
          It supports over 400 programming <br>
          languages and text formats.
        </p>
      </div>
      <div class="flex-initial flex-grow mb-12 md:mb-0">
        <h3 class="text-2xl font-black text-black">Availability & Usage.</h3>
        <p class="text-sm text-gray-600 font-medium leading-5">
          It is available over an API, <br>
          it can be used along side any frontend <br>
          framework that can make requests to an api
        </p>
      </div>
    </aside>
    <!-- end of info div -->
  </div>
</template>

<script>
import CodeEditor from './CodeEditor.vue';

export default {
  name: 'Home',
  components: { CodeEditor },
};
</script>
