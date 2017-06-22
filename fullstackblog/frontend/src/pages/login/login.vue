<template>
  <div class="login-box">
    <h1>Login</h1>
    <el-form :model="ruleForm" ref="ruleForm" label-width="100px" class="demo-ruleForm">
      <el-form-item label="Username" prop="username">
        <el-input type="text" v-model="ruleForm.username" auto-complete="off"></el-input>
      </el-form-item>
      <el-form-item label="Password" prop="password">
        <el-input type="password" v-model="ruleForm.password" auto-complete="off"></el-input>
      </el-form-item>
      <el-form-item>
        <el-button type="primary" @click="submitForm('ruleForm')">Submit</el-button>
        <el-button @click="resetForm('ruleForm')">Reset</el-button>
      </el-form-item>
    </el-form>
  </div>
</template>

<script>
  import {mapActions} from 'vuex'
  import api from '@/api'
  export default {
    data() {
      return {
        ruleForm: {
          username: '',
          password: ''
        }
      }
    },
    methods: {
      ...mapActions(['UserLogin']),
      submitForm(formName) {

        this.$refs[formName].validate((valid) => {
          if (valid) {
            this.$store.dispatch('UserLogin', this.ruleForm).then(res => {
              if (res) {
                this.$router.push('/')
              }
            })
          }
        })
      },
      resetForm(formName) {
        this.$refs[formName].resetFields()
      }
    }
  }
</script>
