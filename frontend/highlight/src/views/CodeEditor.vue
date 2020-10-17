<template>
<!-- eslint-disable max-len -->
    <div class="w-full h-full shadow-2xl rounded-md overflow-hidden">
      <form action="" method="post" @submit.prevent class="w-full flex flex-col">
        <!-- start of editor options -->
        <div id="editor-options" class="flex-1 flex flex-wrap p-3">
          <select-menu label-name="Language" class="flex-1"/>
          <select-menu label-name="Format" class="flex-initial mr-2"/>
          <select-menu label-name="style" class="flex-initial"/>
        </div>
        <!-- end of editor options -->
        <!-- start of editor div -->
        <div class="flex-1 h-66">
          <!-- start of button to open code editor -->
          <div v-if="codeGround" class="h-full border-t border-gray-600 flex justify-center items-center bg-gray-800 bg-opacity-50 group">
            <button
              type="button"
              @click="openEditor()"
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
                class="w-full h-auto resize-none outline-none focus:border-2 focus:border-teal-500 hover:border-2 hover:border-teal-500 text-white bg-gray-700 p-4" />
            </div>
          </transition>
          <!-- end of code editor -->
        </div>
        <!-- end of editor div -->
        <!-- start of editor submit button -->
        <div v-if="!codeGround" class="py-2 flex justify-end mr-6">
          <button
            type="button"
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
import SelectMenu from '../components/SelectMenu.vue';
import TextEditor from '../components/TextEditor.vue';

export default {
  name: 'CodeEditor',
  data() {
    return {
      codeGround: true,
      code: '',
    };
  },
  components: {
    SelectMenu,
    TextEditor,
  },
  methods: {
    openEditor() {
      this.codeGround = false;
    },
  },
};
</script>
