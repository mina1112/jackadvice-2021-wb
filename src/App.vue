<template>
  <v-app>
    <!-- <div
      id="nav"
      class="tab-area-base">
      <ul class="tab-menu-base">
        <li><router-link to="/">Login</router-link></li>
        <li><router-link to="/list">Todo List</router-link></li>
        <li><router-link to="/detail">Todo Detail</router-link></li>
      </ul>
    </div> -->
    <router-view />
  </v-app>
  <!-- <div id="app">
            <img alt="Vue logo" src="./assets/logo.png">
            <HelloWorld msg="ほげほげ"/>
       </div> -->
</template>

<script>
// import HelloWorld from './components/HelloWorld.vue';
// import Login from './components/Login.vue';
// import TodoDetail from './vomponents/TodoDetail.vue';
// import TodoList from './components/TodoList.vue';

// export default {
//   name: 'App',

//   components: {
//     HelloWorld,
//     Login,
//     TodoDetail,
//     TodoList,
//   }
// }
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
#nav {
  text-align: center;
}
.tab-menu-base {
  margin: 0;
  padding: 0;
}
#nav ul li {
  list-style: none;
  display: inline-block;
  width: 18%;
  min-width: 90px;
}
</style>
