<template>
  <div class="TodoList">
    <html lang="ja">
      <head>
        <meta charset="utf-8" />
        <meta name="viewport" content="width=device-width,initial-scale=1" />
        <title>List</title>
      </head>
      <body>
        <header>
          <Header />
        </header>
        <div class="main">
          <ul v-for="todo in todo" :key="todo.id">
            <div class="card">
              <div class="todo">
                <router-link
                  :to="{ name: 'TodoShowPage', params: { id: todo.id } }"
                  class="title"
                  >{{ todo.title }}</router-link
                >
                <div class="goalDate">{{ todo.completed }}</div>
                <div class="rest">あと{{ todo.id }}日</div>
              </div>
              <v-btn
                class="finish"
                color="#ea5532"
                @click="end(todo.id, todo.title)"
                :key="todo.id"
                >Done</v-btn
              >
            </div>
          </ul>

          <div>
            <router-link
              :to="{ name: 'NewRegisterPage', param: {} }"
              class="register"
            >
              +新規タスク
            </router-link>
          </div>
        </div>
      </body>
    </html>
  </div>
</template>

<script>
import Header from '@/components/Header.vue';
import axios from 'axios';

export default {
  name: 'TodoIndexPage',
  components: {
    Header,
  },
  data() {
    return {
      todo: null,
    };
  },

  mounted() {
    axios
      .get('https://jsonplaceholder.typicode.com/todos')
      .then((response) => (this.todo = response.data))
      .catch((error) => console.log(error));
  },
  methods: {
    end: function (id, title) {
      console.log(this.todo);
      const res = confirm(
        'todo「' + title + '」を完了します。よろしいですか？'
      );
      if (res == true) {
        axios
          .delete(`https://jsonplaceholder.typicode.com/todos/${id}`) //まだ実際のデータではないので削除はされません。
          .then((response) => console.log(response))
          .catch((error) => console.log(error));
        alert('todoを削除しました。お疲れ様です！');
        //this.$router.push({ path: '/todo', name: 'TodoIndexPage' });
      } else {
        alert('キャンセルされました');
      }
    },
    // リストからカードを削除する
    deleteItem: function (index) {
      this.todos.splice(index, 1);
    },
  },
};
</script>

<style scoped>
img {
  height: 40px;
  padding: 5px 0 0 10px;
}

.main {
  margin: 0.75em;
}

.card {
  position: relative;
  display: flex;
  border-radius: 8px;
  /* background-color: rgb(255, 255, 255); */
  box-shadow: 0 2px 5px #ccc;
  width: 100%;
  margin-top: 1em;
}

.todo {
  margin: 0.7em;
}

.title {
  text-decoration: none;
  font-size: 20px;
  color: #000;
  font-weight: 500;
}

.title:hover {
  text-decoration: underline;
}

.goalDate {
  font-size: 1em;
  color: #4c4c4c;
  font-weight: 300;
}

.rest {
  color: #ea5532;
  font-size: 1.1em;
}

.finish {
  display: flex;
  justify-content: center;
  align-items: center;
  position: absolute;
  right: 0.6rem;
  bottom: 0.6rem;
  width: 25%;
  height: 2em;
  border-radius: 0.5rem;
  color: #fff;
  font-size: 1.1rem;
  text-align: center;
  text-decoration: none;
  margin-left: auto;
  margin-bottom: 0;
}

.finish:hover {
  opacity: 0.9;
}

.finish:active {
  transform: translate(0.2px);
  border-bottom: none;
}

.register {
  position: relative;
  display: flex;
  border-radius: 8px;
  width: 100%;
  height: 6rem;
  margin-top: 1em;
  padding: 10px 10px;
  color: rgb(48, 48, 48);
  background-color: rgb(230, 230, 230);
  box-shadow: 0 2px 5px #ccc;
  font-size: 20px;
  font-weight: 500;
  text-decoration: none;
  text-align: center;
}
</style>
