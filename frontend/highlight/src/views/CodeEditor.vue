<template>
<!-- eslint-disable max-len -->
    <div class="w-full h-full shadow-2xl rounded-md overflow-hidden">
      <form action="" method="post" @submit.prevent class="w-full flex flex-col">
        <!-- start of editor options -->
        <div id="editor-options" class="flex-1 flex flex-wrap px-3 py-2 relative">
          <base-text-select-menu
            :label="'Language'"
            :placeholder="'---'"
            :options="getLanguages"
            @option-selected="setLanguage"
            class="flex-1" />
          <base-text-select-menu
            :label="'Formats'"
            :placeholder="'---'"
            :options="getFormats"
            @option-selected="setFormat"
            class="mr-2 flex-initial" />
          <base-text-select-menu
            :label="'Styles'"
            :placeholder="'---'"
            :options="getStyles"
            @option-selected="setStyle"
            class="flex-initial" />
        </div>
        <!-- end of editor options -->
        <!-- start of editor div -->
        <div class="flex-1 h-66">
          <!-- start of button to open code editor -->
          <div v-if="codeGround" class="h-66 border-t border-gray-600 flex justify-center items-center bg-gray-800 bg-opacity-50 group">
            <button
              type="button"
              @click="openCode()"
              class="px-2 py-1 rounded-md text-lg text-white font-medium bg-gradient-to-tr from-blue-600 via-pink-500 to-red-500
              group-hover:animate-bounce focus:outline-none">
                Code Ground
            </button>
          </div>
          <!-- end of button to open editor -->
          <!-- start of code editor -->
          <transition
            name="show-editor"
            enter-from-class="scale-0 opacity-0"
            enter-to-class=""
            enter-active-class="transition transform duration-200"
            leave-to-class="scale-0 opacity-0"
            leave-from-class=""
            leave-active-class="transition transform duration-200">
            <div v-if="!codeGround">
              <text-editor
                autofocus
                :rows="10"
                v-model="code"
                class="w-full h-auto resize-none outline-none focus:border focus:border-teal-500 hover:border-2 hover:border-teal-500 text-white bg-gray-700 p-4" />
            </div>
          </transition>
          <!-- end of code editor -->
        </div>
        <!-- end of editor div -->
        <!-- start of editor submit button -->
        <div v-if="!codeGround" class="py-2 flex justify-end mr-6">
          <button
            type="button"
            @click="highlight()"
            class="px-2 py-1 bg-gradient-to-tr from-blue-600 via-pink-500 to-red-500 shadow-lg rounded-lg inline-flex place-items-center space-x-2
            hover:from-red-500 hover:via-pink-500 hover:to-blue-600 transition duration-500 ease-out focus:outline-none">
            <span class="font-semibold text-base text-white">Highlight</span>
            <i class="fas fa-long-arrow-alt-right text-lg text-black"></i>
          </button>
        </div>
        <!-- end of editor submit button -->
      </form>
    </div>
</template>

<script>
import { mapActions, mapGetters } from 'vuex';
import BaseTextSelectMenu from '../components/BaseTextSelectMenu.vue';
import TextEditor from '../components/TextEditor.vue';
// import SelectMenu from '../components/SelectMenu.vue';

export default {
  name: 'CodeEditor',
  data() {
    return {
      codeGround: true,
      code: '',
      language: '',
      format: '',
      style: '',
    };
  },
  components: { BaseTextSelectMenu, TextEditor },
  computed: {
    ...mapGetters(['getLanguages', 'getFormats', 'getStyles']),
  },
  methods: {
    ...mapActions([
      'fetchLanguages', 'fetchFormats',
      'fetchStyles', 'highlightCode',
    ]),
    openCode() { this.codeGround = false; },
    setLanguage(value) { this.language = value; },
    setFormat(value) { this.format = value; },
    setStyle(value) { this.style = value; },
    highlight() {
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
  created() {
    this.fetchLanguages();
    this.fetchFormats();
    this.fetchStyles();
  },
};
</script>
