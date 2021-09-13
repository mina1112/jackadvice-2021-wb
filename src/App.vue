<template>
  <v-app>
    <v-main>
      <v-container>
        <div class="content" id="login">
          <Login />
        </div>
        <!-- <div id="app">
          <img alt="Vue logo" src="./assets/logo.png">
          <HelloWorld msg="ほほげほげ"/>
        </div> -->
      </v-container>
    </v-main>
  </v-app>
</template>

<script>
// import HelloWorld from './components/HelloWorld.vue';
import Login from './components/Login.vue';
// import TodoDetail from './vomponents/TodoDetail.vue';
// import TodoList from './components/TodoList.vue';

export default {
  name: 'App',

  components: {
    // HelloWorld,
    Login,
    // TodoDetail,
    // TodoList,
  }
}
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
</style>
