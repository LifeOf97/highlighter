<template>
<!-- eslint-disable max-len -->
  <div class="w-11/12 md:w-10/12 mx-auto py-4">
    <!-- start of intro section doc -->
    <div id="intro-section" class="flex flex-col space-y-4">
      <h1 class="text-gray-800 text-3xl sm:text-4xl font-semibold">Introduction</h1>
      <!-- start of JustHighlight info -->
      <div>
        <h3 class="text-2xl font-medium text-gray-800 border-b border-gray-300">JustHighlight</h3>
        <p class="my-4 text-sm sm:text-base text-gray-700">
          JustHighlight is a syntax highlighter api that can be used to highlight code snippets in any kind of website(webapp), blogs
          and other applications that deals with code samples or code hosting.
        </p>
      </div>
      <!-- end of JustHighlight info -->
      <!-- start of apis info -->
      <div class="flex flex-col">
        <h3 class="text-2xl font-medium text-gray-800 border-b border-gray-300">APIs</h3>
        <ul class="flex flex-col space-y-4">
          <li class="flex flex-col space-y-4">
            <p class="mt-4 text-sm sm:text-base text-gray-700">
              This is the main highlighter api. It collects the sourcecode that needs to be highlighted
              along side relevant data options used in styling the code snippet and returns the
              highlighted format of the sourcecode.
            </p>
            <span class="p-4 border-l-4 border-teal-500 bg-gray-100 text-gray-700">NOTE: Only <b>POST</b> request are allowed for this api endpoint.</span>
            <div class="relative p-2 md:p-4 rounded bg-gray-300 group overflow-x-auto">
              <span class="block text-indigo-500 text-sm sm:text-base" ref="api-link">https://api.justhighlight.com/highlighter/</span>
              <button
                type="button"
                class="absolute bottom-0 right-0 text-sm text-white font-medium p-1 md:p-2 rounded-md bg-gradient-to-tr from-blue-600
                via-pink-500 to-red-500 hover:from-red-500 hover:via-pink-500 hover:to-blue-600 opacity-0 group-hover:opacity-100
                transition duration-300 ease-out shadow-lg focus:outline-none">
                Copy
              </button>
            </div>
          </li>
          <li class="flex flex-col space-y-4">
            <p class="mt-4 text-sm sm:text-base text-gray-700">
              Here are the highlighter options api endpoint which returns the values available for a
              particular option.
            </p>
            <span class="p-4 border-l-4 border-teal-500 bg-gray-100 text-gray-700">NOTE: Only <b>GET</b> request are allowed for this api endpoints.</span>
            <span class="text-sm sm:text-base text-gray-700">Languages option api endpoint. Returns a list of available languages.</span>
            <div class="relative p-2 md:p-4 rounded bg-gray-300 group overflow-x-auto">
              <span class="block text-indigo-500 text-sm sm:text-base" ref="api-link">https://api.justhighlight.com/highlighter/</span>
              <button
                type="button"
                class="absolute bottom-0 right-0 text-sm text-white font-medium p-1 md:p-2 rounded-md bg-gradient-to-tr from-blue-600
                via-pink-500 to-red-500 hover:from-red-500 hover:via-pink-500 hover:to-blue-600 opacity-0 group-hover:opacity-100
                transition duration-300 ease-out shadow-lg focus:outline-none">
                Copy
              </button>
            </div>
            <span class="text-sm sm:text-base text-gray-700">Styles option api endpoint. Returns a list of available styles.</span>
            <div class="relative p-2 md:p-4 rounded bg-gray-300 group overflow-x-auto">
              <span class="block text-indigo-500 text-sm sm:text-base" ref="api-link">https://api.justhighlight.com/styles/</span>
              <button
                type="button"
                class="absolute bottom-0 right-0 text-sm text-white font-medium p-1 md:p-2 rounded-md bg-gradient-to-tr from-blue-600
                via-pink-500 to-red-500 hover:from-red-500 hover:via-pink-500 hover:to-blue-600 opacity-0 group-hover:opacity-100
                transition duration-300 ease-out shadow-lg focus:outline-none">
                Copy
              </button>
            </div>
            <span class="text-sm sm:text-base text-gray-700">Formats option api endpoint. Returns a list of available formats.</span>
            <div class="relative p-2 md:p-4 rounded bg-gray-300 group overflow-x-auto">
              <span class="block text-indigo-500 text-sm sm:text-base" ref="api-link">https://api.justhighlight.com/formats/</span>
              <button
                type="button"
                class="absolute bottom-0 right-0 text-sm text-white font-medium p-1 md:p-2 rounded-md bg-gradient-to-tr from-blue-600
                via-pink-500 to-red-500 hover:from-red-500 hover:via-pink-500 hover:to-blue-600 opacity-0 group-hover:opacity-100
                transition duration-300 ease-out shadow-lg focus:outline-none">
                Copy
              </button>
            </div>
          </li>
        </ul>
      </div>
      <!-- end of apis info -->
    </div>
    <!-- end of intro section doc -->
    <!-- start of request response format -->
    <div id="reqres-section"  class="my-6 flex flex-col space-y-4">
      <h1 class="text-gray-800 text-3xl sm:text-4xl font-semibold">Request & Response format</h1>
      <!-- start of highlighter main api endpoint -->
      <div>
        <h3 class="text-2xl font-medium text-gray-800 border-b border-gray-300">Highlighter Endpoint</h3>
        <p class="my-4 text-sm sm:text-base text-gray-700">The highlighter request format.</p>
      </div>
      <!-- end of highlighter main api endpoint -->
    </div>
    <!-- end of request response format -->
    <!-- start of footer -->
    <base-footer />
    <!-- end of footer -->
  </div>
</template>

<script>
// import BaseHighlight from '../components/BaseHighlight.vue';
import BaseFooter from '../components/BaseFooter.vue';

export default {
  name: 'DocsDetail',
  components: { BaseFooter },
};
</script>
