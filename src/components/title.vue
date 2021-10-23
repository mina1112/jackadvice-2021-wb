<template>
    
</template>

<script>
export default{
    name: 'title',
    data: {
        title: "課題１を終わらせる"
    },
    watch: {
        title: function() {
            localStorage.setItem('title', JSON.stringify(this.title));
        },
    },
    mounted: function(){
        this.title = JSON.parse(localStorage.getItem('title'))  || [];
    }
}
</script>