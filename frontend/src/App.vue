<template>
  <div id="app">
    <nav class="navbar navbar-expand-lg navbar-light bg-light">
      <a class="navbar-brand" href="#">Navbar</a>
      <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNavAltMarkup" aria-controls="navbarNavAltMarkup"
        aria-expanded="false" aria-label="Toggle navigation">
        <span class="navbar-toggler-icon"></span>
      </button>
      <div class="collapse navbar-collapse" id="navbarNavAltMarkup">
        <div class="navbar-nav">
          <a class="nav-item nav-link active" href="/">Home
            <span class="sr-only">(current)</span>
          </a>
          <a class="nav-item nav-link" href="/auth">Login/Signup</a>
          <a class="nav-item nav-link" href="/contacts">Contacts</a>
          <a class="nav-item nav-link" href="/chats">Chats</a>
          <a class="nav-item nav-link" href="/rooms">Rooms</a>
        </div>
      </div>
    </nav>
    <router-view></router-view>
  </div>
</template>

<script>
  //import HelloWorld from './components/HelloWorld.vue'

  export default {
    name: 'app',
    components: {
      //HelloWorld
    }
  }
</script>

<style>
  #app {
    font-family: 'Avenir', Helvetica, Arial, sans-serif;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
    text-align: center;
    color: #2c3e50;
  }
</style>