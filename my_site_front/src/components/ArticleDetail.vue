<template>
    <div style="height:100%;">
        <el-row :gutter='20' style="margin-top: 20px;">
            <el-col :span='18'>
                <!-- 文章列表及内容显示区域 -->
                <mavon-editor 
                    v-model="articleContent"
                    :external-link="externalLink" 
                    :subfield="false"
                    :defaultOpen="'preview'"
                    :editable="false"
                    :toolbarsFlag="false"
                    :scrollStyle="true"
                    :ishljs="true">
                </mavon-editor>

                <div class="content-footer">
                    <button @click="thumbArticle()" class="thumb-btn" :class="{'thumbed': articleThumbed}" :disabled="articleThumbed">
                        <span class="iconfont icon-dianzan"></span>
                        <span>{{articleThumbed?"已赞":"已赞"}} {{articleThumbNum}}</span>
                    </button>
                    <div>
                        本文于 {{articlePubTime}} 发布在 {{articleCate}} 专题
                    </div>
                    <div>
                        &copy;自由转载 - 署名 - 非商业性使用
                    </div>
                </div>

                <!-- 快速返回文章列表 -->
                <el-button icon="el-icon-caret-left" circle class="back-up" @click="backUp()"></el-button>

                <!-- 快速返回顶部 -->
                <el-button icon="el-icon-caret-top" circle class="back-top" v-if="topLeft < -50" @click="backTop()"></el-button>

            </el-col>
            <el-col :span='6'>
                <el-card class="box-card" style="margin-bottom: 10px">
                    <div class="article-title border-style" @click="topMao(articleInfo.href)">
                        <div style="font-size: 14px;font-weight: bold;padding-left: 12px">{{ articleInfo.title }}</div>
                        <div style="font-size: 12px; color: gray;padding-left: 12px">共{{ articleInfo.count }}字</div>
                    </div>
                    
                    <div class="article-menu border-style">
                        <el-scrollbar style="height:100%;">
                        <ul style="margin: 0; padding: 6px">
                            <li v-for="(item, index) in menuList" :key="index" class="article-menu-item" :class="item.level" @click="topMao(item.href)">{{ item.title }}</li>
                        </ul>
                        </el-scrollbar>
                    </div>

                    <div class="article-footer border-style" style="color: gray">
                        <i class="iconfont icon-heart" style="font-size: 14px; padding: 0 12px; margin: 0; border-right: 2px solid gray;">
                            <span style="margin-left: 5px">按赞</span>
                        </i>
                        <i class="iconfont icon-yanjing" style="font-size: 14px; padding:0 12px; margin: 0; border-right: 2px solid gray;">
                            <span style="margin-left: 5px">{{articleBrowseNum}}</span>
                        </i>
                        <i class="iconfont icon-dianzan" style="font-size: 14px; padding:0 12px;">
                            <span style="margin-left: 5px">{{articleThumbNum}}</span>
                        </i>
                    </div>
                </el-card>

                <div ref="scrollJudgeRef">
                    <el-card class="box-card">
                        <div slot="header" class="clearfix" style="font-size: 14px;font-weight: bold;">
                            打赏一下
                        </div>
                        <div class="support">
                            <div style="height: 65%; width: 65%">
                                <img src="/static/img/contact/support.png" style="height: 100%; width: 100%">
                            </div>
                        </div>
                    </el-card>
                </div>

                <div class="fixed-item" v-if="topLeft <= -250">
                    <el-card class="box-card" style="margin-bottom: 10px">
                        <div class="article-title border-style" @click="topMao(articleInfo.href)">
                            <div style="font-size: 14px;font-weight: bold;padding-left: 12px">{{ articleInfo.title }}</div>
                            <div style="font-size: 12px; color: gray;padding-left: 12px">共{{ articleInfo.count }}字</div>
                        </div>
                        
                        <div class="article-menu border-style">
                            <el-scrollbar style="height:100%;">
                            <ul style="margin: 0; padding: 6px">
                                <li v-for="(item, index) in menuList" :key="index" class="article-menu-item" :class="item.level" @click="topMao(item.href)">{{ item.title }}</li>
                            </ul>
                            </el-scrollbar>
                        </div>

                        <div class="article-footer border-style" style="color: gray">
                            <i class="iconfont icon-heart" style="font-size: 14px; padding: 0 12px; margin: 0; border-right: 2px solid gray;">
                                <span style="margin-left: 5px">按赞</span>
                            </i>
                            <i class="iconfont icon-yanjing" style="font-size: 14px; padding:0 12px; margin: 0; border-right: 2px solid gray;">
                                <span style="margin-left: 5px">{{articleBrowseNum}}</span>
                            </i>
                            <i class="iconfont icon-dianzan" style="font-size: 14px; padding:0 12px;">
                                <span style="margin-left: 5px">{{articleThumbNum}}</span>
                            </i>
                        </div>
                    </el-card>

                    <div>
                        <el-card class="box-card">
                            <div slot="header" class="clearfix" style="font-size: 14px;font-weight: bold;">
                                打赏一下
                            </div>
                            <div class="support">
                                <div style="height: 65%; width: 65%">
                                    <img src="/static/img/contact/support.png" style="height: 100%; width: 100%">
                                </div>
                            </div>
                        </el-card>
                    </div>
                </div>
            </el-col>
        </el-row>
    </div>
