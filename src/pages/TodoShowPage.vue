<template>
  <div class="detail">
    <!--ここにhtmlを書いてね-->
    <html lang="ja">
    <head>
        <meta charset="utf-8">
        <title>ToDo</title>
      </head>
      <body>
        <header>
            <Header />
        </header>
        <div class="title">
            タスク:<input type="text" style="border:none" v-model="todo.title">
        </div>
        <div class="goalDate">
            <div class="caption">終わらせたい日時</div>
            <input type="datetime-local" style="border:none" v-model="todo.goalDate">
        </div>
        <div class="limitDate">
            <div class="caption">締め切り日時</div>
            <input type="datetime-local" style="border:none" v-model="todo.limitDate">
        </div>
        <div class="notification">
            <div class="caption">通知</div>
            <input type="datetime-local" style="border:none" v-model="todo.notification">
        </div>
        <div class="memo">メモ</div>
        <div class="form">
            <textarea cols="43" rows="4" style="border:none" v-model="todo.memo"></textarea>
        </div>
        <div class="btn">
            <v-btn
                class=white--text
                depressed
                color=#ea5532
                elevation="2"
                rounded
                @click="deleteItem(index)"
            >Done</v-btn>
            <v-btn
                class="ma-2"
                outlined
                color=#ea5532
                elevation="2"
                rounded
            >Save</v-btn>
        </div>
    </body>
    </html>
  </div>
</template>

<script>
import Header from "@/components/Header.vue";

export default {
    name: 'TodoShowPage',
     components: {
    Header
    },
    data(){
        return{
            todo: {},
        }
    },
    // watch: {
    //     title: function() {
    //         localStorage.setItem('title', JSON.stringify(this.title));
    //     },
    //     date1: function() {
    //         localStorage.setItem('date1', JSON.stringify(this.date1));
    //     },
    //     date2: function() {
    //         localStorage.setItem('date2', JSON.stringify(this.date2));
    //     },
    //     date3: function() {
    //         localStorage.setItem('date3', JSON.stringify(this.date3));
    //     },
    //     memo: function() {
    //         localStorage.setItem('memo', JSON.stringify(this.memo));
    //     },
    // },
    // mounted: function(){
    //     this.title = JSON.parse(localStorage.getItem('title'))  || [];
    //     this.date1 = JSON.parse(localStorage.getItem('date1'))  || [];
    //     this.date2 = JSON.parse(localStorage.getItem('date2'))  || [];
    //     this.date3 = JSON.parse(localStorage.getItem('date3'))  || [];
    //     this.memo = JSON.parse(localStorage.getItem('memo'))  || [];
    // },

  // by ほりしょー
  // mounted は最初のレンダリングで呼ばれる。
  // 将来的にはここでAPI(Django)を呼び出してデータを取得する。
  // 現状は sampleTodos をAPIと見立てて todo に代入してあげている。
  mounted() {
    const sampleTodos = [
      {
        title: '課題１を終わらせる',
        goalDate: '2021-8-17.19：00',
        limitDate: '2021-8-20.23：59',
        notification: '2021-8-16.9：00',
        memo: 'なし',
        rest: '2',
      },
      {
        title: 'レポートAを終わらせる',
        goalDate: '2021-8-20.21:00',
        limitDate: '2021-8-26.23:00',
        notification: '8-19.9:00',
        memo: '4000字だよ一日じゃ終わらないよ',
        rest: '5',
      },
      {
        title: '経営学テキスト読んでくる',
        goalDate: '2021-9-1.23:00',
        limitDate: '2021-9-2.10:30',
        notification: '2021-8-31.9:00',
        memo: 'p.123-150',
        rest: '16',
      },
      {
        title: '機構アカウント作る',
        goalDate: '2021-9-20.21:00',
        limitDate: '2021-9-27.23:59',
        notofication: '2021-9-19.9:00',
        memo: 'なし',
        rest: '36',
      },
    ];
    // this.$route.params で URL のパラメータ部分を取得できる。
    this.todo = sampleTodos[this.$route.params.id];
  },
  methods: {
    deleteItem: function(index) {
      //モーダルを閉じる
      // リストからカードを削除
      this.schedules.splice(index, 1);
    },
    // by ほりしょー
    // mounted は最初のレンダリングで呼ばれる。
    // 将来的にはここでAPI(Django)を呼び出してデータを取得する。
    // 現状は sampleTodos をAPIと見立てて todo に代入してあげている。
    mounted() {
        const sampleTodos = [
                {
                  id: 1,
                  title: '課題１を終わらせる',
                  goalDate: '2021-08-17T19:00',
                  limitDate: '2021-08-20T23:59',
                  notification: '2021-08-16T09:00',
                  memo: 'なし',
                  rest: '2',
                },
                {
                  id: 2,
                  title: 'レポートAを終わらせる',
                  goalDate: '2021-08-20T21:00',
                  limitDate: '2021-08-26T23:00',
                  notification: '2021-08-19T09:00',
                  memo: '4000字だよ一日じゃ終わらないよ',
                  rest: '5',
                },
                {
                  id: 3,
                  title: '経営学テキスト読んでくる',
                  goalDate: '2021-09-01T23:00',
                  limitDate: '2021-09-02T10:30',
                  notification: '2021-08-31T09:00',
                  memo: 'p.123-150',
                  rest: '16',
                },
                {
                  id: 4,
                  title: '機構アカウント作る',
                  goalDate: '2021-09-20T21:00',
                  limitDate: '2021-09-27T23:59',
                  notification: '2021-09-19T09:00',
                  memo: 'なし',
                  rest: '36',
                },
            ]
        // this.$route.params で URL のパラメータ部分を取得できる。
        this.todo = sampleTodos[this.$route.params.id-1]
    },
    methods: {
        deleteItem: function(index){
            // リストからカードを削除
            this.sampleTodos.splice(index, 1);
            //モーダルを閉じる
        }
    },
}
}
</script>

<style scoped>

/* ここにcssを書いてね */
.detail{
    text-align: left;
    font-size: 16px!important;
}

header {
  height: 50px;
  background-color: #ea5532;
}

img {
    height: 50px;
    padding-left: 8px;
}

.title{
    font-size: 20px;
    padding-top: 15px;
    padding-bottom: 15px;
    padding-left: 10px;
    color: rgb(100, 100, 100);
}

.goalDate, .limitDate, .notification {
    display: flex;
    border-top: 1px solid #ea5532;
    justify-content: space-between;
    color: rgb(100, 100, 100);
    padding-top: 20px;
}

.caption {
  padding-left: 10px;
}

.memo{
    border-top: 1px solid #ea5532;
    padding-top: 16px;
    padding-left: 10px;
    color: rgb(100, 100, 100);
}

.form {
  border-bottom: 1px solid #ea5532;
  padding-top: 16px;
  padding-bottom: 16px;
  padding-left: 10px;
}

.btn {
  text-align: center;
  margin-top: 16px;
}

a {
    text-decoration: none;
    color: white!important;
}

input[type="datetime-local"] {
    height: 30px;
    margin-top: 12px;
    margin-right: 10px;
    width: 185px;
    position: relative;
    bottom: 16px;
}

input[type='text'] {
  font-size: 20px;
}
</style>