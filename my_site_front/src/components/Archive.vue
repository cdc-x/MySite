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
            this.getArchiveData()
        },
        
        data(){
            return {
                activities: []
            }
        },

        methods: {
            getArchiveData(){
                 this.$http.get("q/archive").then(response => {
                    const res = response.data;
                    if (res.status_code === 1000){
                        this.activities = res.data
                    }
                })
            }
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