<template>
  <div>
    <el-container>
      <el-header>
        <el-menu :default-active="activeIndex" class="el-menu-demo" mode="horizontal" @select="handleSelect">
          <el-menu-item index="1">
            <router-link :to="{name:'DaysMatter'}">
              Days Matter
            </router-link>
          </el-menu-item>
          <el-menu-item index="2">
            <router-link :to="{name:'HundredThings'}">
              HundredThings
            </router-link>
          </el-menu-item>
          <el-menu-item index="3">
            <router-link :to="{name:'ImageWall'}">
              照片墙
            </router-link>
          </el-menu-item>
          <el-menu-item index="4">
            <router-link :to="{name:'Memorandum'}">
              备忘录
            </router-link>
          </el-menu-item>
        </el-menu>
      </el-header>
      <el-main>
        <router-view />
      </el-main>
      <el-footer>Footer</el-footer>
    </el-container>
  </div>
</template>

<script>
import {mapState} from 'vuex';

export default {
    name: 'Home',
    //组件挂载完毕：可以向服务器发请求
    mounted(){
      //通知vuex发请求，获取数据，存储于仓库当中
      //hundredThings模块
      this.$store.dispatch('hundredThingsList');
      //daysMatter模块
      this.$store.dispatch('daysMattersList');
    },
    data() {
      return {
        activeIndex: '1'
      };
    },
    methods: {
      handleSelect(key, keyPath) {
        console.log(key, keyPath);
      }
    },
    computed:{
      ...mapState({
        HundredThingsList: state => state.home.HundredThingsList
      })
    }
  }
</script>

<style scoped>
.router-link-active {
  text-decoration: none;
}

</style>
