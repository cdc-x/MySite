import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex);

export default new Vuex.Store({
    state: {
        activeIndex: "",
        articleCategory: "",
    },

    mutations: {
        changeActiveIndex(state, path){
            state.activeIndex = path;
        },

        changeArticleCategory(state, cate){
            state.articleCategory = cate;
        },
    },
    
    actions: {
        
    }
})