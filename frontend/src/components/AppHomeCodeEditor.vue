<script setup>
/* eslint-disable */
import { ref, reactive, onMounted } from 'vue';
import { useRouter } from 'vue-router';
import { useHighlighterStore } from '../stores/highlight';
import AppSelectMenu from './AppSelectMenu.vue';
import AppTextArea from './AppTextArea.vue';
import IconLongRight from './icons/IconLongRight.vue';
import { gsap } from 'gsap'

// emits
const emits = defineEmits(["updateComponent"])

// refs
const openEditor = ref(false)
const language = reactive({value: '', error: null})
const format = reactive({value: '', error: null})
const style = reactive({value: '', error: null })
const code = reactive({value: '', error: null})
const codeEditor = ref(null)

// stores
const highlighterStore = useHighlighterStore()

// route/routers
const router = useRouter()

// methods
const highlight = () => {
  const data = {
    language: language.value,
    getFormat: format.value,
    style: style.value,
    code: code.value,
    noBackground: false,
  }

  if (!highlighterStore.languages.data.includes(language.value.toLowerCase())) language.error = `${language.value} is not a valid option`
  else language.error = null
  if (!highlighterStore.formats.data.includes(format.value.toLowerCase())) format.error = `${format.value} is not a valid option`
  else format.error = null
  if (!highlighterStore.styles.data.includes(style.value.toLowerCase())) style.error = `${style.value} is not a valid option`
  else style.error = null

  if (language.error == null && format.error == null && style.error == null) {
    highlighterStore.highlightCode(data)
    emits("updateComponent", 'AppHomeCodeResult')
  }
}

const animCodeEditor = () => {
  gsap.from(codeEditor.value, {y: 50, opacity: 0, duration: 1, delay: 0.5})
}

// hooks
onMounted(() => {
  animCodeEditor()
})
</script>

<template>
  <main ref="codeEditor" class="-mt-20 w-11/12 mx-auto h-full md:-mt-0 md:absolute md:-top-20 md:w-1/2 md:right-0 lg:right-10 xl:right-20">

    <form @submit.prevent="highlight()" class="w-full flex flex-col shadow-xl shadow-slate-400 dark:shadow-slate-900">

      <div class="w-full flex flex-col gap-3 p-4 bg-slate-700 rounded-t-md border-b border-slate-600 sm:flex-row lg:gap-7">
        <AppSelectMenu @selected-option="(option) => language.value = option" @refresh="highlighterStore.getLanguages()" v-model="language.value" :input-error="language.error" :loading="highlighterStore.languages.loading" :menu-error="highlighterStore.languages.error" :options="highlighterStore.languages.data" :required="true" label="Language" />
        <AppSelectMenu @selected-option="(option) => format.value = option" @refresh="highlighterStore.getFormats()" v-model="format.value" :input-error="format.error" :loading="highlighterStore.formats.loading" :menu-error="highlighterStore.formats.error" :options="highlighterStore.formats.data" :required="true" label="Format" />
        <AppSelectMenu @selected-option="(option) => style.value = option" @refresh="highlighterStore.getStyles()" v-model="style.value" :input-error="style.error" :loading="highlighterStore.styles.loading" :menu-error="highlighterStore.styles.error" :options="highlighterStore.styles.data" :required="true" label="Style" />
      </div>

      <!-- start of editor -->
      <div class="w-full h-full bg-slate-700">
        <div v-if="!openEditor" class="w-full h-60 flex items-center justify-center group">
          <button @click.prevent="openEditor = true" type="button" class="text-sm text-white px-4 py-2 rounded-md bg-slate-600 shadow-xl transition-all duration-200 group-hover:animate-bounce hover:bg-slate-500 md:text-sm">Editor</button>
        </div>

        <transition
          name="editor"
          enter-from-class="scale-0 opacity-0"
          enter-active-class="transition-all duration-200"
          leave-to-class="scale-0 opacity-0"
          leave-active-class="transition-all duration-200">
            <AppTextArea v-if="openEditor" v-model="code.value" rows="10" placeholder="Enter code to highlight..." />
        </transition>

      </div>
      <!-- end of editor -->

      <div v-if="openEditor" class="w-full flex px-6 py-3 items-center justify-between rounded-b-md bg-slate-700">
          <div>
            <span v-if="highlighterStore.highlighter.error" class="text-xs sm:text-sm font-semibold text-red-500">{{highlighterStore.highlighter.error}}</span>
          </div>

          <button
            type="submit"
            class="text-sm group flex items-center gap-3 text-white px-4 py-2 rounded-md bg-slate-600 shadow-xl transition-all duration-200 hover:bg-slate-500 group-hover:animate-bounce md:text-sm">
              <p>Highlight</p>
              <IconLongRight class="w-7 h-7 fill-slate-400 group-hover:animate-bounce-x" />
          </button>
      </div>

    </form>

  </main>
</template>