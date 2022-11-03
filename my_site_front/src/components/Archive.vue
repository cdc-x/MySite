<template>
    <div class="box-all">
        <el-timeline>
            <el-timeline-item v-for="activity in activities" :key="activity.time" :timestamp="activity.time" placement="top" color="#0bbd87">
                <el-card v-for="item in activity.articles" :key="item.id" class="archive-card zoomIn">
                    <h4>归档 {{ item.title }}</h4>
                    <p>更新于 {{ item.category }}</p>
                    <p>技术标签： {{ item.tag }}</p>
                </el-card>
            </el-timeline-item>
        </el-timeline>
    </div>    
</template>

<script>
    export default {
        created(){

        },
        
        data(){
            return {
                activities: [
                    {
                        time: "2020-12-31",
                        articles: [
                            {id: 4, title: "Python面向对象", category: "Python学习之路", tag: "Python"},
                            {id: 3, title: "Python函数", category: "Python学习之路", tag: "Python"},
                        ]
                    },
                    {
                        time: "2020-12-30",
                        articles: [
                            {id: 2, title: "Python基础数据类型", category: "Python学习之路", tag: "Python"},
                        ]
                    },
                    {
                        time: "2020-12-29",
                        articles: [
                            {id: 1, title: "Python初识", category: "Python学习之路", tag: "Python"},
                        ]
                    },
                    {
                        time: "2020-12-28",
                        articles: [
                            {id: 4, title: "Python面向对象", category: "Python学习之路", tag: "Python"},
                            {id: 3, title: "Python函数", category: "Python学习之路", tag: "Python"},
                        ]
                    },
                    {
                        time: "2020-12-27",
                        articles: [
                            {id: 2, title: "Python基础数据类型", category: "Python学习之路", tag: "Python"},
                        ]
                    },
                    {
                        time: "2020-12-26",
                        articles: [
                            {id: 1, title: "Python初识", category: "Python学习之路", tag: "Python"},
                        ]
                    },
                    {
                        time: "2020-12-25",
                        articles: [
                            {id: 4, title: "Python面向对象", category: "Python学习之路", tag: "Python"},
                            {id: 3, title: "Python函数", category: "Python学习之路", tag: "Python"},
                        ]
                    },
                    {
                        time: "2020-12-24",
                        articles: [
                            {id: 2, title: "Python基础数据类型", category: "Python学习之路", tag: "Python"},
                        ]
                    },
                    {
                        time: "2020-12-23",
                        articles: [
                            {id: 1, title: "Python初识", category: "Python学习之路", tag: "Python"},
                        ]
                    }
                ]
            }
        },

        methods: {

        },
    }
</script>

<style scoped>

    .box-all {
        height: 100%;
        width: 100%;
        margin-top: 20px;
        padding: 20px;
        background-color: #fff;
    }

    .archive-card {
        margin-bottom: 10px; 
        width: 90%; 
        visibility: visible; 
        animation-duration: 1s;
    }

    .zoomIn {
        -webkit-animation-name: zoomIn;
        animation-name: zoomIn;
    }
</style>