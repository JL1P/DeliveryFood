import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/restaurante',
    name: 'Restaurante',
    component: () => import(/* webpackChunkName: "restaurante" */ '../views/Restaurante.vue')
  },
  {
    path: '/repartidor',
    name: 'Repartidor',
    component: () => import(/* webpackChunkName: "repartidor" */ '../views/Repartidor.vue')
  },
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router