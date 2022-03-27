//当前这个模块：API进行统一管理
import requests from "./request";

//HundredThings接口
// /api/home/getHundredThings get
export const reqHundredThingsList = ()=>requests({url: '/home/getHundredThings', method:'get'});

//DaysMatters接口
export const reqDaysMatters = ()=>requests({url: '/home/getDaysMatters', method:'get'});

//登录接口
export function login(data) {
    return requests({
        method: 'POST',
        url: '/auth/login',
        data: data
    })
}

//上传一个Thing到HundredThings
export function submitThing(data) {
    return requests({
        method: 'POST',
        url: '/home/submitThing',
        data: data
    })
}








