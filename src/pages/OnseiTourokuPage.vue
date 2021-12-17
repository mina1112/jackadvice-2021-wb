<template>
<div class=onsei>
  <html lang="ja">
    <head>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width,initial-scale=1">
        <title>onsei</title>
    </head>
    <header>
      <img src="#" />
    </header>
    <body>
       <div
          v-for="sampleOnsei in sampleOnseis"
          :key="sampleOnsei.name" >
            <div class="onseiname">{{ sampleOnsei.name }}</div>
            <div class="onseihensyu">編集</div>
      </div>
      <hr>
    </body>
  </html>
</div>
</template>

<script>
export default {
  name: 'OnseiTouroku',
  data() {
    return {
      sampleOnseis: [
        {
          name: '音声ファイル１'
        },
      ]
    }
  }
}
</script>

<style scoped>
header {
    height: 50px;
    background-color:  #ea5532;
}

img {
    height: 40px;
    padding: 5px 0 0 10px;
}
.onseiname{
    font-size: 20px;
    padding-top: 15px;
    padding-bottom: 15px;
    padding-left: 10px;
    color: rgb(143, 143, 143);
}
</style>