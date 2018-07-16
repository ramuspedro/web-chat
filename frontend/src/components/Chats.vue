<!-- ./src/components/Chats.vue -->
<template>
  <div>
    <div class="title">
      <h1>{{msg}}</h1>
    </div>
  </div>
</template>

<script>
  export default {
    name: 'chats',
    data () {
      return {
        msg: 'Chats'
      }
    }
  }
</script>