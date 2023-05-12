import Vue from 'vue'
import VueRouter from 'vue-router'
import MovieView from '../views/MovieView.vue'
import WatchListView from '../views/WatchListView.vue'

Vue.use(VueRouter)

const routes = [

  {
    path: '/',
    name: 'movie',
    component: MovieView
  },
  {
    path: '/watchlist',
    name: 'watchlist',
    component: WatchListView
  },
  {
    path: '/weather',
    name: 'weather',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "weather" */ '../views/WeatherView.vue')
  },
  {
    path: '/random',
    name: 'random',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "random" */ '../views/RandomView.vue')
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
