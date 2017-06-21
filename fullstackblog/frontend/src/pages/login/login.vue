<template>
  <div class="login-box">
    <h1>Registration</h1>
    
    <el-form :model="ruleForm" ref="ruleForm" label-width="100px" class="demo-ruleForm">
      <el-form-item label="Username" prop="username">
        <el-input type="text" v-model="ruleForm.username" auto-complete="off"></el-input>
      </el-form-item>
      <el-form-item label="Password" prop="password">
        <el-input type="password" v-model="ruleForm.password" auto-complete="off"></el-input>
      </el-form-item>
      <el-form-item label="Display name" prop="displayName">
        <el-input type="text" v-model="ruleForm.displayName" auto-complete="off"></el-input>
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
  export default {
    // name: 'Login',
    data () {
      
      const checkName = (rule, value, cb) => {
        if (!value) {
          return cb(new Error('Username cannot be empty'))
        }
      }
      const validatePass = (rule, value, cb) => {
        if (value === '') {
          cb(new Error('Please enter the password'))
        }
        cb()
      }
      const validateDisplayName = (rule, value, cb) => {
        if (value === '') {
          cb(new Error('Please enter the Display name'))
        }
        cb()
      } 
      return {
        ruleForm: {
          password: '',
          displayName: '',
          username: ''
        },
        /*
        rules: {
          pass: [
            {validator: validatePass, trigger: 'blur'}
          ],
          displayName: [
            {validator: validateDisplayName, trigger: 'blur'}
          ],
          username: [
            {
              validator: checkName,
              trigger: 'blur'
            }
          ]
        }
        */
        
      }
    },
    computed: {
      ...mapActions({
        UserReg: 'UserReg'
      })
    },
    methods: {
      submitForm(formName) {
        this.$store.dispatch('UserReg', this.ruleForm)  
      },
      resetForm(formName) {
        this.$refs[formName].resetFields()
      }
    }
  }
</script>

<style>
  .login-box {
    width: 400px;
    height: 600px;
    position: absolute;
    left: 50%;
    margin-left: -200px;
    top: 50%;
    margin-top: -300px;
  }
</style>
