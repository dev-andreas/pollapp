import { createRouter, createWebHashHistory } from 'vue-router'
import Home from '../views/Home.vue'

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/settings/',
    name: 'UserSettings',
    component: () => import('../views/UserSettings.vue')
  },
  {
    path: '/new_poll/',
    name: 'NewPoll',
    component: () => import('../views/CreatePoll.vue')
  },
  {
    path: '/poll/',
    name: 'Poll',
    component: () => import('../views/Poll.vue')
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