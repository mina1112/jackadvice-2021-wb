<template>
<div class=onsei>
  <html lang="ja">
    <head>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width,initial-scale=1">
        <title>onsei</title>
    </head>
    <header>
      <Header />
    </header>
    <body>
      <h3 class="text-left">登録した音声</h3>
      <v-container>
        <v-row>
          <v-col id="select" class="d-flex" cols="12" sm="6" md="6" lg="6" xl="6">
            <v-select :items="items" label="Solo field" solo />
          </v-col>
          <v-col cols="12" sm="6" md="6" lg="6" xl="6">
            <v-btn class="ma-2" outlined color="#ea5532">登録</v-btn>
          </v-col>
        </v-row>
      </v-container>
      <h3 class="text-left">既存の音声ファイル</h3>
      <hr>
      <v-container>
        <v-row
            v-for="sampleOnsei in sampleOnseis"
            :key="sampleOnsei.title" >
              <v-col cols="12" xs="10" sm="10" md="10" lg="10" xl="10">
                <div class="onseiname text-left">{{ sampleOnsei.title }}</div>
              </v-col>
              <v-col cols="12" xs="2" sm="2" md="2" lg="2" xl="2">
                <div id="onseihensyu">編集</div>
              </v-col>
        </v-row>
      </v-container>
      <v-btn class="ma-2" outlined color="#ea5532">save</v-btn>
    </body>
  </html>
</div>
</template>

<script>
import Header from "@/components/Header.vue";
import axios from 'axios'


export default {
  name: 'OnseiTouroku',
  components: {
    Header
  },

  data() {
    return {
       mp3_url: "", //音声ファイルの中身
      //  showContent: false,
      //  postItem: '',
      //  sampleOnseis: [
      //   {
      //     id: 1,
      //     title: '音声ファイル1',
      //   },
      //    {
      //     id: 2,
      //     title: '音声ファイル2',
      //   },
      //    {
      //     id: 3,
      //     title: '音声ファイル3',
      //   }
      // ],
      // items: ['Foo', 'Bar', 'Fizz', 'Buzz'],
    }
  },
    mounted () {
    this.response = axios.get("https://post.s3-ap-northeast-1.amazonaws.com/local/"+this.username+"/"+this.$route.params['postId']+".mp3")
    .then((response) => (this.todo = response.data))
    .catch((error) => console.log(error));
      // .then((res) => {
      //   return res;
      // }, this);
      // if (this.response.status === 403) {
      //   console.log("エラー！");
      //   this.mp3_url = null;
      //   console.log(this.mp3_url);
      // } else {
      //   console.log("取得した");
      //   this.mp3_url = this.response.config.url;
      //   console.log(this.mp3_url);
      // }
    },
  }


</script>

<style scoped>
h3 {
  margin-top: 2vh;
  margin-left: 6vw;
}

hr{
  height: 1px;
  background-color: #ea5532;
  border: none;
}

img {
    height: 40px;
    padding: 5px 0 0 10px;
}
.onseiname{
    font-size: 20px;
    padding-top: 15px;
    padding-bottom: 15px;
    color: #333333;
}
#onseihensyu{
  color: #ea5532;
  padding-top: 2.4vh;
  margin-bottom: 2.3vh;
}

#select{
  color:#ea5532;
}
</style>