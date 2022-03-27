<template>
  <el-popconfirm
  confirm-button-text='确定'
  cancel-button-text='留着吧'
  icon="el-icon-info"
  icon-color="red"
  title="确定已完成了吗？"
  >
    <el-button slot="reference" class="onething">
        {{ thing }}
        <slot></slot>
    </el-button>
  </el-popconfirm>
</template>

<script>

export default {
    name: 'OneThing',
    props: ['thing']
}
</script>

<style scoped>

.onething {
  margin: 10px;
}

</style>