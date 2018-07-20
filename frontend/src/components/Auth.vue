<!-- ./src/components/Auth.vue -->
<template>
  <div class="container">
    <h1 class="text-center">Welcome to Web Chat!</h1>
    <div id="auth-container" class="row">
      <div class="col-sm-4 offset-sm-4">
        <ul class="nav nav-tabs nav-justified" id="myTab" role="tablist">
          <li class="nav-item">
            <a class="nav-link" id="signup-tab" data-toggle="tab" href="#signup" role="tab" aria-controls="signup" aria-selected="true">Sign Up</a>
          </li>
          <li class="nav-item">
            <a class="nav-link active" id="signin-tab" data-toggle="tab" href="#signin" role="tab" aria-controls="signin" aria-selected="false">Sign In</a>
          </li>
        </ul>

        <div class="tab-content" id="myTabContent">

          <div class="tab-pane fade" id="signup" role="tabpanel" aria-labelledby="signin-tab">
            <form @submit.prevent="signUp">
              <div class="form-group">
                <input type="email" v-model="emailUp" class="form-control" id="emailUp" placeholder="Email Address" required>
              </div>
              <div class="form-row">
                <div class="form-group col-md-6">
                  <input type="text" v-model="usernameUp" class="form-control" id="usernameUp" placeholder="Username" required>
                </div>
                <div class="form-group col-md-6">
                  <input type="password" v-model="passwordUp" class="form-control" id="passwordUp" placeholder="Password" required>
                </div>
              </div>
              <div class="form-group">
                <div class="form-check">
                  <input class="form-check-input" type="checkbox" id="toc" required>
                  <label class="form-check-label" for="gridCheck">
                    Accept terms and Conditions
                  </label>
                </div>
              </div>
              <button type="submit" class="btn btn-block btn-primary">Sign up</button>
            </form>
          </div>

          <div class="tab-pane fade show active" id="signin" role="tabpanel" aria-labelledby="signin-tab">
            <form @submit.prevent="signIn">
              <div class="form-group">
                <input v-model="username" type="text" class="form-control" id="usernameIn" placeholder="Username" required>
              </div>
              <div class="form-group">
                <input v-model="password" type="password" class="form-control" id="passwordIn" placeholder="Password" required>
              </div>
              <button type="submit" class="btn btn-block btn-primary">Sign in</button>
            </form>
          </div>

        </div>
      </div>
    </div>
  </div>
</template>

<script>
  import axios from 'axios'

  export default {
    name: 'Auth',
    data() {
      return {
        username: '',
        password: '',
        emailUp: '',
        usernameUp: '',
        passwordUp: '',
      }
    },
    methods: {
      signUp() {
        axios({
            method: 'post',
            url: 'http://localhost:8000/api/v1/rest-auth/registration/',
            // responseType: "application/json",
            headers: {
              'Accept': 'application/json',
              'Content-Type': 'application/json',
            },
            data: {
              username: this.usernameUp,
              email: this.emailUp,
              password1: this.passwordUp,
              password2: this.passwordUp
            }
          })
          .then(function (response) {
            console.log("Registration", response);

          });
      },
      signIn() {
        console.log("login", this.username)
        console.log("login", this.password)

        // GET request for remote image
        axios({
            method: 'post',
            url: 'http://localhost:8000/api/v1/rest-auth/login/',
            // responseType: "application/json",
            headers: {
              'Accept': 'application/json',
              'Content-Type': 'application/json',
            },
            data: {
              username: this.username,
              password: this.password
            }
          })
          .then(function (response) {
            console.log("TESTE", response);

          });

      }
    }
  }
</script>

<style scoped>
  .container {
    margin-top: 3rem;
  }
</style>