<template>
  <div class="login">
    <!--ここにhtmlを書いてね-->
    <html>
    <head>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width,initial-scale=1">
        <title>ToDo</title>
    </head>
    <body>
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
    </body>
    </html>
  </div>
</template>
<script>
export default {
  name: 'Login'
}
// ここにjavascriptを書いてね
</script>

<style scoped>
/* ここにcssを書いてね */
div {
    max-width: 480px;
    margin: auto;
    text-align: center;
}

img{
    height: 300px;
    padding-top: 100px;
}

.logIn {
    margin-top: 100px;
    background-color: #ef845d;
    width: 250px;
    height: 40px;
    border-radius: 8px;
    line-height: 40px;
    box-shadow: 1px 1px #882906;
}

.signIn {
    margin-top: 75px;
    background-color: #ffffff;
    width: 250px;
    height: 40px;
    border-radius: 8px;
    line-height: 40px;
    box-shadow: 1px 1px #ef845d;
}

.logIn:active {
    box-shadow: none;
    position: relative;
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
    color: white;
    display: block;
}

@media screen and (min-width:481px) {
	.container{
        width: 480px;
        height: 900px;
        margin: 0 auto;
        background-color: rgb(248, 248, 247);
    }
}

@media screen and (max-width:480px) {
	.container{
        margin: 0 auto;
    }
}
</style>