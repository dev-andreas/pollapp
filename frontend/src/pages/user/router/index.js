import { createRouter, createWebHashHistory } from 'vue-router'
import Home from '../views/Home.vue'

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/settings',
    name: 'UserSettings',
    component: () => import('../views/UserSettings.vue')
  },

  // catchall 404
  {
    path: '/:catchAll(.*)',
    redirect: '/',
  }
]

const router = createRouter({
  history: createWebHashHistory(),
  mode: 'history',
  routes
})

export default router