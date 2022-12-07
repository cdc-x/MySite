<template>
    <div class="box-all">
        <div class="header">
            <header class="gird-header">
                <div class="header-fixed">
                    <div class="header-inner">
                        <a class="header-logo" id="logo">Mr.Chen</a>
                        <nav class="nav" id="nav">
                            <ul>
                                <li @mouseenter="moveCurrent('/index')" @mouseleave="moveCurrent('')" @click="changeCurrent('/index')" :class="{current: moveIndex==='/index' || activeIndex==='/index'}">
                                    <a>首页</a>
                                </li>
                                <li @mouseenter="moveCurrent('/blog')" @mouseleave="moveCurrent('')" @click="changeCurrent('/blog')" :class="{current: moveIndex==='/blog' || activeIndex==='/blog'}">
                                    <a>博客</a>
                                </li>
                                <li @mouseenter="moveCurrent('/project')" @mouseleave="moveCurrent('')" @click="changeCurrent('/project')" :class="{current: moveIndex==='/project' || activeIndex==='/project'}">
                                    <a>项目</a>
                                </li>
                                <li @mouseenter="moveCurrent('/archive')" @mouseleave="moveCurrent('')" @click="changeCurrent('/archive')" :class="{current: moveIndex==='/archive' || activeIndex==='/archive'}">
                                    <a>归档</a>
                                </li>
                                <li @mouseenter="moveCurrent('/link')" @mouseleave="moveCurrent('')" @click="changeCurrent('/link')" :class="{current: moveIndex==='/link' || activeIndex==='/link'}">
                                    <a>友链</a>
                                </li>
                            </ul>
                        </nav>
                    </div>
                </div>
            </header>

            <div class="doc-container" id="doc-container">
                <div class="container-fixed">
                    <blog v-if="activeIndex === '/blog'"></blog>
                    <project v-if="activeIndex === '/project'"></project>
                    <archive v-if="activeIndex === '/archive'"></archive>
                    <about-link v-if="activeIndex === '/link'"></about-link>
                    <about-site v-if="activeIndex === '/about/site'"></about-site>
                    <learn-more v-if="activeIndex === '/learn/more'"></learn-more>
                </div>
            </div>

            <footer class="grid-footer">
                <div class="footer-fixed">
                    <div class="copyright">
                        <div class="info">
                            <div class="contact">
                                <a class="github" @click="showContact('github')"><i class="iconfont icon-github"></i></a>
                                <a class="weixin" @click="showContact('wechat')"><i class="iconfont icon-weixin"></i></a>
                                <a class="qq" @click="showContact('qq')"><i class="iconfont icon-QQ"></i></a>
                                <a class="gzh" @click="showContact('gzh')"><i class="iconfont icon-daohang-gongzhonghaotixing"></i></a>
                            </div>
                            <p class="mt05">
                                Copyright © 2022-2099 CDC-博客 All Rights Reserved V.3.1.3 Power by CDC-博客
                            </p>
                        </div>
                    </div>
                </div>
            </footer>

             <!-- 社交码显示区域 -->
            <div class="show-contact" v-if="isShowContact">
                <div class="contact-content">
                    <el-card>
                        <div slot="header" class="clearfix" style="font-size: 20px; font-weight: bold;">
                            <span>{{contactTite}}</span>
                        </div>
                        <div style="height: 300px; width: 300px; margin: 0 auto;">
                            <img :src="contactImg" style="width: 100%; height: 100%">
                        </div>
                    </el-card>
                </div>

                <!-- 二维码关闭按钮 -->
                <el-button icon="el-icon-close" circle class="contact-close" @click="closeContact()"></el-button>
            </div>
        </div>
    </div>
</template>

<script>
    import Blog from './Blog.vue'
    import Project from './Project.vue'
    import Archive from './Archive.vue'
    import aboutLink from './Link.vue'
    import aboutSite from './AboutSite.vue'
    import learnMore from './LearnMore.vue'

    export default {

        created(){
            this.activeIndex = this.$store.state.activeIndex?this.$store.state.activeIndex:'/blog'
        },

        components: {
            Blog,
            Project,
            Archive,
            aboutLink,
            aboutSite,
            learnMore,
        },

        data(){
            return {
                // 当前选中的菜单
                activeIndex: "",
                // 当前鼠标移动到的菜单
                moveIndex: "",
                // 点击展示社交二维码
                isShowContact: false,
                // 展示的平台标题
                contactImg: "",
                // 展示的二维码
                contactTite: "",

            }
        },

        methods: {
            moveCurrent(item){
                this.moveIndex = item
            },

            changeCurrent(item){
                if (item === "/index"){
                    this.$router.push('/')
                }
                this.$store.commit('changeShowFlag', "list")
                this.$store.commit('changeArticleCategory', "")
                this.activeIndex = item
            },

            // 点击展示社交工具
            showContact(contactType){
                if (contactType == 'qq'){
                    this.isShowContact = true
                    this.contactImg = "/static/img/contact/qq.png"
                    this.contactTite = "QQ号搜索: 1275500642"
                }else if (contactType == 'wechat'){
                    this.isShowContact = true
                    this.contactImg = "/static/img/contact/wechat.png"
                    this.contactTite = "微信号搜索: CDC1275500642"
                }else if (contactType == 'gzh'){
                    this.isShowContact = true
                    this.contactImg = "/static/img/contact/gzh.png"
                    this.contactTite = "公众号搜索: cdc-54be3793"
                }else if (contactType == 'github'){
                    window.open("https://github.com/cdc-x" ,"_blank")
                }
            },

            // 关闭社交平台二维码
            closeContact(){
                this.isShowContact = false
                this.contactTite = ''
                this.contactImg = ''
            },
        },
    }
</script>

<style scoped src="@/assets/css/home-style.css">

</style>