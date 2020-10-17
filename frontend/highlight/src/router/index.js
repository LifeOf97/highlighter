import { createRouter, createWebHistory } from 'vue-router';
import Home from '../views/Home.vue';

const routes = [
  {
    path: '/',
    name: 'Home',
    alias: '/home',
    // redirect to the code editor to always make it visible whenever route changes.
    redirect: { name: 'CodeEditor' },
    component: Home,
    children: [
      {
        path: '/home',
        name: 'CodeEditor',
        component: () => import(/* webpackChunkName: "codeeditor" */ '../views/CodeEditor.vue'),
      },
    ],
  },
  {
    path: '/docs',
    name: 'Docs',
    component: () => import(/* webpackChunkName: "docs" */ '../views/Docs.vue'),
  },
  {
    path: '/:pathMatch(.*)*',
    name: 'NonFound',
    component: () => import(/* webpackChunkName: "notfound" */ '../views/NotFound.vue'),
  },
  // {
  // path: '/about',
  // name: 'About',
  // route level code-splitting
  // this generates a separate chunk (about.[hash].js) for this route
  // which is lazy-loaded when the route is visited.
  //   component: () => import(/* webpackChunkName: "about" */ '../views/About.vue'),
  // },
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
});

export default router;
