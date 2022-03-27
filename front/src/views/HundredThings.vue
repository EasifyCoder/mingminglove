<template>
  <div> 
    <h1>未完成的事情</h1>
    <div v-for="(thing,index) in Things" :key="index">
      <OneThing :thing="thing"></OneThing>
    </div>

    <h1>已经完成的事情</h1>
    <div v-for="(thing,index) in DoneThings" :key="index+ '-only'">
      <OneThing :thing="thing"></OneThing>
    </div>


    <!-- Form -->
    <el-button type="text" icon="el-icon-plus" size="medium" @click="dialogFormVisible = true">添加事件</el-button>

    <el-dialog title="待完成的一百件事" :visible.sync="dialogFormVisible">
      <el-form :model="form">
        <el-form-item label="活动名称" :label-width="formLabelWidth">
          <el-input v-model="form.name" autocomplete="off"></el-input>
        </el-form-item>
        <el-form-item label="是否完成" :label-width="formLabelWidth">
          <el-select v-model="form.done" placeholder="请选择是否完成">
            <el-option label="未完成" value="0"></el-option>
            <el-option label="已完成" value="1"></el-option>
          </el-select>
        </el-form-item>
      </el-form>
      <div slot="footer" class="dialog-footer">
        <el-button @click="dialogFormVisible = false">取 消</el-button>
        <el-button type="primary" @click="submitThing">确 定</el-button>
      </div>
    </el-dialog>

  </div>
</template>

<script>
  import OneThing from '@/components/OneThing'
  import {mapState} from 'vuex';
  import {submitThing} from '@/api';

  export default {
    name: 'HundredThings',
    data(){
      return {
        dialogFormVisible: false,
        form: {
          name: '',
          done: ''
        },
        formLabelWidth: '120px'
      }
    },
    components: {
      OneThing
    },
    computed: {
      ...mapState({
        DoneThings: state => state.home.HundredThingsList.done,
        Things: state => state.home.HundredThingsList.undone
      }),
    },
    methods: {
      submitThing() {
        this.dialogFormVisible = false;
        submitThing(this.form);
      }
    }
  }
</script>