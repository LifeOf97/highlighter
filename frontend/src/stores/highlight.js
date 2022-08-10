/* eslint-disable */
import { defineStore } from 'pinia'
import axios from 'axios'


export const useHighlighterStore = defineStore({
  id: 'highlight',
  state: () => ({
    theme: localStorage.getItem('theme'),
    highlighter: {data: JSON.parse(localStorage.getItem("highlighter_highlighted")), component: "AppHomeCodeEditor", loading: false, error: null},
    languages: {data: JSON.parse(localStorage.getItem("highlighter_languages")), loading: false, error: null},
    formats: {data: JSON.parse(localStorage.getItem("highlighter_formats")), loading: false, error: null},
    styles: {data: JSON.parse(localStorage.getItem("highlighter_styles")), loading: false, error: null},
  }),
  actions: {
    async highlightCode(data) {
      this.highlighter.loading = true
      this.highlighter.error = null

      await axios.post("highlight/", data)
        .then((resp) => {
          this.highlighter.loading = false            
          this.highlighter.error = null
          this.highlighter.data = resp.data
          localStorage.setItem("highlighter_highlighted", JSON.stringify(resp.data))
        })
        .catch((err) => {
          this.highlighter.loading = false
          this.highlighter.loading = "An error occured"
        })
    },
    async getLanguages() {
      this.languages.loading = true
      this.languages.error = null

      await axios.get('options/languages/')
        .then((resp) => {
          this.languages.loading = false
          this.languages.error = null
          this.languages.data = resp.data.result
          localStorage.setItem("highlighter_languages", JSON.stringify(resp.data.result))
        })
        .catch((err) => {
          this.languages.loading = false
          this.languages.error = "An error occured"
        })
    },
    async getFormats() {
      this.formats.loading = true
      this.formats.error = null

      await axios.get('options/formats/')
        .then((resp) => {
          this.formats.loading = false
          this.formats.error = null
          this.formats.data = resp.data.result
          localStorage.setItem("highlighter_formats", JSON.stringify(resp.data.result))
        })
        .catch((err) => {
          this.formats.loading = false
          this.formats.error = "An error occured"
        })
    },
    async getStyles() {
      this.styles.loading = true
      this.styles.error = null

      await axios.get('options/styles/')
        .then((resp) => {
          this.styles.loading = false
          this.styles.error = null
          this.styles.data = resp.data.result
          localStorage.setItem("highlighter_styles", JSON.stringify(resp.data.result))
        })
        .catch((err) => {
          this.styles.loading = false
          this.styles.error = "An error occured"
        })
    }
  }
})
