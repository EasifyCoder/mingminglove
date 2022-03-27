<template>
  <div>
    <el-form :rules="rules" ref="loginForm" :model="loginForm" class="loginContainer">
      <h3 class="loginTitle">系统登陆</h3>
      <el-form-item label="" prop="username">
        <el-input type= "text" auto-complete= "false" v-model= "loginForm.username" placeholder= "请输入用户名"></el-input>
      </el-form-item>
      <el-form-item label="" prop="password">
        <el-input type= "password" auto-complete= "false" v-model= "loginForm.password" placeholder= "请输入密码"></el-input>
      </el-form-item>
      <el-button 
        type="primary" round 
        style="width: 100%" 
        @click="submitLogin"
        :disabled="!canSubmit"
      >
        登录
      </el-button>
    </el-form>
  </div>
</template>

<script>
// import { ElMessage } from 'element-plus'
//引入api下的login函数，用于发起登录的axios请求
import {login} from '@/api'; 
export default {
  name: 'Login',
  data () {
    return {
      loginForm: {
        username: '',
        password: ''
      },
      rules: {
        username: [{ required: true, message: '请输入用户名', trigger: 'blur' }],
        password: [{ required: true, message: '请输入密码', trigger: 'blur' }]
      }
    }
  },
  computed: {
    //用于登录按钮是否可点击，需要输入用户名和密码才能点击
    canSubmit() {
      const {username, password} = this.loginForm
      return Boolean(username && password)
    },
  },
  methods: {
    submitLogin () {
      this.$refs.loginForm.validate((valid) => {
        if (valid) {
          login(this.loginForm).then(
            (response) => {
              if(response['code']==200){
                // 如果返回的response['code']==200，则证明用户名密码正确
                // 将response['token']存入本地
                localStorage.setItem('token', response['token']);
                this.$router.replace('/home')
              }
            }
          ).catch(
            (err) => {
              console.log(err);
            }
          )
          // this.$router.replace('/home')
        } else {
          ElMessage.error('请输入所有字段')
          return false
        }
      })
    }
  }
}
</script>

<style>
#app {
  width: 100%;
}

.loginContainer {
    border-radius: 15px;
    background-clip: padding-box;
    margin: 180px auto;
    width: 350px;
    padding: 15px 35px 15px 35px;
    background: #fff;
    border: 1px solid #eaeaea;
    box-shadow: 0 0 25px #cac6c6;
}

.loginTitle {
    margin: 0px auto 40px auto;
    text-align: center;
}
</style>
