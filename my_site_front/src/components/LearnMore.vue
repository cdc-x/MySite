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
                        <el-tag v-for="cate in articleCategoryMap" :key="cate.id" :type="cate.type" style="margin: 10px" @click="getArticleByCategory(cate.category, cate.id)">
                            {{cate.category}}
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
                        <el-tag v-for="tag in articleTagMap" :key="tag.id" :type="tag.type" style="margin: 10px;" @click="getArticleByTag(tag.tag, tag.id)">
                            {{tag.tag}}
                        </el-tag>
                    </div>
                </el-card>
            </el-col>
        </el-row>
        
        <div class="useful-tools clearfix" v-if="titpTitle">
            <div>
                <h3 class="tools-title">{{ titpTitle }}</h3>
            </div>
            <el-row :gutter="40">
                <el-col :span="12">
                    <ul class="tool-list">
                        <li v-for="article in articleListLeft" :key="article.id" @click="getArticleContent(article.id)">{{ article.title }}</li>
                    </ul>
                </el-col>
                <el-col :span="12">
                    <ul class="tool-list">
                        <li v-for="article in articleListRight" :key="article.id" @click="getArticleContent(article.id)">{{ article.title }}</li>
                    </ul>
                </el-col>
            </el-row>
        </div>

    </div>
</template>

<script>
    export default {
        
        created(){
            this.getArticleCategory()
            this.getArticleTags()
        },
        
        data(){
            return {
                colorMap: {
                    "0": "",
                    "1": "success",
                    "2": "info",
                    "3": "warning",
                    "4": "danger",
                },
                articleCategoryMap: [],
                articleTagMap: [],
                articleListLeft: [],
                articleListRight: [],
                titpTitle: "",
            }
        },

        methods: {
            // 查询所有的文章分类
            getArticleCategory(){
                this.$http.get("q/article/category").then(response => {
                    const res = response.data
                    if (res.status_code === 1000){
                        this.articleCategoryMap = res.data

                        for (let i = 0; i < this.articleCategoryMap.length; i++){
                            this.articleCategoryMap[i].type = this.colorMap[(this.articleCategoryMap[i]["id"] % 5).toString()]
                        }
                    }
                })
            },

            // 查询所有文章标签
            getArticleTags(){
                this.$http.get("q/article/tags").then(response => {
                    const res = response.data
                    if (res.status_code === 1000){
                        this.articleTagMap = res.data

                        for (let i = 0; i < this.articleTagMap.length; i++){
                            this.articleTagMap[i].type = this.colorMap[(this.articleTagMap[i]["id"] % 5).toString()]
                        }
                    }
                })
            },

            // 根据文章分类查询文章内容
            getArticleByCategory(cate, cid){
                this.titpTitle = "文章分类【" + cate + "】"
                this.$http.get("q/article/search_by_category?cid=" + cid).then(response => {
                    const res = response.data
                    if (res.status_code === 1000){
                        this.articleListLeft = res.data.slice(0, Math.ceil(res.data.length / 2))
                        this.articleListRight = res.data.slice(Math.ceil(res.data.length / 2))
                    }
                })
            },

            // 根据文章标签查询文章内容
            getArticleByTag(tag, tid){
                this.titpTitle = "文章标签【" + tag + "】"
                this.$http.get("q/article/search_by_tag?tid=" + tid).then(response => {
                    const res = response.data
                    if (res.status_code === 1000){
                        this.articleListLeft = res.data.slice(0, Math.ceil(res.data.length / 2))
                        this.articleListRight = res.data.slice(Math.ceil(res.data.length / 2))
                    }
                })
            },

            getArticleContent(aid){
                this.$store.commit('changeArticleId', aid)
                this.$store.commit('changeShowFlag', "detail")
                this.$parent.activeIndex = "/blog"
            }
        },
    }
</script>

<style scoped>

    .box-all {
        width: 100%;
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

    .tools-title {
        line-height: 30px;
        height: 30px;
        font-weight: bold;
        padding-left: 10px;
    }

    .useful-tools .tools-title {
        border-left: 5px solid #06a2c9;
    }

    .clearfix::after {
        content: "";
        display: block;
        clear: both;
    }

    .tool-list {
        padding: 0;
    }

    .tool-list li {
        float: left;
        width: 100%;
        margin: 5px 0;
    }

    li {
        list-style: none;
    }

    .tool-list li:hover {
        cursor: pointer;
        color: #0088F5;
    }

 
</style>