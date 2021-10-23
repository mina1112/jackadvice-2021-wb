<template>
  <div class="detail">
    <!--ここにhtmlを書いてね-->
    <html lang="ja">
    <head>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width,initial-scale=1">
        <title>ToDo</title>
    </head>
    <body>
        <header>
            <img src="#">
        </header>
        <div class="title" id="goal">
            タスク：<input type="text" style="border:none" v-model="title">
        </div>
        <div class="goalDate" id="app">
            <p class="caption">終わらせたい日時</p>
            <input type="datetime-local" style="border:none" v-model="date1">
        </div>
        <div class="limitDate">
            <p class="caption">締め切り日時</p>
            <input type="datetime-local" style="border:none" v-model="date2">
        </div>
        <div class="notification">
            <p class="caption">通知</p>
            <input type="datetime-local" style="border:none" v-model="date3">
        </div>
        <div class="memo">メモ</div>
        <div class="form" id="note">
            <textarea cols="47" style="border:none" v-model="memo"></textarea>
        </div>
        <div class="finish">
            <a href="#">Done!</a>
        </div>
    </body>
    </html>
  </div>
</template>

<script>
// ここにjavascriptを書いてね
export default {
    name: 'TodoList',
    data(){
        return {
            title: "課題１を終わらせる",
            date1: '',
            date2: '',
            date3: '',
            memo: 'なし'
        }
    },
    watch: {
        title: function() {
            localStorage.setItem('title', JSON.stringify(this.title));
        },
        date1: function() {
            localStorage.setItem('date1', JSON.stringify(this.date1));
        },
        date2: function() {
            localStorage.setItem('date2', JSON.stringify(this.date2));
        },
        date3: function() {
            localStorage.setItem('date3', JSON.stringify(this.date3));
        },
        memo: function() {
            localStorage.setItem('memo', JSON.stringify(this.memo));
        },
    },
    mounted: function(){
        this.title = JSON.parse(localStorage.getItem('title'))  || [];
        this.date1 = JSON.parse(localStorage.getItem('date1'))  || [];
        this.date2 = JSON.parse(localStorage.getItem('date2'))  || [];
        this.date3 = JSON.parse(localStorage.getItem('date3'))  || [];
        this.memo = JSON.parse(localStorage.getItem('memo'))  || [];
    },
}
</script>

<style scoped>
/* ここにcssを書いてね */
header {
    height: 50px;
    background-color:  #ea5532;
}

img {
    height: 40px;
    padding: 5px 0 0 10px;
}

.title{
    font-size: 20px;
    padding-top: 15px;
    padding-bottom: 15px;
    padding-left: 10px;
    color: rgb(143, 143, 143);
}

.goalDate, .limitDate, .notification {
    display: flex;
    border-top: 1px solid #ea5532;
    justify-content: space-between;
    color: rgb(143, 143, 143);
}

.caption{
    padding-left: 10px;
}

.memo{
    border-top: 1px solid #ea5532;
    padding-top: 16px;
    padding-left: 10px;
    color: rgb(143, 143, 143);
}

.form {
    border-bottom: 1px solid #ea5532;
    padding-top: 16px;
    padding-bottom: 16px;
    padding-left: 10px;
}


.finish {
    background-color: #ea5532;
    width: 150px;
    height: 40px;
    border-radius: 8px;
    line-height: 40px;
    text-align: center;
    margin:0 auto;
    margin-top: 16px;
    box-shadow: 1px 1px #b3381c;
}

.finish:active {
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

input[type="datetime-local"] {
    height: 30px;
    margin-top: 12px;
    margin-right: 10px;
    width: 185px;
}

input[type="text"] {
    font-size: 20px;
}
</style>