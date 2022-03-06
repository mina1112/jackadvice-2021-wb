import Vue from 'vue'
import Router from 'vue-router'
import Login from '@/pages/LoginPage.vue'
import TodoIndexPage from '@/pages/TodoIndexPage.vue'
import TodoShowPage from '@/pages/TodoShowPage.vue'
import OnseiTourokuPage from '@/pages/OnseiTourokuPage.vue'

Vue.use(Router)

// ここでルーティングをしている。
const routes = [
  { path: '/', name: 'LoginPage', component: Login },
  { path: '/todo', name: 'TodoIndexPage', component: TodoIndexPage },
  // :id でそこにパラメータが入ることを宣言。
  // 遷移元は <router-link :to="{ name: 'TodoShowPage', params: { id: todo.id }}"/>でパラメータを渡して飛べる。
  // 遷移先では $route.params.id で取得できる。
  { path: '/todo/:id', name: 'TodoShowPage', component: TodoShowPage },
  { path: '/onsei', name: 'OnseiTourokuPage', component: OnseiTourokuPage},
]

export default new Router({
  mode: 'history',
  routes: routes
})