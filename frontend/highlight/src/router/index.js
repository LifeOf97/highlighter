import { createRouter, createWebHistory } from 'vue-router';
import Home from '../views/Home.vue';

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home,
    meta: {
      title: 'Welcome to JustHighlight.',
    },
  },
  {
    path: '/docs',
    name: 'Docs',
    component: () => import(/* webpackChunkName: "docs" */ '../views/Docs.vue'),
    meta: {
      title: 'Documentation | JustHighlight.',
    },
  },
  {
    path: '/:pathMatch(.*)*',
    name: 'NotFound',
    component: () => import(/* webpackChunkName: "notfound" */ '../views/NotFound.vue'),
    meta: {
      title: 'Error | Page not found.',
    },
  },
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
});

router.afterEach((to) => {
  // update the title of every route page.
  document.title = to.meta.title || 'JustHighlight';
});

export default router;
