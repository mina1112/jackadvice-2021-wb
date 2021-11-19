<template>
  <v-app>
    <div id="app">
    <!-- <div
      id="nav"
      class="tab-area-base">
      <ul class="tab-menu-base">
        <li><router-link to="/">Login</router-link></li>
        <li><router-link to="/list">Todo List</router-link></li>
        <li><router-link to="/detail">Todo Detail</router-link></li>
      </ul>
    </div> -->
      <router-view/>
    </div>
  </v-app>
</template>

<style lang="scss">
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
