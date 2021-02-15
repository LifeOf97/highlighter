<template>
<!-- eslint-disable max-len -->
  <div class="w-11/12 md:w-10/12 mx-auto py-4">
    <!-- start of intro section doc -->
    <div id="intro-section" class="flex flex-col space-y-4">
      <h1 class="text-gray-700 dark:text-gray-300 text-3xl sm:text-4xl font-semibold">Introduction</h1>
      <!-- start of JustHighlight info -->
      <div>
        <h3 class="text-2xl font-medium text-gray-700 dark:text-gray-300 border-b border-gray-300">JustHighlight</h3>
        <p class="my-4 text-sm sm:text-base text-gray-600 dark:text-gray-400">
          JustHighlight is a syntax highlighter api that can be used to highlight code snippets in any kind of website(webapp), blogs
          and other applications that deals with code samples or code hosting.
        </p>
      </div>
      <!-- end of JustHighlight info -->
      <!-- start of apis info -->
      <div id="apis" class="flex flex-col">
        <h3 class="text-2xl font-medium text-gray-700 dark:text-gray-300 border-b border-gray-300">APIs Endpoint</h3>
        <ul class="flex flex-col space-y-4">
          <li class="flex flex-col space-y-4">
            <p class="mt-4 text-sm sm:text-base text-gray-600 dark:text-gray-400">
              The justHighlight api is divided into two endpoints. The highlighter endpoint collects the sourcecode that needs to be highlighted
              along side relevant data options used in styling the code snippet and returns the
              highlighted format of the sourcecode.
            </p>
            <span class="p-4 border-l-4 border-cyan-300 bg-gray-100 dark:bg-gray-300 text-gray-600">NOTE: Only <b>POST</b> request are allowed for this api endpoint.</span>
            <div class="relative p-2 md:p-4 rounded bg-gray-300 group overflow-x-auto">
              <span class="block text-indigo-500 text-sm sm:text-base" ref="api-link">https://api.justhighlight.com/highlighter/</span>
            </div>
          </li>
          <li class="flex flex-col space-y-4">
            <p class="mt-4 text-sm sm:text-base text-gray-600 dark:text-gray-400">
              The second endpoint deals with the highlighter options api endpoint which returns the values available for a
              particular option.
            </p>
            <span class="p-4 border-l-4 border-cyan-300 bg-gray-100 dark:bg-gray-300 text-gray-600">NOTE: Only <b>GET</b> request are allowed for this api endpoints.</span>
            <span class="text-sm sm:text-base text-gray-600 dark:text-gray-400">Language option api endpoint. Returns a list of available languages.</span>
            <div class="relative p-2 md:p-4 rounded bg-gray-300 group overflow-x-auto">
              <span class="block text-indigo-500 text-sm sm:text-base" ref="api-link">https://api.justhighlight.com/options/languages/</span>
            </div>
            <span class="text-sm sm:text-base text-gray-600 dark:text-gray-400">Style option api endpoint. Returns a list of available styles.</span>
            <div class="relative p-2 md:p-4 rounded bg-gray-300 group overflow-x-auto">
              <span class="block text-indigo-500 text-sm sm:text-base" ref="api-link">https://api.justhighlight.com/options/styles/</span>
            </div>
            <span class="text-sm sm:text-base text-gray-600 dark:text-gray-400">Format option api endpoint. Returns a list of available formats.</span>
            <div id="bm-reqres" class="relative p-2 md:p-4 rounded bg-gray-300 group overflow-x-auto">
              <span class="block text-indigo-500 text-sm sm:text-base" ref="api-link">https://api.justhighlight.com/options/formats/</span>
            </div>
          </li>
        </ul>
      </div>
      <!-- end of apis info -->
    </div>
    <!-- end of intro section doc -->
    <!-- start of request response format -->
    <div id="reqres-section"  class="my-6 flex flex-col space-y-6">
      <h1 class="text-gray-700 dark:text-gray-300 text-3xl sm:text-4xl font-semibold">Request & Response format</h1>
      <!-- start of highlighter main api endpoint -->
      <div class="flex flex-col">
        <h3 class="text-2xl font-medium text-gray-700 dark:text-gray-300 border-b border-gray-300">Highlighter Endpoint</h3>
        <p class="my-4 text-sm sm:text-base text-gray-600 dark:text-gray-400">The <b>request</b> format.</p>
        <!-- start of highlighted request code snippet -->
        <div id="highlighter-request" class="relative bg-coolGray-700 dark:bg-blueGray-700 h-66 rounded overflow-auto cursor-text shadow-inner">
          <div class="justhighlight absolute top-0 left-0 h-full w-full text-sm" style="padding: 20px;"><pre style="line-height: 125%; margin: 0;"><span></span><span style="color: #f8f8f2">{</span><br>  <span style="color: #75715e">// Code snippet to be highlighted. Required.</span><br>  <span style="color: #a6e22e">code</span><span style="color: #f92672">:</span> <span style="color: #e6db74">&#39;&#39;</span><span style="color: #f8f8f2">,</span><br><br>  <span style="color: #75715e">// Programming language (sourcecode) of the code snippet to be highlighted. Required. </span><br>  <span style="color: #a6e22e">language</span><span style="color: #f92672">:</span> <span style="color: #e6db74">&#39;python&#39;</span><span style="color: #f8f8f2">,</span> <span style="color: #75715e">// default</span><br><br>  <span style="color: #75715e">// Syntax highlighting style.</span><br>  <span style="color: #75715e">// checkout the available styles at the features section of this doc.</span><br>  <span style="color: #a6e22e">style</span><span style="color: #f92672">:</span> <span style="color: #e6db74">&#39;default&#39;</span><span style="color: #f8f8f2">,</span> <span style="color: #75715e">// default</span><br><br>  <span style="color: #75715e">// In what format would you like to retrieve your code snippet,</span><br>  <span style="color: #75715e">// checkout the available formats at the features section of this doc.</span><br>  <span style="color: #a6e22e">getFormat</span><span style="color: #f92672">:</span> <span style="color: #e6db74">&#39;html&#39;</span><span style="color: #f8f8f2">,</span> <span style="color: #75715e">// default</span><br><br>  <span style="color: #75715e">// lineNo is used to request if the result should have line numbers</span><br>  <span style="color: #75715e">// or not, this can be one of [&#39;inline&#39;, &#39;table&#39;, &#39;none&#39;], defaults to</span><br>  <span style="color: #75715e">// &#39;none&#39;, no line numbers. Optional.</span><br>  <span style="color: #a6e22e">lineNo</span><span style="color: #f92672">:</span> <span style="color: #e6db74">&#39;none&#39;</span><span style="color: #f8f8f2">,</span> <span style="color: #75715e">// default</span><br>  <br>  <span style="color: #75715e">// FORMAT: HTML =&gt; what type of html css styling would you prefer? inline css or</span><br>  <span style="color: #75715e">// classes, this can be one of [&#39;inline&#39;, &#39;class&#39;]</span><br>  <span style="color: #a6e22e">css</span><span style="color: #f92672">:</span> <span style="color: #e6db74">&#39;inline&#39;</span><span style="color: #f8f8f2">,</span> <span style="color: #75715e">// default</span><br>  <br>  <span style="color: #75715e">// FORMAT: HTML =&gt; class name giving to the div tag wrapping the whole code block</span><br>  <span style="color: #75715e">// defaults to &#39;justhighlight&#39;. NOTE: if &quot;lineNos&quot; is set to table this</span><br>  <span style="color: #75715e">// will append a &#39;table&#39; to the class name making it for example &#39;justhighlighttable&#39;.</span><br>  <span style="color: #a6e22e">divClass</span><span style="color: #f92672">:</span> <span style="color: #e6db74">&#39;justhighlight&#39;</span><span style="color: #f8f8f2">,</span> <span style="color: #75715e">// default</span><br><br>  <span style="color: #75715e">// hlLines is used to specify a list of line numbers to be highlighted in your code snippet</span><br>  <span style="color: #75715e">// this should be an array of numbers. Defaults to an empty array.</span><br>  <span style="color: #a6e22e">hlLines</span><span style="color: #f92672">:</span> <span style="color: #f8f8f2">[],</span> <span style="color: #75715e">// default</span><br>  <br>  <span style="color: #75715e">// FORMAT: HTML =&gt; classPrefix is used to prefix the css classes used</span><br>  <span style="color: #75715e">// when &quot;css&quot; is set &quot;class&quot;.</span><br>  <span style="color: #a6e22e">classPrefix</span><span style="color: #f92672">:</span> <span style="color: #e6db74">&#39;&#39;</span> <span style="color: #75715e">// default is an empty string</span><br><br>  <span style="color: #75715e">// The noBackground option is used to request that the &quot;style&quot; option selected should not</span><br>  <span style="color: #75715e">// affect the code background color. this should either be true/false, where true is</span><br>  <span style="color: #75715e">// &quot;do not apply background color&quot; and false is &quot;apply background color&quot;. </span><br>  <span style="color: #a6e22e">noBackground</span><span style="color: #f92672">:</span> <span style="color: #66d9ef">false</span><span style="color: #f8f8f2">,</span> <span style="color: #75715e">// default</span><br><span style="color: #f8f8f2">}</span><br></pre></div>
          <!-- <div class="justhighlight absolute top-0 left-0 h-full w-full text-sm" style="padding: 20px;"><pre style="line-height: 125%; margin: 0;"><span></span><span style="color: #f8f8f2">{</span><br>  <span style="color: #75715e">// code snippet to be highlighted. required.</span><br>  <span style="color: #a6e22e">code</span><span style="color: #f92672">:</span> <span style="color: #e6db74">&#39;&#39;</span><span style="color: #f8f8f2">,</span><br><br>  <span style="color: #75715e">// programming language (sourcecode) of the code snippet to be highlighted. required. </span><br>  <span style="color: #a6e22e">language</span><span style="color: #f92672">:</span> <span style="color: #e6db74">&#39;python&#39;</span><span style="color: #f8f8f2">,</span> <span style="color: #75715e">// default</span><br><br>  <span style="color: #75715e">// syntax highlighting style.</span><br>  <span style="color: #75715e">// checkout the available styles at the features section of this readme.</span><br>  <span style="color: #a6e22e">style</span><span style="color: #f92672">:</span> <span style="color: #e6db74">&#39;default&#39;</span><span style="color: #f8f8f2">,</span> <span style="color: #75715e">// default</span><br><br>  <span style="color: #75715e">// in what format would you like to retrieve your code snippet,</span><br>  <span style="color: #75715e">// checkout the available formats at the features section of this readme.</span><br>  <span style="color: #a6e22e">getformat</span><span style="color: #f92672">:</span> <span style="color: #e6db74">&#39;html&#39;</span><span style="color: #f8f8f2">,</span> <span style="color: #75715e">// default</span><br><br>  <span style="color: #75715e">// linenos is used to request if the result should have line numbers</span><br>  <span style="color: #75715e">// or not, this can be one of [&#39;inline&#39;, &#39;table&#39;, &#39;none&#39;], defaults to</span><br>  <span style="color: #75715e">// &#39;none&#39;, no line numbers.</span><br>  <span style="color: #75715e">// optional.</span><br>  <span style="color: #a6e22e">linenos</span><span style="color: #f92672">:</span> <span style="color: #e6db74">&#39;none&#39;</span><span style="color: #f8f8f2">,</span> <span style="color: #75715e">// default</span><br>  <br>  <span style="color: #75715e">// format: html =&gt; what type of html styling would you prefer? inline styling or</span><br>  <span style="color: #75715e">// classes, this can be one of [&#39;inline&#39;, &#39;class&#39;]</span><br>  <span style="color: #a6e22e">css</span><span style="color: #f92672">:</span> <span style="color: #e6db74">&#39;inline&#39;</span><span style="color: #f8f8f2">,</span> <span style="color: #75715e">// default</span><br>  <br>  <span style="color: #75715e">// format: html =&gt; class name giving to the div tag wrapping the whole code block</span><br>  <span style="color: #75715e">// defaults to &#39;justhighlight&#39;, note: if linenos is set to table this</span><br>  <span style="color: #75715e">// will append a &#39;table&#39; making it &#39;justhighlighttable&#39;.</span><br>  <span style="color: #a6e22e">divclass</span><span style="color: #f92672">:</span> <span style="color: #e6db74">&#39;justhighlight&#39;</span><span style="color: #f8f8f2">,</span> <span style="color: #75715e">// default</span><br><br>  <span style="color: #75715e">// hllines is used to specify a list of line numbers to be highlighted in your code snippet</span><br>  <span style="color: #75715e">// this should be an array of numbers. defaults to an empty array.</span><br>  <span style="color: #a6e22e">hllines</span><span style="color: #f92672">:</span> <span style="color: #f8f8f2">[],</span> <span style="color: #75715e">// default</span><br>  <br>  <span style="color: #75715e">// the nobackground option is used to request that the style option selected should not</span><br>  <span style="color: #75715e">// affect the code background color. this should either be true/false </span><br>  <span style="color: #a6e22e">nobackground</span><span style="color: #f92672">:</span> <span style="color: #66d9ef">false</span><span style="color: #f8f8f2">,</span> <span style="color: #75715e">// default</span><br>  <br>  <span style="color: #75715e">// format: html =&gt; classprefix is used to prefix the css classes used</span><br>  <span style="color: #75715e">// when &#39;styling&#39; is set &#39;class&#39;</span><br>  <span style="color: #a6e22e">classprefix</span><span style="color: #f92672">:</span> <span style="color: #e6db74">&#39;&#39;</span> <span style="color: #75715e">// default is an empty string</span><br><span style="color: #f8f8f2">}</span><br></pre></div> -->
        </div>
        <!-- start of highlighted request code snippet -->
        <!-- start of highlighted response code snippet -->
        <p class="my-4 text-sm sm:text-base text-gray-600 dark:text-gray-400 mt-6">The <b>response</b> format.</p>
        <div id="highlighter-response" class="relative bg-coolGray-700 dark:bg-blueGray-700 h-64 rounded overflow-auto cursor-text shadow-inner">
          <div class="justhighlight absolute top-0 left-0 h-full w-full text-sm" style="padding: 20px;"><pre style="line-height: 125%; margin: 0;"><span></span><span style="color: #f8f8f2">{</span><br>    <span style="color: #75715e">// the status of the reesponse.</span><br>    <span style="color: #a6e22e">status</span><span style="color: #f92672">:</span> <span style="color: #e6db74">&#39;success&#39;</span><span style="color: #f8f8f2">,</span><br>    <br>    <span style="color: #75715e">// the result object containing the highlighted code data</span><br>    <span style="color: #a6e22e">result</span><span style="color: #f92672">:</span> <span style="color: #f8f8f2">{</span><br>        <span style="color: #a6e22e">highlighted</span><span style="color: #f92672">:</span> <span style="color: #e6db74">&#39;&#39;</span><span style="color: #f8f8f2">,</span> <span style="color: #75715e">// the highlighted code snippet.</span><br>        <span style="color: #a6e22e">sourcecode</span><span style="color: #f92672">:</span> <span style="color: #e6db74">&#39;&#39;</span><span style="color: #f8f8f2">,</span> <span style="color: #75715e">// the highlighted code return format. </span><br>        <span style="color: #a6e22e">formatting</span><span style="color: #f92672">:</span> <span style="color: #e6db74">&#39;&#39;</span><span style="color: #f8f8f2">,</span> <span style="color: #75715e">// the programming language highlighted.</span><br>        <span style="color: #a6e22e">styles</span><span style="color: #f92672">:</span> <span style="color: #e6db74">&#39;&#39;</span><span style="color: #f8f8f2">,</span> <span style="color: #75715e">// only available when styling is set to class.</span><br>    <span style="color: #f8f8f2">}</span><br><span style="color: #f8f8f2">}</span><br></pre></div>
        </div>
        <!-- end of highlighted response code snippet -->
      </div>
      <!-- end of highlighter main api endpoint -->
      <!-- start of highlighter options api endpiont -->
      <div class="flex flex-col">
        <h3 class="text-2xl font-medium text-gray-700 dark:text-gray-300 border-b border-gray-300">Options Endpoint</h3>
        <p class="my-4 text-sm sm:text-base text-gray-600 dark:text-gray-400">
          The options endpoint only allows <b>GET</b> request, therefore a get request should be made to any of the options api.
        </p>
        <p class="mb-4 text-sm sm:text-base text-gray-600 dark:text-gray-400">The <b>response</b> format.</p>
        <div id="highlighter-response" class="relative bg-coolGray-700 dark:bg-blueGray-700 h-24 rounded overflow-auto cursor-text shadow-inner">
          <div class="justhighlight absolute top-0 left-0 h-full w-full text-sm" style="padding: 20px;"><pre style="line-height: 125%; margin: 0;"><span></span><span style="color: #f8f8f2">{</span><br>    <span style="color: #a6e22e">result</span><span style="color: #f92672">:</span> <span style="color: #f8f8f2">[]</span> <span style="color: #75715e">// returns a list of data.</span><br><span style="color: #f8f8f2">}</span><br></pre></div>
        </div>
      </div>
      <!-- end of highlighter options api endpiont -->
    </div>
    <!-- end of request response format -->
    <!-- start of example -->
    <div id="reqres-section" class="my-6 flex flex-col space-y-6">
      <h1 class="text-gray-700 dark:text-gray-300 text-3xl sm:text-4xl font-semibold">Examples</h1>
      <div id="example-axios" class="flex flex-col space-y-5">
        <h3 class="text-2xl font-medium text-gray-700 dark:text-gray-300 border-b border-gray-300">Using axios api</h3>
        <div class="relative bg-coolGray-700 dark:bg-blueGray-700 h-56 rounded overflow-auto cursor-text shadow-inner">
          <div class="justhighlight absolute top-0 left-0 h-full w-full text-sm" style="padding: 20px;"><pre style="line-height: 125%; margin: 0;"><span></span><span style="color: #a6e22e">axios</span><span style="color: #f8f8f2">.</span><span style="color: #a6e22e">post</span><span style="color: #f8f8f2">(</span><span style="color: #e6db74">&#39;https://api.justhighlight.com/highlighter/&#39;</span><span style="color: #f8f8f2">,</span> <span style="color: #f8f8f2">{</span><br>    <span style="color: #a6e22e">code</span><span style="color: #f92672">:</span> <span style="color: #e6db74">&quot;const greet = &#39;Hello World!&#39;&quot;</span><span style="color: #f8f8f2">,</span><br>    <span style="color: #a6e22e">language</span><span style="color: #f92672">:</span> <span style="color: #e6db74">&#39;javascript&#39;</span><span style="color: #f8f8f2">,</span><br>    <span style="color: #a6e22e">getFormat</span><span style="color: #f92672">:</span> <span style="color: #e6db74">&#39;html&#39;</span><span style="color: #f8f8f2">,</span><br>    <span style="color: #a6e22e">style</span><span style="color: #f92672">:</span> <span style="color: #e6db74">&#39;paraiso-dark&#39;</span><span style="color: #f8f8f2">,</span><br>    <span style="color: #a6e22e">lineNo</span><span style="color: #f92672">:</span> <span style="color: #e6db74">&#39;none&#39;</span><span style="color: #f8f8f2">,</span><br>    <span style="color: #a6e22e">css</span><span style="color: #f92672">:</span> <span style="color: #e6db74">&#39;inline&#39;</span><span style="color: #f8f8f2">,</span><br>    <span style="color: #a6e22e">divClass</span><span style="color: #f92672">:</span> <span style="color: #e6db74">&#39;player&#39;</span><span style="color: #f8f8f2">,</span><br>    <span style="color: #a6e22e">hlLines</span><span style="color: #f92672">:</span> <span style="color: #f8f8f2">[],</span><br>    <span style="color: #a6e22e">noBackground</span><span style="color: #f92672">:</span> <span style="color: #66d9ef">false</span><span style="color: #f8f8f2">,</span><br><span style="color: #f8f8f2">})</span><br>  <span style="color: #f8f8f2">.</span><span style="color: #a6e22e">then</span><span style="color: #f8f8f2">((</span><span style="color: #a6e22e">response</span><span style="color: #f8f8f2">)</span> <span style="color: #f8f8f2">=&gt;</span> <span style="color: #f8f8f2">{</span><br>      <span style="color: #75715e">// make use of the returned response as you will.</span><br>      <span style="color: #66d9ef">this</span><span style="color: #f8f8f2">.</span><span style="color: #a6e22e">highlighted</span> <span style="color: #f92672">=</span> <span style="color: #a6e22e">response</span><span style="color: #f8f8f2">.</span><span style="color: #a6e22e">data</span><span style="color: #f8f8f2">.</span><span style="color: #a6e22e">result</span><span style="color: #f8f8f2">.</span><span style="color: #a6e22e">data</span><span style="color: #f8f8f2">;</span><br>  <span style="color: #f8f8f2">})</span><br>  <span style="color: #f8f8f2">.</span><span style="color: #66d9ef">catch</span><span style="color: #f8f8f2">((</span><span style="color: #a6e22e">error</span><span style="color: #f8f8f2">)</span> <span style="color: #f8f8f2">=&gt;</span> <span style="color: #f8f8f2">{</span><br>      <span style="color: #75715e">// catch any error what so ever and debug it.</span><br>      <span style="color: #a6e22e">console</span><span style="color: #f8f8f2">.</span><span style="color: #a6e22e">log</span><span style="color: #f8f8f2">(</span><span style="color: #a6e22e">error</span><span style="color: #f8f8f2">.</span><span style="color: #a6e22e">response</span><span style="color: #f8f8f2">);</span><br>  <span style="color: #f8f8f2">});</span><br></pre></div>
        </div>
      </div>
      <div id="example-fetch" class="flex flex-col space-y-5">
        <h3 class="text-2xl font-medium text-gray-700 dark:text-gray-300 border-b border-gray-300">Using fetch api</h3>
        <div class="relative bg-coolGray-700 dark:bg-blueGray-700 h-56 rounded overflow-auto cursor-text shadow-inner">
          <div class="justhighlight absolute top-0 left-0 h-full w-full text-sm" style="padding: 20px;"><pre style="line-height: 125%; margin: 0;"><span></span><span style="color: #75715e">// get all data needed.</span><br><span style="color: #66d9ef">const</span> <span style="color: #a6e22e">data</span> <span style="color: #f92672">=</span> <span style="color: #f8f8f2">{</span><br>    <span style="color: #a6e22e">code</span><span style="color: #f92672">:</span> <span style="color: #e6db74">&quot;const greet = &#39;Hello World!&#39;&quot;</span><span style="color: #f8f8f2">,</span><br>    <span style="color: #a6e22e">language</span><span style="color: #f92672">:</span> <span style="color: #e6db74">&#39;javascript&#39;</span><span style="color: #f8f8f2">,</span><br>    <span style="color: #a6e22e">getFormat</span><span style="color: #f92672">:</span> <span style="color: #e6db74">&#39;html&#39;</span><span style="color: #f8f8f2">,</span><br>    <span style="color: #a6e22e">style</span><span style="color: #f92672">:</span> <span style="color: #e6db74">&#39;paraiso-dark&#39;</span><span style="color: #f8f8f2">,</span><br>    <span style="color: #a6e22e">lineNo</span><span style="color: #f92672">:</span> <span style="color: #e6db74">&#39;none&#39;</span><span style="color: #f8f8f2">,</span><br>    <span style="color: #a6e22e">css</span><span style="color: #f92672">:</span> <span style="color: #e6db74">&#39;inline&#39;</span><span style="color: #f8f8f2">,</span><br>    <span style="color: #a6e22e">divClass</span><span style="color: #f92672">:</span> <span style="color: #e6db74">&#39;player&#39;</span><span style="color: #f8f8f2">,</span><br>    <span style="color: #a6e22e">hlLines</span><span style="color: #f92672">:</span> <span style="color: #f8f8f2">[],</span><br>    <span style="color: #a6e22e">noBackground</span><span style="color: #f92672">:</span> <span style="color: #66d9ef">false</span><span style="color: #f8f8f2">,</span><br><span style="color: #f8f8f2">};</span><br><span style="color: #75715e">// make a post request using fetch api.</span><br><span style="color: #a6e22e">fetch</span><span style="color: #f8f8f2">(</span><span style="color: #e6db74">&#39;https://api.justhighlight.com/highlighter/&#39;</span><span style="color: #f8f8f2">,</span> <span style="color: #f8f8f2">{</span><br>    <span style="color: #a6e22e">method</span><span style="color: #f92672">:</span> <span style="color: #e6db74">&#39;POST&#39;</span><span style="color: #f8f8f2">,</span><br>    <span style="color: #a6e22e">headers</span><span style="color: #f92672">:</span> <span style="color: #f8f8f2">{</span><span style="color: #e6db74">&#39;Content-Type&#39;</span><span style="color: #f92672">:</span> <span style="color: #e6db74">&#39;application/json&#39;</span><span style="color: #f8f8f2">},</span><br>    <span style="color: #a6e22e">body</span><span style="color: #f92672">:</span> <span style="color: #a6e22e">JSON</span><span style="color: #f8f8f2">.</span><span style="color: #a6e22e">stringify</span><span style="color: #f8f8f2">(</span><span style="color: #a6e22e">data</span><span style="color: #f8f8f2">),</span><br><span style="color: #f8f8f2">})</span><br>  <span style="color: #f8f8f2">.</span><span style="color: #a6e22e">then</span><span style="color: #f8f8f2">((</span><span style="color: #a6e22e">response</span><span style="color: #f8f8f2">)</span> <span style="color: #f8f8f2">=&gt;</span> <span style="color: #a6e22e">response</span><span style="color: #f8f8f2">.</span><span style="color: #a6e22e">json</span><span style="color: #f8f8f2">())</span><br>  <span style="color: #f8f8f2">.</span><span style="color: #a6e22e">then</span><span style="color: #f8f8f2">((</span><span style="color: #a6e22e">data</span><span style="color: #f8f8f2">)</span> <span style="color: #f8f8f2">=&gt;</span> <span style="color: #f8f8f2">{</span><br>      <span style="color: #75715e">// make use of the returned response as you will.</span><br>      <span style="color: #66d9ef">this</span><span style="color: #f8f8f2">.</span><span style="color: #a6e22e">highlighted</span> <span style="color: #f92672">=</span> <span style="color: #a6e22e">data</span><span style="color: #f8f8f2">.</span><span style="color: #a6e22e">result</span><span style="color: #f8f8f2">.</span><span style="color: #a6e22e">data</span><span style="color: #f8f8f2">;</span><br>  <span style="color: #f8f8f2">})</span><br>  <span style="color: #f8f8f2">.</span><span style="color: #66d9ef">catch</span><span style="color: #f8f8f2">((</span><span style="color: #a6e22e">error</span><span style="color: #f8f8f2">)</span> <span style="color: #f8f8f2">=&gt;</span> <span style="color: #f8f8f2">{</span><br>      <span style="color: #75715e">// catch any error what so ever and debug it.</span><br>      <span style="color: #a6e22e">console</span><span style="color: #f8f8f2">.</span><span style="color: #a6e22e">log</span><span style="color: #f8f8f2">(</span><span style="color: #a6e22e">error</span><span style="color: #f8f8f2">);</span><br>  <span style="color: #f8f8f2">});</span><br></pre></div>
        </div>
      </div>
    </div>
    <!-- end of example -->
    <!-- start of features available -->
    <div id="features-section" class="my-6 flex flex-col space-y-6">
      <h1 class="text-gray-700 dark:text-gray-300 text-3xl sm:text-4xl font-semibold">Features</h1>
      <!-- start of formats available -->
      <div id="formats-features" class="flex flex-col space-y-5">
        <h3 class="text-2xl font-medium text-gray-700 dark:text-gray-300 border-b border-gray-300">Formats available</h3>
        <ul class="text-sm sm:text-base text-gray-600 dark:text-gray-400">
          <li v-for="form in formats" :key="form.short" class="list-disc list-inside">{{form.short}}
            <a v-if="form.full" :href="form.url" target="_blank" class="text-cyan-400 hover:text-cyan-600"> - {{form.full}}</a>
            <i v-if="form.url" class="fas fa-external-link-alt text-xs ml-1"></i>
          </li>
        </ul>
      </div>
      <!-- end of formats available -->
      <!-- start of styles available -->
      <div id="styles-section" class="flex flex-col space-y-5">
        <h3 class="text-2xl font-medium text-gray-700 dark:text-gray-300 border-b border-gray-300">Styles available</h3>
        <div class="flex flex-wrap text-sm sm:text-base text-gray-600 dark:text-gray-400 text-justify">
          <span v-for="style in styles" :key="style" class="mr-2">{{style}}</span>
        </div>
      </div>
      <!-- end of styles available -->
      <!-- start of important info -->
      <div class="my-6 flex flex-col space-y-6">
        <h3 class="text-2xl font-medium text-gray-700 dark:text-gray-300 border-b border-gray-300">Important</h3>
        <div>
          <p class="text-sm sm:text-base text-gray-600 dark:text-gray-400">Please note concerning the <b>formats</b> available, That:</p>
          <ul class="my-4 flex flex-col space-y-3 text-sm sm:text-base text-gray-600 dark:text-gray-400">
            <li class="list-inside list-disc">
              The <b>HTML</b> format should be used when playing with the
              <router-link :to="{name: 'Home'}" class="text-cyan-400 hover:text-cyan-600">justHighlight code editor</router-link> as this is easily formatted to
              represent the code snippet by the browser.
            </li>
            <li class="list-inside list-disc">
              The <b>SVG</b> format is still experimental as indicated in the official
              <a href="https://pygments.org/docs/formatters/#SvgFormatter" target="_blank" class="text-cyan-400 hover:text-cyan-600">pygments formatters documentation</a>
              <i class="fas fa-external-link-alt text-xs ml-1"></i>
            </li>
            <li class="list-inside list-disc text">The <b>Text</b> format is simply returned to you as written. But why is it an option then?</li>
            <li class="list-inside list-disc">As for the rest of the formatters, please use in environments where they will be fully represented.</li>
            <li class="list-inside list-disc">All code snippet written on the code editor is never saved neither is it ever executed.</li>
          </ul>
        </div>
      </div>
      <!-- end of important info -->
    </div>
    <!-- end of features available -->
    <!-- start of footer -->
    <div class="border-t border-gray-300 dark:border-gray-700 pt-4">
      <base-footer />
    </div>
    <!-- end of footer -->
  </div>
</template>

<script>
import BaseFooter from '../components/BaseFooter.vue';

export default {
  name: 'DocsDetail',
  components: { BaseFooter },
  data() {
    return {
      formats: [
        // features formats list
        { short: 'HTML', full: 'Hypertext Markup Language.', url: 'https://www.w3schools.com/html/html_intro.asp' },
        { short: 'SVG', full: 'Scalable Vector Graphics.', url: 'https://developer.mozilla.org/en-US/docs/Web/SVG' },
        { short: 'BBCode', full: 'Bulletin Board Code.', url: 'https://en.wikipedia.org/wiki/BBCode' },
        { short: 'RTF', full: 'Rich Text Format.', url: 'https://en.wikipedia.org/wiki/Rich_Text_Format' },
        { short: 'Terminal256.', full: null, url: null },
        { short: 'Terminal.', full: null, url: null },
        { short: 'Text.', full: null, url: null },
        { short: 'IRC.', full: null, url: null },
      ],
      styles: [
        'abap', 'algol', 'algol_nu', 'arduino', 'autumn', 'borland', 'bw', 'colorful', 'default', 'emacs', 'friendly',
        'fruity', 'igor', 'inkpot', 'lovelace', 'manni', 'monokai', 'murphy', 'native', 'paraiso-dark', 'paraiso-light',
        'pastie', 'perldoc', 'rainbow_dash', 'rrt', 'sas', 'solarized-dark', 'solarized-light', 'stata', 'stata-dark',
        'stata-light', 'tango', 'trac', 'vim', 'vs', 'xcode',
      ],
    };
  },
};
</script>
