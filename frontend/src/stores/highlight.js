/* eslint-disable */
import { defineStore } from 'pinia'
import axios from 'axios'


export const useHighlighterStore = defineStore({
  id: 'highlight',
  state: () => ({
    languages: {data: JSON.parse(localStorage.getItem("highlighter_languages")), loading: false, error: null},
    formats: {data: JSON.parse(localStorage.getItem("highlighter_formats")), loading: false, error: null},
    styles: {data: JSON.parse(localStorage.getItem("highlighter_styles")), loading: false, error: null},
  }),
  actions: {
    async getLanguages() {
      this.languages.loading = true
      this.languages.error = null

      await axios.get('options/languages/')
        .then((resp) => {
          this.languages.loading = false
          this.languages.error = null
          this.languages.data = resp.data
          localStorage.setItem("highlighter_languages", JSON.stringify(resp.data))
          console.log(resp)
        })
        .catch((err) => {
          this.languages.loading = false
          this.languages.error = "An error occured"
          console.log(err.response)
        })
    }
  }
})
