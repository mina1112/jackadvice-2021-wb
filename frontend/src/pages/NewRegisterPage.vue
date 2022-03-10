<template>
  <div class="detail">
    <header>
      <Header/>
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
      <SaveButton @click.native="RegisterData"></SaveButton>
    </div>
  </div>
</template>

<script>
import SaveButton from '../components/SaveButton.vue'
import Header from '../components/Header.vue'
import axios from 'axios'

export default {
    name: 'TodoRegisterPage',
    components: {
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
    //データの更新
    methods: {
      RegisterData: function(){
      axios
        .post('https://jsonplaceholder.typicode.com/todos/', this.todo)
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
