<template>
  <div class="container">
    <div class="d-flex justify-content-between flex-wrap flex-md-nowrap align-items-center pt-3 pb-2 mb-3 border-bottom">
      <h1 class="h2">Chats</h1>
      <!-- <div class="btn-toolbar mb-2 mb-md-0">
        <div class="btn-group mr-2">
          <button class="btn btn-sm btn-outline-secondary">Share</button>
          <button class="btn btn-sm btn-outline-secondary">Export</button>
        </div>
        <button class="btn btn-sm btn-outline-secondary dropdown-toggle">
          <span data-feather="calendar"></span>
          This week
        </button>
      </div> -->
      <div class="btn-toolbar mb-2 mb-md-0">
        <button class="btn btn-primary my-2" data-toggle="modal" data-target="#createRoomModal">Create a New Room</button>
      </div>
    </div>
    <div class="row">
      <div class="col-sm" v-for="item in chatRooms" :key="item.id">
        <div class="card" style="width: 15rem;">
          <img class="card-img-top" src="data:image/svg+xml;charset=UTF-8,%3Csvg%20width%3D%22286%22%20height%3D%22180%22%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%20286%20180%22%20preserveAspectRatio%3D%22none%22%3E%3Cdefs%3E%3Cstyle%20type%3D%22text%2Fcss%22%3E%23holder_164bec6ffae%20text%20%7B%20fill%3Argba(255%2C255%2C255%2C.75)%3Bfont-weight%3Anormal%3Bfont-family%3AHelvetica%2C%20monospace%3Bfont-size%3A14pt%20%7D%20%3C%2Fstyle%3E%3C%2Fdefs%3E%3Cg%20id%3D%22holder_164bec6ffae%22%3E%3Crect%20width%3D%22286%22%20height%3D%22180%22%20fill%3D%22%23777%22%3E%3C%2Frect%3E%3Cg%3E%3Ctext%20x%3D%22106.3984375%22%20y%3D%2296.3%22%3E286x180%3C%2Ftext%3E%3C%2Fg%3E%3C%2Fg%3E%3C%2Fsvg%3E"
            alt="Card image cap">
          <div class="card-body">
            <h5 class="card-title">{{item.name_room}}</h5>
            <p class="card-text">Some quick example text to build on the card title and make up the bulk of the card's content.</p>
            <a href="#" class="btn btn-primary">Go somewhere</a>
          </div>
        </div>
      </div>
      <div class="col-sm-6 offset-3">
        <div v-if="false" id="chat-container" class="card">
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
    <!-- Modal -->
    <div class="modal fade" id="createRoomModal" tabindex="-1" role="dialog" aria-labelledby="exampleModalLabel" aria-hidden="true">
      <div class="modal-dialog" role="document">
        <div class="modal-content">
          <div class="modal-header">
            <h5 class="modal-title" id="exampleModalLabel">Create a new room!</h5>
            <button type="button" class="close" data-dismiss="modal" aria-label="Close">
              <span aria-hidden="true">&times;</span>
            </button>
          </div>
          <div class="modal-body">
            <input class="form-control form-control-lg" type="text" placeholder="room name" v-model="roomName">
            <p style="text-align: left;">
              <small>Create a new room and invite your friends to chat with. Define the name and start to chat!</small>
            </p>
          </div>
          <div class="modal-footer">
            <button type="button" class="btn btn-secondary" data-dismiss="modal">Close</button>
            <button type="button" class="btn btn-primary" @click="createRoom" :disabled="!roomName">Create</button>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
  import Vue from 'vue'
  import axios from 'axios'
  import VueLocalStorage from 'vue-localstorage'

  Vue.use(VueLocalStorage)

  export default {
    name: 'chats',
    data() {
      return {
        roomName: "",
        chatRooms: []
      }
    },
    created() {
      console.log("TESTEEEEE");

      let token = Vue.localStorage.get('token')

      axios({
            method: 'get',
            url: 'http://localhost:8000/api/v1/chat-session-list/',
            // responseType: "application/json",
            headers: {
              'Accept': 'application/json',
              'Content-Type': 'application/json',
              'Authorization': "Token " + token
            }
          })
          .then((response) => {
            console.log("Chat list: ", response)
            this.chatRooms = response.data
          })
      
    },
    methods: {
      createRoom() {
        console.log("token: ", Vue.localStorage.get('token'))
        console.log("username: ", Vue.localStorage.get('username'))
        console.log("roomName: ", this.roomName)

        let token = Vue.localStorage.get('token')
        let username = Vue.localStorage.get('username')
        let roomName = this.roomName

        axios({
            method: 'post',
            url: 'http://localhost:8000/api/v1/chat-session-create/',
            // responseType: "application/json",
            headers: {
              'Accept': 'application/json',
              'Content-Type': 'application/json',
              'Authorization': "Token " + token
            },
            data: {
              room_name: roomName,
            }
          })
          .then(function (response) {
            console.log("Chat session: ", response);

          })
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