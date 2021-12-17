<template>
  <modal name="done-modal" :resizale="true">
    <div class="modal-header">
      <h2>Modal Title</h2>
    </div>
    <div class="modal-body">
      <p>モーダルが表示されました！</p>
    </div>
    <button v-on:click="hide">close</button>
  </modal>
</template>

<script>
export default {
    name: 'DoneAction',
    data() {
        
    }
}
</script>

<style scoped></style>
