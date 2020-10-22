<template>
<!-- eslint-disable max-len -->
    <div class="w-full h-full">
      <form action="" method="post" @submit.prevent class="w-full flex flex-col">
        <!-- start of code editor options -->
        <div id="editor-options" class="flex-1 flex flex-wrap px-3 py-2 relative bg-gray-800">
          <base-text-select-menu
            :label="'Language:'"
            :placeholder="'---'"
            :options="getLanguages"
            :position="'left-0'"
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
          <div v-if="codeGround" class="h-66 border-t border-gray-600 flex justify-center items-center bg-gray-800 bg-opacity-50 group">
            <button
              type="button"
              @click="openEditor()"
              class="px-2 py-1 rounded-md text-lg text-white font-medium bg-gradient-to-tr from-blue-600 via-pink-500 to-red-500
              group-hover:animate-bounce focus:outline-none">
                Code Ground
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
            <div v-if="!codeGround">
              <text-editor
                autofocus
                :rows="10"
                v-model="code"
                placeholder="Enter code here..."
                class="w-full h-auto resize-none outline-none text-white bg-gray-700 p-4 placeholder-gray-400" />
            </div>
          </transition>
          <!-- end of code editor contained within a transition effect-->
          <!-- end of code editor div -->
        </div>
        <!-- start of code editor submit button div -->
        <div
          v-if="!codeGround"
          class="p-2 self-end">
          <button
            @click="highlight()"
            class="px-2 py-1 bg-gradient-to-tr from-blue-600 via-pink-500 to-red-500 shadow-lg rounded-lg inline-flex place-items-center space-x-2
            hover:from-red-500 hover:via-pink-500 hover:to-blue-600 transition duration-500 ease-out focus:outline-none">
            <span class="font-semibold text-base text-white">Highlight</span>
            <i class="fas fa-long-arrow-alt-right text-lg text-black"></i>
          </button>
        </div>
        <!-- end of code editor submit button -->
      </form>
    </div>
</template>

<script>
import { mapActions, mapGetters } from 'vuex';
import BaseTextSelectMenu from '../components/BaseTextSelectMenu.vue';
import TextEditor from '../components/TextEditor.vue';

export default {
  name: 'CodeEditor',
  data() {
    return {
      code: '',
      style: '',
      format: '',
      language: '',
      codeGround: true,
    };
  },
  components: { BaseTextSelectMenu, TextEditor },
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
      // method to open the code editor by setting the codeGround data Object
      // to false
      this.codeGround = false;
    },
    setLanguage(value) {
      // method to update the selected language option
      this.language = value;
    },
    setFormat(value) {
      // method to update the selected format option
      this.format = value;
    },
    setStyle(value) {
      // method to update the selected style option
      this.style = value;
    },
    highlight() {
      // method to call the store action passing in the required payload
      // to highlight the code snippet.
      this.highlightCode({
        loading: { status: true },
        highlight: {
          code: this.code.toLowerCase(),
          style: this.style.toLowerCase(),
          format: this.format.toLowerCase(),
          language: this.language.toLowerCase(),
        },
      });
    },
  },
};
</script>
