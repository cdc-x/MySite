<template>
    <div class="box-all">
        <div id="menu" class="hover_animation" :class="{menu_open: menuStatus === false, menu_close: menuStatus === true}"  @click="openMenu()">
            <span></span>
            <span></span>
            <span></span>
        </div>

        <div id="navgation" class="navgation" :class="{navgation_close: menuStatus === false, navgation_open: menuStatus === true}">
            <ul class="point">
                <li @click="enterHome('/blog')">
                    <a>博客</a>
                </li>
                <li @click="enterHome('/project')">
                    <a>项目</a>
                </li>
                <li @click="enterHome('/archive')">
                    <a>归档</a>
                </li>
                <li @click="enterHome('/link')">
                    <a>友链</a>
                </li>
            </ul>
            <div class="logo">
                <a href="/">Mr.Chen</a>
            </div>
        </div>

        <div class="section" id="section1">
            <div class="fp-tablecell">
                <div class="page1">
                    <div class="nav wow zoomIn animated" data-wow-duration="2s" style="visibility: visible; animation-duration: 2s; animation-name: zoomIn;">
                        <h1>CDC-Blog</h1>
                        <p>学而不思则罔，思而不学则殆</p>
                        <el-button type="primary" style="margin-top: 20px" @click="enterHome('/blog')">Enter Blog</el-button>
                    </div>
                    <a class="next wow fadeInUp animated" data-wow-duration="2s" id="next" style="visibility: visible; animation-duration: 2s; animation-name: fadeInUp;" @click="moveToPage2()"></a>
                </div>
            </div>
        </div>

        <div class="section" id="section2">
            <div class="fp-tablecell">
                <div class="page2">
                    <div class="new-article">
                        <div class="inner wow fadeInDown animated" data-wow-delay=".2s" style="visibility: visible; animation-delay: 0.2s; animation-name: fadeInDown;">
                            <h1>推荐阅读</h1>
                            <p>
                                只要朝着一个方向努力
                                <br>
                                一切都会变的得心应手
                            </p>
                        </div>
                        <el-row style="width: 60%; margin: 0 auto">
                            <el-col :span="8" class="wow fadeInUp animated" style="padding: 0px 10px; visibility: visible; animation-name: fadeInUp;">
                                <div class="single-news">
                                    <div class="news-head">
                                        <img src="/static/img/index/python.jpeg">
                                    </div>
                                    <div class="news-content" style="text-align: left;">
                                        <div>Python专栏</div>
                                        <div class="date">2022年10月11日</div>
                                        <p>本专栏主要分享python相关知识，包括python基础，面向对象、并发等进阶内容，相关框架，由浅入深整理Python学习中的每一个阶段和知识点</p>
                                        <a class="btn" @click="enterHome('/blog', 'Python学习路线')">阅读更多</a>
                                    </div>
                                </div>
                            </el-col>
                            <el-col :span="8" class="wow fadeInUp animated" data-wow-delay=".2s" style="padding: 0px 10px; visibility: visible; animation-delay: 0.2s; animation-name: fadeInUp;">
                                <div class="single-news">
                                    <div class="news-head">
                                        <img src="/static/img/index/web.jpg">
                                    </div>
                                    <div class="news-content" style="text-align: left;">
                                        <div>web前端专栏</div>
                                        <div class="date">2022年10月11日</div>
                                        <p>本专栏主要介绍了前端开发相关的内容，包含HTML、CSS、JavaScript入门知识，还介绍了前端框架Vue的基本使用方法</p>
                                        <a class="btn" @click="enterHome('/blog', '前端开发')">阅读更多</a>
                                    </div>
                                </div>
                            </el-col>
                            <el-col :span="8" class="wow fadeInUp animated" data-wow-delay=".4s" style="padding: 0px 10px; visibility: visible; animation-delay: 0.4s; animation-name: fadeInUp;">
                                <div class="single-news">
                                    <div class="news-head">
                                        <img src="/static/img/index/go.jpeg">
                                    </div>
                                    <div class="news-content" style="text-align: left;">
                                        <div>golang专栏</div>
                                        <div class="date">2022年10月11日</div>
                                        <p>本专栏主要记录go语言自学过程中整理的相关知识点，包含golang基础知识，gin框架等内容</p>
                                        <a class="btn" @click="enterHome('/blog', 'Go学习路线')">阅读更多</a>
                                    </div>
                                </div>
                            </el-col>
                        </el-row>
                    </div>
                </div>
            </div>
        </div>

        <div class="section" id="section3">
            <div class="fp-tablecell">
                <div class="page3">
                    <div class="warp-box">
                        <div class="warp">
                            <div class="inner">
                                <div class="links">
                                    <ul>
                                        <li class="wow fadeInLeft animated" style="visibility: visible; animation-name: fadeInLeft;" @click="enterHome('/about/site')">
                                            <a>关于本站</a>
                                        </li>
                                        <li class="wow fadeInRight animated" style="visibility: visible; animation-name: fadeInRight;" @click="enterHome('/link')">
                                            <a>+友情链接</a>
                                        </li>
                                    </ul>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>

        <div class="section" id="section4">
            <div class="fp-tablecell">
                <div class="page4">
                    <div class="warp-box">
                        <div class="about">
                            <div class="inner">
                                <h1 class="wow fadeInLeft animated" style="visibility: visible; animation-name: fadeInLeft;">Chendacheng 个人博客</h1>
                                <p class="wow fadeInRight animated" style="visibility: visible; animation-name: fadeInRight;">
                                    少一些功利主义的追求，多一些不为什么的坚持
                                </p>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>

        <footer class="footer wow fadeInUp animated" id="contact" style="visibility: visible; animation-name: fadeInUp;">
            <div class="footer-top">
                <div class="container">
                    <el-row>
                        <el-col :span="8">
                            <div class="single-widget about">
                                <div class="footer-logo">
                                    <h2>CDC个人博客</h2>
                                </div>
                                <p>万事开头难，然后中间难，然后一直难……</p>
                                <el-button type="primary" @click="enterHome('/learn/more')">Learn More</el-button>
                            </div>
                        </el-col>
                        <el-col :span="8">
                            <div class="single-widget">
                                <h2>相关链接</h2>
                                <ul class="social-icon">
                                    <li @click="enterHome('/blog')">
                                        <a>
                                            <i class="iconfont icon-book"></i>
                                            博文
                                        </a>
                                    </li>
                                    <li @click="enterHome('/project')">
                                        <a>
                                            <i class="iconfont icon-xiangmu2"></i>
                                            项目
                                        </a>
                                    </li>
                                    <li @click="enterHome('/archive')">
                                        <a>
                                            <i class="iconfont icon-danganguanli-danganyijiao"></i>
                                            归档
                                        </a>
                                    </li>
                                    <li @click="enterHome('/link')">
                                        <a>
                                            <i class="iconfont icon-lianjie"></i>
                                            友链
                                        </a>
                                    </li>
                                </ul>
                            </div>
                        </el-col>
                        <el-col :span="8">
                            <div class="single-widget contact">
                                <h2>联系我</h2>
                                <ul class="list">
                                    <li>
                                        <i class="iconfont icon-weixin"></i>
                                        微信号：CDC1275500642
                                    </li>
                                    <li>
                                        <i class="iconfont icon-QQ"></i>
                                        QQ号：1275500642
                                    </li>
                                    <li>
                                        <i class="iconfont icon-youxiang"></i>
                                        邮箱：CDC1275500642@qq.com
                                    </li>
                                </ul>
                            </div>
                        </el-col>
                    </el-row>
                </div>
            </div>
            <div class="copyright">
                <div class="container">
                    <el-row>
                        <el-col :span="24" class="text-center">
                            <p>Copyright © 2022-2099 CDC-博客 All Rights Reserved V.3.1.3 Power by CDC-博客</p>
                        </el-col>
                    </el-row>
                </div>
            </div>
        </footer>
    </div>
    
</template>

<script>
    import $ from 'jquery'
    export default {
        mounted() {
            new this.$wow.WOW().init()
        },

        data(){
            return {
                menuStatus: false,
            }
        },

        methods: {
            moveToPage2(){
                $('html,body').animate({
                    scrollTop: $('#section1').outerHeight() + 1
                }, 600);
            },

            openMenu(){
                this.menuStatus = !this.menuStatus
            },

            enterHome(path, cate){
                this.$store.commit('changeActiveIndex', path)
                if (cate){
                    this.$store.commit('changeArticleCategory', cate)
                }

                this.$router.push("/home")
            },
        },
    }
</script>

<style scoped src="@/assets/css/index-style.css">

</style>