</template>

<script>
    export default {

        created(){
            this.getArticleInfo()
        },

        mounted(){
            window.addEventListener('scroll', this.handleScrollx, true)
        },
        
        data(){
            return {
                // mavon-editor 本地加载设置
                externalLink: {
                    markdown_css: () => '../static/md/markdown/github-markdown.min.css',
                    hljs_js: () => '../static/md/highlightjs/highlight.min.js',
                    hljs_css: (css) => '../static/md/highlightjs/styles/' + css + '.min.css',
                    hljs_lang: (lang) => '../static/md/highlightjs/languages/' + lang + '.min.js',
                    katex_css: () => '../static/md/katex/katex.min.css',
                    katex_js: () => '../static/md/katex/katex.min.js',
                },

                // 文章内容
                articleContent: "",

                // 文章点赞数
                articleThumbNum: 0,

                // 文章浏览数
                articleBrowseNum: 0,

                // 文章发布时间
                articlePubTime: "",

                // 当前文章ID
                articleId: "",

                // 文章分类
                articleCate: "",

                // 文章是否已点赞
                articleThumbed: false,

                // 文章菜单
                menuList: [],

                // 显示内容距离窗口顶部的距离
                topLeft: 0,

                // 文章标题及字数统计
                articleInfo: {}
            }
        },

        methods: {
            // 查询文章内容
            getArticleContent(){
                return this.$http.get("/article/content?p=" + this.articleId)
            },

            // 查询文章点赞数
            getArticleThumbNum(){
                return this.$http.get("/article/count/thumb?p=" + this.articleId)
            },

            // 查询文章点赞数
            getArticleThumbNum2(){
                this.$http.get("/article/count/thumb?p=" + this.articleId).then(response => {
                    const res = response.data
                    this.articleThumbNum = res.data
                })
            },

            // 查询文章浏览数
            getArticleBrowseNum(){
                return this.$http.get("/article/count/browse?p=" + this.articleId)
            },

            // 查询当前用户是否已点赞当前文章
            getArticleThumbed(){
                return this.$http.get("/article/check/thumb?p=" + this.articleId)
            },

            // 查询文章详细信息
            getArticleInfo(){
                this.articleId = this.$store.state.articleId
                this.$http.all([this.getArticleContent(), this.getArticleThumbNum(), this.getArticleBrowseNum(), this.getArticleThumbed()]).then(
                    this.$http.spread((res1, res2, res3, res4) => {
                        let _articleInfo = res1.data;
                        let _thumbInfo = res2.data;
                        let _browseInfo = res3.data;
                        let _thumbed = res4.data;
                        
                        this.articleContent = _articleInfo.data
                        this.articlePubTime = _articleInfo.pub_time
                        this.articleCate = _articleInfo.category
                        this.getArticleMenu()

                        this.articleThumbNum = _thumbInfo.data

                        this.articleBrowseNum = _browseInfo.data

                        this.articleThumbed = _thumbed.flag
                    })
                )
            },
            
            // 点击返回顶部
            backTop(){
                this.topMao(this.articleInfo.href)
            },

            // 返回文章列表
            backUp(){
                this.$parent.showFlag = "list"
            },

            // 文章点赞
            thumbArticle(){
                if (this.articleThumbed === false){
                    this.$http.get("/article/thumb?p=" + this.articleId).then(response => {
                        this.getArticleThumbNum2(this.articleId)
                        this.articleThumbed = true
                    })
                }
            },

            // 获取文章菜单
            getArticleMenu(){
                let menuList = []
                let articleInfo = {
                    title: "",
                    count: 0,
                    href: ""
                }

                this.$nextTick(() => {
                    let _aList = document.querySelectorAll(".v-show-content a");
                    articleInfo.count = document.getElementsByClassName("v-show-content")[0].innerText.length;
                    for (let i = 0; i < _aList.length; i++){
                        parent = _aList[i].parentNode;
                        if (_aList[i].id && parent.tagName !== "H1"){
                            let _data = {
                                title: parent.innerText, 
                                href: _aList[i].id,
                                level: "level1"
                            };

                            if (parent.tagName === "H3"){
                                _data.level = "level2"
                            }else if (parent.tagName === "H4"){
                                _data.level = "level3"
                            }else if (parent.tagName === "H5"){
                                _data.level = "level4"
                            }
                            menuList.push(_data)
                        }else {
                            if (_aList[i].id && parent.tagName === "H1"){
                                articleInfo.title = parent.innerText;
                                articleInfo.href = _aList[i].id;
                            }
                        }

                    };
                })
                this.menuList = menuList;
                this.articleInfo = articleInfo;
            },

            // 点击跳转菜单指定位置处
            topMao(id){
                let dHeight = document.documentElement.clientHeight;
                let elem = document.getElementById(id).parentNode;
                let oldHeight = elem.style.height;
                elem.style.height = dHeight - 70 + "px";
                elem.scrollIntoView(false);
                elem.style.height = oldHeight;
            },

            // 监控滚动 
            handleScrollx(){
                this.$nextTick(() => {
                    if (this.$refs.scrollJudgeRef){
                        this.topLeft = this.$refs.scrollJudgeRef.getBoundingClientRect().top;
                    }
                })
            },
        },
    }
</script>

<style scoped src="@/assets/css/detail.css">

</style>