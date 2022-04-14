<template>
  <div class="detail">
    <header>
      <Header />
    </header>
    <v-container class="top" fluid>
      <v-text-field v-model="todo.title" label="タスク" color="#ea5532" outlined />
    </v-container>
    <v-container class="second" fluid>
      <v-row>
        <v-col cols="4">
          <div class="caption">終わらせたい日時</div>
        </v-col>
        <v-col cols="8">
          <input type="datetime-local" style="border: none" v-model="todo.goalDate"/>
        </v-col>
      </v-row>
    </v-container>
    <v-divider color="#ea5532" />
    <v-container fluid>
      <v-row>
        <v-col cols="4">
          <div class="caption">締め切り日時</div>
        </v-col>
        <v-col cols="8">
          <input type="datetime-local" style="border: none" v-model="todo.limitDate"/>
        </v-col>
      </v-row>
    </v-container>
    <v-divider color="#ea5532" />
    <v-container fluid>
      <v-row>
        <v-col cols="4">
          <div class="caption">設定する音声</div>
        </v-col>
        <v-col cols="8" id="select">
          <v-select id="onseisentaku" item-value="id" item-text="name" :items="tourokuOnseis" label="Solo field" solo color="#ea5532" />
        </v-col>
      </v-row>
    </v-container>
    <v-divider color="#ea5532" />
    <v-container fluid>
      <v-row>
        <v-col cols="4">
          <div class="caption">通知</div>
        </v-col>
        <v-col cols="8">
          <input type="datetime-local" style="border: none" v-model="todo.notification"/>
        </v-col>
      </v-row>
    </v-container>
    <v-divider color="#ea5532" />
    <v-container fluid>
      <v-textarea v-model="todo.memo" label="メモ" color="#ea5532" />
    </v-container>
    <div class="btn">
      <DoneButton />
      <SaveButton @click.native="SaveData" />
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
            tourokuOnseis: [
              {id: 1, name: "スタジアムの歓声" },//apiが入ったら[]にする予定
              {id: 2, name: "威風堂々" },
           ],
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
      },
      fetchTourokus: function(){
      axios.get('XML入れるよ')
      .then(res=>{
        console.log(res)
        console.log(res.data)
      })
    },
    fetchSamples: function(){
      axios
        .get('XML入れるよ')
        .then(res=>{
        console.log(res)
        console.log(res.data)
        })
        .catch(function (err) {
          console.log(err);
        });
    }
    }
}
</script>

<style scoped>

.detail {
  margin: 0;
}
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
