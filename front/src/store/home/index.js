import {reqHundredThingsList} from '@/api';
import { reqDaysMatters } from '@/api';

// home模块的小仓库
const state = {
    //state中的数据的默认初始值别瞎写，服务器返回的是对象，初始值就是对象
    //服务器返回的是数组，初始值就是数组
    HundredThingsList: {},
    DaysMattersList: []
};
const mutations = {
    HundredThingsList(state, HundredThingsList){
        state.HundredThingsList = HundredThingsList;
    },
    DaysMattersList(state, DaysMattersList){
        state.DaysMattersList = DaysMattersList;
    }
};
const actions = {
    //通过API里面的接口函数调用，向服务器发请求，获取服务器的数据
    async hundredThingsList({commit}){
        let result = await reqHundredThingsList();
        if(result.code==200){
            commit("HundredThingsList", result.data);
        }
    },
    async daysMattersList({commit}){
        let result = await reqDaysMatters();
        if(result.code==200){
            commit("DaysMattersList", result.data);
        }
    }
};
const getters = {};

export default {
    state,
    mutations,
    actions,
    getters
}