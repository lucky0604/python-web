<template>
  <div class="login-container">
    <el-form autoComplete="on" :model="loginForm" ref="loginForm" label-position="left" label-width="0px" class="card-box login-form">
      <h3 class="title">System Registration</h3>
      <el-form-item prop="email">

        <el-input type="text" v-model="loginForm.username" autoComplete="on" placeholder="Username"></el-input>
      </el-form-item>
      <el-form-item prop="password1">

        <el-input type="password" v-model="loginForm.password" autoComplete="on" placeholder="Password"></el-input>
      </el-form-item>
      <el-form-item>
        <el-button type="primary" style="width: 100%;" @click="handleSubmit">Login</el-button>
      </el-form-item>
      <router-link to="/login" class="forget-pwd">
        Already has an account? Directly login.
      </router-link>
    </el-form>
  </div>  
</template>

<script>
  import {isValidEmail} from 'utils/validate'
  import {mapActions} from 'vuex'
  export default {
    name: 'login',
    data() {
      return {
        loginForm: {
          username: '',
          password: '',
        },
      }
    },
    computed: {
    },
    methods: {
      handleSubmit(){
        this.$refs['loginForm'].validate((valid) => {
          if (valid) {
            this.$store.dispatch('LoginByUsername', this.loginForm).then(() => {
              this.$router.push({path: '/'})
              alert('login component')
            })
            .catch(err => {
              console.log(err)
            })
          } else {
            console.log('error submit')
            return false
          }
        })
      }
    }
  }
</script>


<style rel="stylesheet/scss" lang="scss">
    @import "src/styles/mixin.scss";
    .tips{
      font-size: 14px;
      color: #fff;
      margin-bottom: 5px;
    }
    .login-container {
        @include relative;
        height: 100vh;
        background-color: #2d3a4b;

        input:-webkit-autofill {
            -webkit-box-shadow: 0 0 0px 1000px #293444 inset !important;
            -webkit-text-fill-color: #fff !important;
        }
        input {
            background: transparent;
            border: 0px;
            -webkit-appearance: none;
            border-radius: 0px;
            padding: 12px 5px 12px 15px;
            color: #eeeeee;
            height: 47px;
        }
        .el-input {
            display: inline-block;
            height: 47px;
            width: 85%;
        }
        .svg-container {
            padding: 6px 5px 6px 15px;
            color: #889aa4;
        }

        .title {
            font-size: 26px;
            font-weight: 400;
            color: #eeeeee;
            margin: 0px auto 40px auto;
            text-align: center;
            font-weight: bold;
        }

        .login-form {
            position: absolute;
            left: 0;
            right: 0;
            width: 400px;
            padding: 35px 35px 15px 35px;
            margin: 120px auto;
        }

        .el-form-item {
            border: 1px solid rgba(255, 255, 255, 0.1);
            background: rgba(0, 0, 0, 0.1);
            border-radius: 5px;
            color: #454545;
        }

        .forget-pwd {
            color: #fff;
        }
    }

</style>