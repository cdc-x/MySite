<template>
    <div class="box-all">
        <h3 class="title">通过本站，你可以了解到以下相关内容</h3>
        <el-row :gutter="20">
            <el-col :span="12">
                <el-card class="box-card">
                    <div slot="header" class="card-title">
                        <span>技术分类</span>
                    </div>
                    <div style="height: 450px; overflow-y: scroll">
                        <el-tag v-for="cate in category" :key="cate.name" :type="cate.type" style="margin: 10px">
                            {{cate.name}}
                        </el-tag>
                    </div>
                </el-card>
            </el-col>
            <el-col :span="12">
                <el-card class="box-card">
                    <div slot="header" class="card-title">
                        <span>技术标签</span>
                    </div>
                    <div style="height: 450px; overflow-y: scroll">
                        <el-tag v-for="tag in tags" :key="tag.name" :type="tag.type" style="margin: 10px;">
                            {{tag.name}}
                        </el-tag>
                    </div>
                </el-card>
            </el-col>
        </el-row>
        
    </div>
</template>

<script>
    export default {
        
        created(){

        },
        
        data(){
            return {
                category: [
                    { name: 'Python学习路线', type: '' },
                    { name: 'GoLang学习路线', type: 'success' },
                ],
                
                tags: [
                    { name: 'Python', type: '' },
                    { name: 'JavaScript', type: 'success' },
                    { name: 'GoLang', type: 'info' },
                    { name: 'HTML', type: 'warning' },
                    { name: 'CSS', type: 'danger' },
                    { name: 'VUE', type: 'danger' },
                    { name: 'Shell', type: 'danger' },
                ],
            }
        },

        methods: {
            // Math.floor(Math.random() * (max - min)) + min
        },
    }
</script>

<style scoped>

    .box-all {
        width: 100%;
        height: calc(80vh);
        margin-top: 30px;
        padding: 20px;
        background-color: #fff;
    }

    .title {
        padding-left: 10px;
        border-left: 5px solid #0bbd87;
    }

    .card-title {
        font-weight: bolder;
    }

    /deep/.el-tag:hover {
        cursor: pointer;
        box-shadow: 2px 5px 14px #c5c5c5;
        -webkit-transform: translate3d(0,-3px,0);
        transform: translate3d(0,-2px,0);
    }

</style>