/* eslint-disable */
import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView,
      meta: {title: 'Welcome | JustHighLight'}
    },
    {
      path: '/docs',
      name: 'docs',
      component: () => import('../views/DocsView.vue'),
      meta: {title: 'Documentation | JustHighLight'}
    }
  ]
})

router.beforeEach((to, from) => {
  // update the page title
  document.title = to.meta.title;
})

export default router
