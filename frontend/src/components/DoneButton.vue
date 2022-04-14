<template>
 <div>
    <v-btn
        class=white--text
        depressed
        color=#ea5532
        elevation="2"
        rounded
        @click="end"
    >Done</v-btn>
    <audio
        v-if="mp3_url!==null"
        id="audio"
        controls
        :src="mp3_url"   />
</div>
</template>

<script>
import axios from 'axios'

export default {
    data(){
        return{
          mp3_url: ""
        }
    },
    async mounted() {
      this.response = await axios.get("https://post.s3-ap-northeast-1.amazonaws.com/local/"+this.username+"/"+this.$route.params['postId']+".mp3")
      .then((res) => {
        return res;
    }, this);
      if (this.response.status === 403) {
        console.log("エラー！");
        this.mp3_url = null;
        console.log(this.mp3_url);
      } else {
        console.log("取得した");
        this.mp3_url = "https://samsample-1.s3.us-east-2.amazonaws.com/%E3%82%B9%E3%82%BF%E3%82%B8%E3%82%A2%E3%83%A0%E3%81%AE%E6%AD%93%E5%A3%B01.mp3"; //本来は this.response.config.url
        console.log(this.mp3_url);
      }
    },
    methods: {
        end: function(){
            const res = confirm('button was clicked.');
            if (res == true) {
                alert('おめでとうございます！');
            } else {
                alert('キャンセルされました');
            }
        },
        // リストからカードを削除する
        deleteItem: function(index){
            this.sampleTodos.splice(index, 1);
        },
    },
}
</script>

<style>
</style>