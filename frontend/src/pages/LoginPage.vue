<template>
<div>
    <MyHeader></MyHeader>
    <div class="container">
        <div class="logo">
            <img src="../assets/hanamar_icon.jpg">
        </div>
        <div class="logIn">
            <a href="#">log in</a>
        </div>
        <div class="signIn">
            <a href="#">sign up</a>
        </div>
    </div>
</div>
</template>
<script>
import MyHeader from '../components/Header.vue'

export default {
  name: 'Login',
  components: {
      MyHeader
  }
}
</script>

<style scoped>
div {
    margin: 0 auto;
    text-align: center;
}

.logIn {
    background-color: #ef845d;
    width: 250px;
    height: 40px;
    border-radius: 8px;
    line-height: 40px;
    box-shadow: 2px 2px #882906;
}

.signIn {
    background-color: #3f51b5;
    width: 250px;
    height: 40px;
    border-radius: 8px;
    line-height: 40px;
    box-shadow: 2px 2px #020e55;
    top: 1px;
    left: 1px;
}

.signIn:active {
    box-shadow: none;
    position: relative;
    top: 1px;
    left: 1px;
}

a {
    text-decoration: none;
    color: white !important;
    display: block;
}

@media screen and (min-width:481px) {
    img {
        height: 400px;
        padding-top: 64px;
    }

    .logIn {
        margin-top: 96px;
    }

    .signIn {
        margin-top: 64px;
    }
}

@media screen and (max-width:480px) {
	.container {
        margin: 0 auto;
    }

    img {
        width: 75vw;
        padding-top: 3rem;
    }

    .logIn {
        margin-top: 4rem;
    }

    .signIn {
        margin-top: 3rem;
    }
}
</style>