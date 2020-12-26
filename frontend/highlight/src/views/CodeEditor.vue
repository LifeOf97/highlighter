<template>
<!-- eslint-disable max-len -->
    <div class="w-full h-full bg-blueGray-700 dark:bg-blueGray-200">
      <form method="post" @submit.prevent class="w-full flex flex-col">
        <!-- start of code editor options -->
        <div id="editor-options" class="flex-1 flex flex-wrap px-3 py-2 relative bg-blueGray-700 dark:bg-blueGray-200">
          <base-text-select-menu
            :label="'Language:'"
            :placeholder="'---'"
            :options="getLanguages"
            @option-selected="setLanguage"
            class="flex-1" />
          <base-text-select-menu
            :label="'Return code in:'"
            :placeholder="'---'"
            :options="getFormats"
            @option-selected="setFormat"
            class="mr-2 flex-initial" />
          <base-text-select-menu
            :label="'Style:'"
            :placeholder="'---'"
            :options="getStyles"
            @option-selected="setStyle"
            class="flex-initial" />
        </div>
        <!-- end of code editor options -->
        <!-- start of code editor text div -->
        <div class="flex-1 h-66">
          <!-- start of button to open code editor -->
          <div v-if="codeEditor" class="h-66 border-t border-gray-400 dark:border-coolGray-300 flex justify-center items-center bg-blueGray-700 dark:bg-blueGray-200 group">
            <button type="button" @click="openEditor()"
              class="px-2 py-1 rounded-md text-lg text-white font-medium bg-gradient-to-tr from-blue-600 via-pink-500 to-red-500
              group-hover:animate-bounce focus:outline-none">Code Editor
            </button>
          </div>
          <!-- end of button to open code editor -->
          <!-- start of code editor contained within a transition effect-->
          <transition
            name="show-editor"
            enter-from-class="scale-0 opacity-0"
            enter-to-class=""
            enter-active-class="transition transform duration-300"
            leave-to-class="scale-0 opacity-0"
            leave-from-class=""
            leave-active-class="transition transform duration-300">
            <div v-if="!codeEditor">
              <base-text-editor
                autofocus
                :rows="10"
                ref="texteditor"
                v-model="code"
                placeholder="Enter your code here..."
                class="w-full h-auto resize-none outline-none text-white dark:text-black bg-blueGray-500 dark:bg-blueGray-300 p-4 placeholder-blueGray-200 dark:placeholder-blueGray-700" />
            </div>
          </transition>
          <!-- end of code editor contained within a transition effect-->
          <!-- end of code editor div -->
        </div>
        <!-- start of code editor submit button div -->
        <div v-if="!codeEditor" class="p-2 flex justify-between">
          <!-- start of div to handle errors -->
          <div class="flex-1">
            <transition
              name="error"
              enter-to-class=""
              enter-from-class="opacity-0 translate-y-5"
              enter-active-class="transition transform duration-100"
              leave-from-class=""
              leave-to-class="opacity-0 translate-y-5"
              leave-active-class="transition transform duration-100">
              <div v-if="error.state">
                <i class="fas fa-exclamation-circle text-md text-gray-200 dark:text-gray-600 mr-1"></i>
                <span class="text-xs sm:text-sm font-semibold text-red-400">{{error.message}}</span>
              </div>
            </transition>
          </div>
          <!-- end of div to handle errors -->
          <!-- start of code editor submit/highlight button -->
          <button
            type="submit"
            @click="highlight()"
            class="px-2 py-1 bg-gradient-to-tr from-blue-600 via-pink-500 to-red-500 shadow-lg rounded-lg inline-flex place-items-center space-x-2
            hover:from-red-500 hover:via-pink-500 hover:to-blue-600 transition duration-500 ease-out focus:outline-none">
            <span class="font-semibold text-base text-white">Highlight</span>
            <i class="fas fa-long-arrow-alt-right text-lg text-black"></i>
          </button>
          <!-- end of code editor submit/highlight button -->
        </div>
        <!-- end of code editor submit button -->
      </form>
    </div>
</template>

<script>
import { mapActions, mapGetters } from 'vuex';
import BaseTextSelectMenu from '../components/BaseTextSelectMenu.vue';
import BaseTextEditor from '../components/BaseTextEditor.vue';

export default {
  name: 'CodeEditor',
  emits: ['update:component'],
  data() {
    return {
      code: '',
      style: '',
      format: '',
      language: '',
      codeEditor: true,
      error: { state: false, message: '' },
    };
  },
  components: { BaseTextSelectMenu, BaseTextEditor },
  created() {
    this.fetchLanguages();
    this.fetchFormats();
    this.fetchStyles();
  },
  computed: {
    ...mapGetters(['getLanguages', 'getFormats', 'getStyles']),
  },
  methods: {
    ...mapActions([
      'fetchLanguages', 'fetchFormats',
      'fetchStyles', 'highlightCode',
    ]),
    openEditor() {
      // method to open the code editor by setting the codeEditor data Object
      // to false
      this.codeEditor = false;
    },
    setLanguage(value) {
      // this method is called when an option-selected event emitted from
      // the BaseTextSelectMenu component is captured on the
      this.language = value;
    },
    setFormat(value) {
      // this method is called when an option-selected event emitted from
      // the BaseTextSelectMenu component is captured.n
      this.format = value;
    },
    setStyle(value) {
      // this method is called when an option-selected event emitted from
      // the BaseTextSelectMenu component is captured.
      this.style = value;
    },
    highlight() {
      // method to call the store action passing in the required payload
      // to highlight the code snippet.
      if (this.code.length > 0) {
        // that is, if the code editor has some text in it then set the
        // error.state to false and error.message to an empty string.
        this.error.state = false;
        this.error.message = '';
        // then call the store action used to highlight the code snippet
        // passing in the relevant data.
        this.highlightCode({
          // pass highlight payload the data needed for highlighting.
          highlight: {
            code: this.code,
            style: this.style,
            format: this.format,
            language: this.language,
          },
        });
        // then emit an event to change the rendered component to the codeResult component.
        this.$emit('update:component', 'CodeResult');
      } else {
        // else if this statement returns false then set the error.state
        // to true and the error.message to a warning message.
        this.error.state = true;
        this.error.message = 'Please type in some code snippet.';
      }
    },
  },
};
</script>
