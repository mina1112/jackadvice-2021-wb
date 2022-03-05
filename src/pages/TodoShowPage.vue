<template>
  <div class="detail">
        <header>
          <Header />
        </header>
        <div class="title">
          タスク:<input type="text" style="border: none" v-model="todo.title" />
        </div>
        <div class="goalDate">
          <div class="caption">終わらせたい日時</div>
          <input
            type="datetime-local"
            style="border: none"
            v-model="todo.goalDate"
          />
        </div>
        <div class="limitDate">
          <div class="caption">締め切り日時</div>
          <input
            type="datetime-local"
            style="border: none"
            v-model="todo.limitDate"
          />
        </div>
        <div class="notification">
          <div class="caption">通知</div>
          <input
            type="datetime-local"
            style="border: none"
            v-model="todo.notification"
          />
        </div>
        <div class="memo">メモ</div>
        <div class="form">
          <textarea
            cols="43"
            rows="4"
            style="border: none"
            v-model="todo.memo"
          ></textarea>
        </div>
        <div class="btn">
            <DoneButton></DoneButton>
            <SaveButton @click.native="SaveData"></SaveButton>
        </div>
  </div>
</template>

<script>
import DoneButton from '../components/DoneButton.vue'
import SaveButton from '../components/SaveButton.vue'
import Header from '../components/Header.vue'
import axios from 'axios'

export default {
    name: 'TodoShowPage',
    components: {
        DoneButton,
        SaveButton,
        Header
    },
    data(){
        return{
            todo: {},
        }
    },
    // todo一覧からidを取得->そのidに対応するdataをAPIから取得
    mounted() {
      axios
        .get('https://jsonplaceholder.typicode.com/todos/')
        .then(response => {
          this.todo = response.data[this.$route.params.id-1]
        })
        .catch(error => {
          console.log(error);
        });
    },
    //SaveButtonのPost
    methods: {
      SaveData: function(){
      axios
        .post('https://jsonplaceholder.typicode.com/posts/', {
          id: this.todo.id,
          title: this.todo.title,
          goalDate: this.todo.goalDate,
          limitDate: this.todo.limitDate,
          notification: this.todo.notification,
          memo: this.todo.memo
        })
        .then(response => {
          // unshift使えない??
          // this.todo.shift(response.data)
          console.log(response.data);
        })
        .catch(error => console.log(error))
      }
    }
}
</script>

<style scoped>

.detail{
  text-align: left;
    font-size: 16px!important;
}

img {
  height: 50px;
  padding-left: 8px;
}

.title {
  font-size: 20px;
  padding-top: 15px;
  padding-bottom: 15px;
  padding-left: 10px;
  color: rgb(100, 100, 100);
}

.goalDate,
.limitDate,
.notification {
  display: flex;
  border-top: 1px solid #ea5532;
  justify-content: space-between;
  color: rgb(100, 100, 100);
  padding-top: 20px;
}

.caption {
  padding-left: 10px;
}

.memo {
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
  color: white !important;
}

input[type='datetime-local'] {
  height: 30px;
  margin-top: 12px;
  margin-right: 10px;
  width: 200px;
  position: relative;
  bottom: 16px;
}

input[type='text'] {
  font-size: 20px;
}
</style>
