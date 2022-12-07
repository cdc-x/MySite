import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex);

export default new Vuex.Store({
    state: {
        activeIndex: "",
        articleCategory: "",
        articleId: "",
        showFlag: "",
    },

    mutations: {
        changeActiveIndex(state, path){
            state.activeIndex = path;
        },

        changeArticleCategory(state, cate){
            state.articleCategory = cate;
        },

        changeArticleId(state, aid){
            state.articleId = aid
        },

        changeShowFlag(state, val){
            state.showFlag = val
        }
    },
    
    actions: {
        
    }
})