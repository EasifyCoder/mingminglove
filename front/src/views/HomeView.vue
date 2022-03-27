<template>
  <div class="home">
    <img alt="Vue logo" src="../assets/logo.png">
    <HelloWorld msg="Welcome to Your Vue.js App"/>
    <EventBlock/>
  </div>
</template>

<script>
// @ is an alias to /src
import HelloWorld from '@/components/HelloWorld.vue'
import EventBlock from '@/components/EventBlock'

export default {
  name: 'HomeView',
  components: {
    HelloWorld,
    EventBlock
  }
}
</script>
