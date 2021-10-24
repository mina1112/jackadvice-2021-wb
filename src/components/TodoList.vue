<template>
  <div class="TodoList">
    <html lang="ja">
      <head>
        <meta charset="utf-8" />
        <meta name="viewport" content="width=device-width,initial-scale=1" />
        <title>List</title>
      </head>
      <body>
        <div class="header">
          <img src="#" />
        </div>
        <div class="main">
          <div
            v-for="sampleSchedule in sampleSchedules"
            :key="sampleSchedule.title"
          >
            <div class="card">
              <div class="todo">
                <a href="#詳細ページ" class="title">{{
                  sampleSchedule.title
                }}</a>
                <div class="goalDate">{{ sampleSchedule.goalDate }}</div>
                <div class="rest">あと{{ sampleSchedule.rest }}日</div>
              </div>
              <a class="finish" href="#done">Done!</a>
            </div>
          </div>
        </div>
      </body>
    </html>
  </div>
</template>

<script>
export default {
  name: 'TodoList',
  data() {
    return {
      sampleSchedules: [
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
      ],
    };
  },
};
</script>

<style scoped>
.header {
  background-color: #ea5532;
  width: 100%;
  height: 50px;
  margin: 0;
}

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
  right: 0.6em;
  bottom: 0.6em;
  color: #fff;
  background-color: #ea5532;
  width: 25%;
  height: 2em;
  border-radius: 0.5em;
  font-size: 1.1em;
  text-align: center;
  text-decoration: none;
  box-shadow: 0 2px 3px #b3381c;
  margin-left: auto;
  margin-bottom: 0;
}

.finish:hover {
  background-color: #b3381c;
}
</style>
