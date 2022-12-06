<template>
    <div class="all-box">
        <div v-if="showFlag === 'list'">
            <div class="col-content">
            <div class="inner">
                <article class="article-list bloglist" id="LAY_bloglist">
                    <section class="article-item zoomIn article" v-for="item in articleList" :key="item.id">
                        <div class="fc-flag">原创</div>
                        <h5 class="title">
                            <span class="fc-blue">【{{ item.category }}】</span>
                            <a @click="getArticleContent(item.id)">{{ item.title }}</a>
                        </h5>
                        <div class="time">
                            <span class="day">{{ item.publish_day }}</span>
                            <span class="month fs-18">{{ item.publish_month }}<span class="fs-14">月</span>
                            </span>
                            <span class="year fs-18 ml10">{{ item.publish_year }}</span>
                        </div>
                        <div class="content">
                            <a class="cover img-light">
                                <img :src="item.img_path">
                            </a>
                            {{ item.desc }}
                        </div>
                        <div class="read-more">
                            <a class="fc-black f-fwb" @click="getArticleContent(item.id)">继续阅读</a>
                        </div>
                        <aside class="f-oh footer">
                            <div class="f-fl tags">
                                <i class="iconfont icon-biaoqian fs-16"></i>
                                <a class="tag" v-for="_tag in item.tags" :key="_tag">{{ _tag }}</a>
                            </div>
                            <div class="f-fr">
                                <span class="read">
                                    <i class="iconfont icon-yanjing fs-16"></i>
                                    <i class="num">{{ item.browse }}</i>
                                </span>
                                <span class="ml20">
                                    <i class="iconfont icon-dianzan fs-16"></i>
                                    <a class="num fc-grey">{{ item.thumb }}</a>
                                </span>
                            </div>
                        </aside>
                    </section>
                </article>

                <div style="margin-top: 16px" :class="{'article-load-outer': articleList.length === total}">
                    <div class="article-load" @click="handleCurrentChange()" :class="{'dis-click': articleList.length === total}">
                        <span class="left">
                            <div class="page-num">
                                {{ articleList.length }} / {{ total }}
                            </div>
                        </span>
                        <span class="right">
                            <div class="page-more">
                                More
                                <span class="iconfont icon-et-more"></span>
                            </div>
                        </span>
                    </div>
                </div>    

            </div>
        </div>
        <div class="col-other">
            <div class="inner">
                <div class="other-item" id="categoryandsearch">
                    <div class="search">
                        <label class="search-wrap">
                            <input type="text" id="searchtxt" placeholder="输入关键字搜索" v-model="searchContent"/>
                            <span class="search-icon" @click="getArticleListByTitle()">
                                <i class="iconfont icon-sousuoxiao"></i>
                            </span>
                        </label>
                        <ul class="search-result"></ul>
                    </div>
                    <ul class="category" id="category">
                        <li :data-index="_tag.id" v-for="_tag in articleTagMap" :key="_tag.id" @click="getArticleListByTag(_tag.tag)"><a>{{ _tag.tag }}</a></li>
                    </ul>
                </div>
                <!-- 手机平板模式 -->
                <div class="category-toggle" :class="{layuiHide: leftMenuOpen}" @click="openLeftMenu()"><i class="iconfont icon-zuojiantou"></i></div>
                <div class="article-category" :class="{categoryOut: !leftMenuOpen, categoryIn: leftMenuOpen, layuiShow: leftMenuOpen}">
                    <div class="article-category-title">分类导航</div>
                            <a href="/Blog/Article/1/">Java</a>
                            <a href="/Blog/Article/2/">前端</a>
                            <a href="/Blog/Article/3/">Python</a>
                    <div class="f-cb"></div>
                </div>
                <!--遮罩-->
                <div class="blog-mask animated" :class="{layuiHide: !leftMenuOpen, layuiShow: leftMenuOpen, maskOut: !leftMenuOpen, maskIn: leftMenuOpen}" @click="closeLeftMenu()"></div>

                <div class="other-item" ref="scrollJudgeRef">
                    <h5 class="other-item-title">热门文章</h5>
                    <div class="inner">
                        <ul class="hot-list-article">
                            <li v-for="hot in hotArticleList" :key="hot.id"><a @click="getArticleContent(hot.id)">{{ hot.title }}</a></li>
                        </ul>
                    </div>
                </div>

                <!-- 固定区域展示 -->
                <div class="other-item" id="categoryandsearchfixed" v-if="topLeft < -300">
                    <div class="search">
                        <label class="search-wrap">
                            <input type="text" id="searchtxt" placeholder="输入关键字搜索" v-model="searchContent"/>
                            <span class="search-icon" @click="getArticleListByTitle()">
                                <i class="iconfont icon-sousuoxiao"></i>
                            </span>
                        </label>
                        <ul class="search-result"></ul>
                    </div>
                    <ul class="category" id="category">
                        <li :data-index="_tag.id" v-for="_tag in articleTagMap" :key="_tag.id" @click="getArticleListByTag(_tag.tag)"><a>{{ _tag.tag }}</a></li>
                    </ul>
                </div>

            </div>
        </div>
        </div>
        <div v-if="showFlag === 'detail'">
            <article-detail></article-detail>
        </div>
    </div>    
