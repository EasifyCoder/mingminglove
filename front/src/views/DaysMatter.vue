<template>
  <div> 
    <div v-for="(event,index) in DaysMattersList" :key="index">
      <EventBlock :description="event.description" :date="event.date" :days="event.days"></EventBlock>
    </div>
  </div>
</template>

<script>
  import EventBlock from '@/components/EventBlock'
  import {mapState} from 'vuex';

  export default {
    name: 'DaysMatter',
    data(){
      return {}
    },
    components: {
      EventBlock
    },
    computed: {
      ...mapState({
        DaysMattersList: state => state.home.DaysMattersList
      }),
    }
  }
</script>