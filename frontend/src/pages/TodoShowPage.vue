<template>
  <div class="detail">
    <header>
      <Header />
    </header>
    <v-col cols="12" class="top">
      <v-text-field v-model="todo.title" label="タスク" color="#ea5532" outlined></v-text-field>
    </v-col>
    <v-col cols="12" class="second">
      <v-row>
        <v-col cols="4">
          <div class="caption">終わらせたい日時</div>
        </v-col>
        <v-col cols="8">
          <input type="datetime-local" style="border: none" v-model="todo.goalDate"/>
        </v-col>
      </v-row>
    </v-col>
    <v-divider color="#ea5532"></v-divider>
    <v-col cols="12">
      <v-row>
        <v-col cols="4">
          <div class="caption">締め切り日時</div>
        </v-col>
        <v-col cols="8">
          <input type="datetime-local" style="border: none" v-model="todo.limitDate"/>
        </v-col>
      </v-row>
    </v-col>
    <v-divider color="#ea5532"></v-divider>
    <v-col cols="12">
      <v-row>
        <v-col cols="4">
          <div class="caption">通知</div>
        </v-col>
        <v-col cols="8">
          <input type="datetime-local" style="border: none" v-model="todo.notification"/>
        </v-col>
      </v-row>
    </v-col>
    <v-divider color="#ea5532"></v-divider>
    <v-col cols="12">
      <v-textarea v-model="todo.memo" label="メモ" color="#ea5532"></v-textarea>
    </v-col>
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
            todo: {
              title: '',
              goalDate: '',
              limitDate: '',
              notification: '',
              memo: ''
            },
        }
    },
    // todo一覧からidを取得->そのidに対応するdataをAPIから取得
    mounted() {
      axios
        .get('https://jsonplaceholder.typicode.com/todos/')
        .then(response => {
          this.todo = response.data[this.$route.params.id-1]
          console.log(this.todo)
        })
        .catch(error => {
          console.log(error);
        });
    },
    //データの更新
    methods: {
      SaveData: function(){
      axios
        .put('https://jsonplaceholder.typicode.com/posts/' + this.todo.id, this.todo)
        .then(response => {
          console.log(response.data);
        })
        .catch(error => console.log(error))
      }
    }
}
</script>

<style scoped>
.btn {
  text-align: center;
}

.top {
  margin-top: 16px;
}

.second {
  margin-top: -32px;
}
</style>