</template>

<script>

    import articleDetail from './ArticleDetail.vue'

    export default {

        created(){
            this.searchCategory = this.$store.state.articleCategory
            this.initArticleList()
            this.getTagMap()
            this.getHotArticleList()
            
        },

        components: {
            articleDetail,
        },

        mounted(){
            window.addEventListener('scroll', this.handleScrollx, true)
        },

        data(){
            return {
                // 左侧菜单栏打开关闭状态
                leftMenuOpen: false,
                // 显示内容距离窗口顶部的距离
                topLeft: 0,
                // 搜索文章的分类
                searchCategory: "",
                // 搜索文章的标签
                searchTag: "",
                // 搜索文章的内容
                searchContent:"",
                // 文章列表
                articleList: [],
                // 文章总数
                total: 0,
                // 当前文章页码
                page: 1,
                // 热门文章列表
                hotArticleList: [],
                // 文章标签映射
                articleTagMap: [],
                // 用于标识显示文章列表还是内容
                showFlag: "list",

            }
        },

        methods: {
            openLeftMenu(){
                this.leftMenuOpen = true
            },

            closeLeftMenu(){
                this.leftMenuOpen = false
            },

            handleScrollx(){
                this.$nextTick(() => {
                    if (this.$refs.scrollJudgeRef){
                        this.topLeft = this.$refs.scrollJudgeRef.getBoundingClientRect().top;
                    }
                })
            },

            // 查询所有文章列表
            initArticleList(){
                this.page = 1
                this.searchTag = ""
                this.searchContent = ""
                let url = "article/all?page=" + this.page
                if (this.searchCategory){
                    url = url + "&category=" + this.searchCategory
                }

                this.$http.get(url).then(response => {
                    const res = response.data

                    if (res.status_code === 1000){
                        this.articleList = res.data
                        this.total = res.total

                        for(let i = 0; i < this.articleList.length; i++){
                            this.articleList[i].img_path = "/static/img/blog/" + this.articleList[i].main_tag + ".jpeg"
                        }
                    }
                })
            },

            // 根据内容搜索文章
            getArticleListByTitle(){
                this.page = 1
                this.searchCategory = ""
                this.searchTag = ""
                let url = "article/all?page=" + this.page + "&content=" + this.searchContent

                this.$http.get(url).then(response => {
                    const res = response.data

                    if (res.status_code === 1000){
                        this.articleList = res.data
                        this.total = res.total

                        for(let i = 0; i < this.articleList.length; i++){
                            this.articleList[i].img_path = "/static/img/blog/" + this.articleList[i].main_tag + ".jpeg"
                        }
                    }
                })
            },

            // 根据标签搜索文章
            getArticleListByTag(tag){
                this.page = 1
                this.searchCategory = ""
                this.searchContent = ""
                this.searchTag = tag
                let url = "article/all?page=" + this.page + "&tag=" + this.searchTag

                this.$http.get(url).then(response => {
                    const res = response.data

                    if (res.status_code === 1000){
                        this.articleList = res.data
                        this.total = res.total

                        for(let i = 0; i < this.articleList.length; i++){
                            this.articleList[i].img_path = "/static/img/blog/" + this.articleList[i].main_tag + ".jpeg"
                        }
                    }
                })
            },
            
            // 分页
            handleCurrentChange(newPage){
                this.page ++;
                let url = "article/all?page=" + this.page
                if (this.searchContent.length !== 0) {
                    url =  url + "&content=" + this.searchContent
                }else if (this.searchTag.length !== 0) {
                    url = url + "&tag=" + this.searchTag
                }else if(this.searchCategory.length !== 0){
                    url = url + "&category=" + this.searchCategory
                }

                this.$http.get(url).then(response => {
                    if (response.status == 200){
                        const res = response.data
                        this.total = res.total

                        if (res.page === 1){
                            this.articleList = res.data
                        }else {
                            this.articleList = this.articleList.concat(res.data)
                        }

                        for(let i = 0; i < this.articleList.length; i++){
                            this.articleList[i].img_path = "/static/img/blog/" + this.articleList[i].main_tag + ".jpeg"
                        }
                        
                    }
                })
            },

            // 查询热门文章
            getHotArticleList(){
                this.$http.get("article/hot").then(response => {
                    const res = response.data

                    if (res.status_code === 1000){
                        this.hotArticleList = res.data
                    }
                })
            },

            // 差选所有的Tag映射数据
            getTagMap(){
                this.$http.get("article/tags").then(response => {
                    const res = response.data
                    if (res.status_code === 1000){
                        this.articleTagMap = res.data
                    }
                })
            },

            // 获取文章详情
            getArticleContent(aid){
                this.showFlag = "detail"
                this.$store.commit('changeArticleId', aid)
            },
        },
        
    }
</script>

<style scoped src="@/assets/css/blog-style.css">

</style>