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
              The justHighlighter api is divided into two endpoints. The highlighter endpoint collects the sourcecode that needs to be highlighted
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
              The second endpoint deals with the highlighter options api endpoint which returns the values available for a
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
    <div id="reqres-section"  class="my-6 flex flex-col space-y-6">
      <h1 class="text-gray-800 text-3xl sm:text-4xl font-semibold">Request & Response format</h1>
      <!-- start of highlighter main api endpoint -->
      <div class="flex flex-col">
        <h3 class="text-2xl font-medium text-gray-800 border-b border-gray-300">Highlighter Endpoint</h3>
        <p class="my-4 text-sm sm:text-base text-gray-700">The <b>request</b> format.</p>
        <!-- start of highlighted request code snippet -->
        <div id="highlighter-request" class="relative bg-gray-800 h-66 rounded overflow-auto cursor-text shadow-inner">
          <div class="justhighlight absolute top-0 left-0 h-full w-full text-sm" style="padding: 20px;"><pre style="line-height: 125%; margin: 0;"><span></span><span style="color: #f8f8f2">{</span><br>  <span style="color: #75715e">// code snippet to be highlighted. required.</span><br>  <span style="color: #a6e22e">code</span><span style="color: #f92672">:</span> <span style="color: #e6db74">&#39;&#39;</span><span style="color: #f8f8f2">,</span><br><br>  <span style="color: #75715e">// programming language (sourcecode) of the code snippet to be highlighted. required. </span><br>  <span style="color: #a6e22e">language</span><span style="color: #f92672">:</span> <span style="color: #e6db74">&#39;python&#39;</span><span style="color: #f8f8f2">,</span> <span style="color: #75715e">// default</span><br><br>  <span style="color: #75715e">// syntax highlighting style.</span><br>  <span style="color: #75715e">// checkout the available styles at the features section of this readme.</span><br>  <span style="color: #a6e22e">style</span><span style="color: #f92672">:</span> <span style="color: #e6db74">&#39;default&#39;</span><span style="color: #f8f8f2">,</span> <span style="color: #75715e">// default</span><br><br>  <span style="color: #75715e">// in what format would you like to retrieve your code snippet,</span><br>  <span style="color: #75715e">// checkout the available formats at the features section of this readme.</span><br>  <span style="color: #a6e22e">getformat</span><span style="color: #f92672">:</span> <span style="color: #e6db74">&#39;html&#39;</span><span style="color: #f8f8f2">,</span> <span style="color: #75715e">// default</span><br><br>  <span style="color: #75715e">// linenos is used to request if the result should have line numbers</span><br>  <span style="color: #75715e">// or not, this can be one of [&#39;inline&#39;, &#39;table&#39;, &#39;none&#39;], defaults to</span><br>  <span style="color: #75715e">// &#39;none&#39;, no line numbers.</span><br>  <span style="color: #75715e">// optional.</span><br>  <span style="color: #a6e22e">linenos</span><span style="color: #f92672">:</span> <span style="color: #e6db74">&#39;none&#39;</span><span style="color: #f8f8f2">,</span> <span style="color: #75715e">// default</span><br>  <br>  <span style="color: #75715e">// format: html =&gt; what type of html styling would you prefer? inline styling or</span><br>  <span style="color: #75715e">// classes, this can be one of [&#39;inline&#39;, &#39;class&#39;]</span><br>  <span style="color: #a6e22e">styling</span><span style="color: #f92672">:</span> <span style="color: #e6db74">&#39;inline&#39;</span><span style="color: #f8f8f2">,</span> <span style="color: #75715e">// default</span><br>  <br>  <span style="color: #75715e">// format: html =&gt; class name giving to the div tag wrapping the whole code block</span><br>  <span style="color: #75715e">// defaults to &#39;justhighlight&#39;, note: if linenos is set to table this</span><br>  <span style="color: #75715e">// will append a &#39;table&#39; making it &#39;justhighlighttable&#39;.</span><br>  <span style="color: #a6e22e">divclass</span><span style="color: #f92672">:</span> <span style="color: #e6db74">&#39;justhighlight&#39;</span><span style="color: #f8f8f2">,</span> <span style="color: #75715e">// default</span><br><br>  <span style="color: #75715e">// hllines is used to specify a list of line numbers to be highlighted in your code snippet</span><br>  <span style="color: #75715e">// this should be an array of numbers. defaults to an empty array.</span><br>  <span style="color: #a6e22e">hllines</span><span style="color: #f92672">:</span> <span style="color: #f8f8f2">[],</span> <span style="color: #75715e">// default</span><br>  <br>  <span style="color: #75715e">// the nobackground option is used to request that the style option selected should not</span><br>  <span style="color: #75715e">// affect the code background color. this should either be true/false </span><br>  <span style="color: #a6e22e">nobackground</span><span style="color: #f92672">:</span> <span style="color: #66d9ef">false</span><span style="color: #f8f8f2">,</span> <span style="color: #75715e">// default</span><br>  <br>  <span style="color: #75715e">// format: html =&gt; classprefix is used to prefix the css classes used</span><br>  <span style="color: #75715e">// when &#39;styling&#39; is set &#39;class&#39;</span><br>  <span style="color: #a6e22e">classprefix</span><span style="color: #f92672">:</span> <span style="color: #e6db74">&#39;&#39;</span> <span style="color: #75715e">// default is an empty string</span><br><span style="color: #f8f8f2">}</span><br></pre></div>
        </div>
        <!-- start of highlighted request code snippet -->
        <!-- start of highlighted response code snippet -->
        <p class="my-4 text-sm sm:text-base text-gray-700 mt-6">The <b>response</b> format.</p>
        <div id="highlighter-response" class="relative bg-gray-800 h-66 rounded overflow-auto cursor-text shadow-inner">
          <div class="justhighlight absolute top-0 left-0 h-full w-full text-sm" style="padding: 20px;"><pre style="line-height: 125%; margin: 0;"><span></span><span style="color: #f8f8f2">{</span><br>    <span style="color: #75715e">// the status of the reesponse.</span><br>    <span style="color: #a6e22e">status</span><span style="color: #f92672">:</span> <span style="color: #e6db74">&#39;success&#39;</span><span style="color: #f8f8f2">,</span><br>    <br>    <span style="color: #75715e">// the result object containing the highlighted code data</span><br>    <span style="color: #a6e22e">result</span><span style="color: #f92672">:</span> <span style="color: #f8f8f2">{</span><br>        <span style="color: #a6e22e">data</span><span style="color: #f92672">:</span> <span style="color: #e6db74">&#39;&#39;</span><span style="color: #f8f8f2">,</span> <span style="color: #75715e">// the highlighted code snippet.</span><br>        <span style="color: #a6e22e">sourcecode</span><span style="color: #f92672">:</span> <span style="color: #e6db74">&#39;&#39;</span><span style="color: #f8f8f2">,</span> <span style="color: #75715e">// the highlighted code return format. </span><br>        <span style="color: #a6e22e">formatting</span><span style="color: #f92672">:</span> <span style="color: #e6db74">&#39;&#39;</span><span style="color: #f8f8f2">,</span> <span style="color: #75715e">// the programming language highlighted.</span><br>        <span style="color: #a6e22e">styles</span><span style="color: #f92672">:</span> <span style="color: #e6db74">&#39;&#39;</span><span style="color: #f8f8f2">,</span> <span style="color: #75715e">// only available when styling is set to class.</span><br>    <span style="color: #f8f8f2">}</span><br><span style="color: #f8f8f2">}</span><br></pre></div>
        </div>
        <!-- end of highlighted response code snippet -->
      </div>
      <!-- end of highlighter main api endpoint -->
      <!-- start of highlighter options api endpiont -->
      <div class="flex flex-col">
        <h3 class="text-2xl font-medium text-gray-800 border-b border-gray-300">Options Endpoint</h3>
        <p class="my-4 text-sm sm:text-base text-gray-700">
          The options endpoint only allows <b>GET</b> request, therefore a get request should be made to any of the options api.
        </p>
        <p class="mb-4 text-sm sm:text-base text-gray-700">The <b>response</b> format.</p>
        <div id="highlighter-response" class="relative bg-gray-800 h-24 rounded overflow-auto cursor-text shadow-inner">
          <div class="justhighlight absolute top-0 left-0 h-full w-full text-sm" style="padding: 20px;"><pre style="line-height: 125%; margin: 0;"><span></span><span style="color: #f8f8f2">{</span><br>    <span style="color: #a6e22e">result</span><span style="color: #f92672">:</span> <span style="color: #f8f8f2">[]</span> <span style="color: #75715e">// returns a list of data.</span><br><span style="color: #f8f8f2">}</span><br></pre></div>
        </div>
      </div>
      <!-- end of highlighter options api endpiont -->
    </div>
    <!-- end of request response format -->
    <!-- start of footer -->
    <base-footer />
    <!-- end of footer -->
  </div>
</template>

<script>
import BaseFooter from '../components/BaseFooter.vue';

export default {
  name: 'DocsDetail',
  components: { BaseFooter },
};
</script>
