<template>
    <div id="eventblock">
        <div id="desc">{{ description }}</div>
        <div id="days">{{ days }}</div>
        <div id="date">{{ date }}</div>
    </div>
</template>

<script>
    export default {
        name: "event",
        props: ['description', 'date', 'days'],
        data() {
            return {
                
            }
        }
    }
</script>

<style scoped>

#eventblock {
    display: inline-block;
    border-radius: 10px;
    height: 180px;
    width: 300px;
    border: 1px solid gray;
}

#desc {
    height: 50px;
    background: #1270ca;
    border-radius: 10px 10px 0px 0px;
    text-align: center;
    font-size: 30px;
    line-height: 50px;
    color: white;
}

#days {
    height: 100px;
    font-size: 80px;
    line-height: 100px;
}

#date {
    height: 30px;
    background: grey;
    border-radius: 0px 0px 10px 10px;
    font-size: 20px;
    line-height: 30px;
}

</style>