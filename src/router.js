import Vue from 'vue'
import Router from 'vue-router'
import Login from './components/Login.vue'
import TodoList from './components/TodoList.vue'
import Tododetail from './components/Tododetail.vue'

Vue.use(Router)

export default new Router({
  mode: 'history',
  routes: [
    {
      path: '/',
      name: 'login',
      component: Login
    },
    {
      path: '/list',
      name: 'list',
      component: TodoList
    },
    {
      path: '/detail',
      name: 'detail',
      component: Tododetail
    }
  ]
})