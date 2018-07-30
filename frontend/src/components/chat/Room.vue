<template>
  <div class="container">
    <div class="d-flex justify-content-between flex-wrap flex-md-nowrap align-items-center pt-3 pb-2 mb-3 border-bottom">
      <h1 class="h2">Room</h1>
    </div>
      <div class="col-sm-6 offset-3">
        <div id="chat-container" class="card">
          <div class="card-header text-white text-center font-weight-bold subtle-blue-gradient">
            Share the page URL to invite new friends
          </div>

          <div class="card-body">
            <div class="container chat-body">
              <div class="row chat-section">
                <div class="col-sm-2">
                  <img class="rounded-circle" src="http://placehold.it/40/f16000/fff&text=D" />
                </div>
                <div class="col-sm-7">
                  <span class="card-text speech-bubble speech-bubble-peer">Hello!</span>
                </div>
              </div>
              <div class="row chat-section">
                <div class="col-sm-7 offset-3">
                  <span class="card-text speech-bubble speech-bubble-user float-right text-white subtle-blue-gradient">
                    Whatsup, another chat app?
                  </span>
                </div>
                <div class="col-sm-2">
                  <img class="rounded-circle" src="http://placehold.it/40/333333/fff&text=A" />
                </div>
              </div>
              <div class="row chat-section">
                <div class="col-sm-2">
                  <img class="rounded-circle" src="http://placehold.it/40/f16000/fff&text=D" />
                </div>
                <div class="col-sm-7">
                  <p class="card-text speech-bubble speech-bubble-peer">
                    Yes this is Chatire, it's pretty cool and it's Open source and it was built with Django and Vue JS so we can tweak it to
                    our satisfaction.
                  </p>
                </div>
              </div>
              <div class="row chat-section">
                <div class="col-sm-7 offset-3">
                  <p class="card-text speech-bubble speech-bubble-user float-right text-white subtle-blue-gradient">
                    Okay i'm already hacking around let me see what i can do to this thing.
                  </p>
                </div>
                <div class="col-sm-2">
                  <img class="rounded-circle" src="http://placehold.it/40/333333/fff&text=A" />
                </div>
              </div>
              <div class="row chat-section">
                <div class="col-sm-7 offset-3">
                  <p class="card-text speech-bubble speech-bubble-user float-right text-white subtle-blue-gradient">
                    We should invite james to see this.
                  </p>
                </div>
                <div class="col-sm-2">
                  <img class="rounded-circle" src="http://placehold.it/40/333333/fff&text=A" />
                </div>
              </div>
            </div>
          </div>

          <div class="card-footer text-muted">
            <form>
              <div class="row">
                <div class="col-sm-10">
                  <input type="text" placeholder="Type a message" />
                </div>
                <div class="col-sm-2">
                  <button class="btn btn-primary">Send</button>
                </div>
              </div>
            </form>
          </div>
        </div>

        <!-- <div v-else>
          <h3 class="text-center">Create a new room!</h3>

          <br />

          <p class="text-center">
            Create a new room and invite your friends to chat with. Define the name and start to chat!
          </p>

          <br />

          <input class="form-control form-control-lg" type="text" placeholder="room name" v-model="roomName">

          <br />

          <button class="btn btn-primary btn-lg btn-block" data-toggle="modal" data-target="#exampleModal">Create Room</button>
        </div> -->

      </div>
    </div>
</template>

<script>
  import Vue from 'vue'
  import axios from 'axios'
  import VueLocalStorage from 'vue-localstorage'

  Vue.use(VueLocalStorage)

  export default {
    name: 'room',
    data() {
      return {
        roomName: "",
        chatRooms: []
      }
    },
    created() {
      console.log("ENTER", this.$route.params.chat_id)

      let chat_id = this.$route.params.chat_id
      
      // axios({
      //       method: 'get',
      //       url: 'http://localhost:8000/api/v1/chat-session-list/',
      //       // responseType: "application/json",
      //       headers: {
      //         'Accept': 'application/json',
      //         'Content-Type': 'application/json',
      //         'Authorization': "Token " + token
      //       }
      //     })
      //     .then((response) => {
      //       console.log("Chat list: ", response)
      //       this.chatRooms = response.data
      //     })      
    },
    methods: {
      createRoom() {
      }
    }
  }
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
  .container {
    margin-top: 3rem;
  }

  h1,
  h2 {
    font-weight: normal;
  }

  ul {
    list-style-type: none;
    padding: 0;
  }

  li {
    display: inline-block;
    margin: 0 10px;
  }

  .btn {
    border-radius: 0 !important;
  }

  .card-footer input[type="text"] {
    background-color: #ffffff;
    color: #444444;
    padding: 7px;
    font-size: 13px;
    border: 2px solid #cccccc;
    width: 100%;
    height: 38px;
  }

  .card-header a {
    text-decoration: underline;
  }

  .card-body {
    background-color: #ddd;
  }

  .chat-body {
    margin-top: -15px;
    margin-bottom: -5px;
    height: 380px;
    overflow-y: auto;
  }

  .speech-bubble {
    display: inline-block;
    position: relative;
    border-radius: 0.4em;
    padding: 10px;
    background-color: #fff;
    font-size: 14px;
  }

  .subtle-blue-gradient {
    background: linear-gradient(45deg, #004bff, #007bff);
  }

  .speech-bubble-user:after {
    content: "";
    position: absolute;
    right: 4px;
    top: 10px;
    width: 0;
    height: 0;
    border: 20px solid transparent;
    border-left-color: #007bff;
    border-right: 0;
    border-top: 0;
    margin-top: -10px;
    margin-right: -20px;
  }

  .speech-bubble-peer:after {
    content: "";
    position: absolute;
    left: 3px;
    top: 10px;
    width: 0;
    height: 0;
    border: 20px solid transparent;
    border-right-color: #ffffff;
    border-top: 0;
    border-left: 0;
    margin-top: -10px;
    margin-left: -20px;
  }

  .chat-section:first-child {
    margin-top: 10px;
  }

  .chat-section {
    margin-top: 15px;
  }

  .send-section {
    margin-bottom: -20px;
    padding-bottom: 10px;
  }
</style>