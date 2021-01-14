import { createRouter, createWebHistory } from 'vue-router';
import PageNotFound from '../views/NotFound.vue';
import Home from '../views/Home.vue';
import Docs from '../views/Docs.vue';

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home,
    meta: { title: 'Welcome to JustHighlight.' },
  },
  {
    path: '/docs',
    name: 'Docs',
    component: Docs,
    meta: { title: 'Documentation | JustHighlight.' },
  },
  {
    path: '/:pathMatch(.*)*',
    name: 'NotFound',
    component: PageNotFound,
    meta: { title: 'Error | Page not found.' },
  },
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
});

router.afterEach((to) => {
  // update the title of every page routed to.
  document.title = to.meta.title || 'JustHighlight';
});

export default router;
