<template>
    <v-btn
        class=white--text
        depressed
        color=#ea5532
        elevation="2"
        rounded
        @click="end"
    >Done</v-btn>
</template>

<script>
export default {
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