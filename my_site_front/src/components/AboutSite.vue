<template>
    <div class="box-all">
        <div>
            <div>
                <h2 style="text-align: center;">关于本站</h2>
            </div>
        <div class="site-desc" style="margin-bottom: 35px;">
            <div>
                <h3 class="desc-title">站点说明</h3>
            </div>
            <div class="desc-content">
                <p>本站主要用于记录和整理本人在学习相关技术过程中的笔记和总结，分享出来和大家一起学习研究。站点内文章可随意转载，但请勿商用，转载文章请注明出处。若发现文章中有歧义或者错误的地方，欢迎联系本人进行修正，联系方式见底部页脚处。</p>
            </div>
        </div>
        <div class="site-count">
            <div>
                <h3 class="count-title">站点统计</h3>
            </div>
            <div class="count-content">
                <el-row :gutter="20" style="margin-bottom: 35px;">
                    <el-col :span="6">                     
                        <el-card class="box-card" style="background-color: #17A2B8; width: 300px">
                            <div style="display: flex; justify-content: space-between;"> 
                                <div>
                                    <i class="iconfont icon-wangluo" style="font-size: 64px; color: white"></i>
                                </div>
                                <ul>
                                    <li style="color: white; font-size: 24px; font-weight: blod">访问量</li>
                                    <li style="color: white; font-size: 30px; font-weight: blod">{{ browseNum }}</li>
                                </ul>
                            </div>
                        </el-card>
                    </el-col>
                    <el-col :span="6">
                        <el-card class="box-card" style="background-color: #6F42C1; width: 300px">
                            <div style="display: flex; justify-content: space-between;"> 
                                <div>
                                    <i class="iconfont icon-bianjiwenzhang_huaban" style="font-size: 64px; color: white"></i>
                                </div>
                                <ul>
                                    <li style="color: white; font-size: 24px; font-weight: blod">文章数</li>
                                    <li style="color: white; font-size: 30px; font-weight: blod">{{ articleNum }}</li>
                                </ul>
                            </div>
                        </el-card>
                    </el-col>
                    <el-col :span="6">
                        <el-card class="box-card" style="background-color: #1CAF9A; width: 300px">
                            <div style="display: flex; justify-content: space-between;"> 
                                <div>
                                    <i class="iconfont icon-yanjing" style="font-size: 64px; color: white"></i>
                                </div>
                                <ul>
                                    <li style="color: white; font-size: 24px; font-weight: blod">阅读量</li>
                                    <li style="color: white; font-size: 30px; font-weight: blod">{{ readNum }}</li>
                                </ul>
                            </div>
                        </el-card>
                    </el-col>
                    <el-col :span="6">
                        <el-card class="box-card" style="background-color: #0866C6; width: 300px">
                            <div style="display: flex; justify-content: space-between;"> 
                                <div>
                                    <i class="iconfont icon-dianzan" style="font-size: 64px; color: white"></i>
                                </div>
                                <ul>
                                    <li style="color: white; font-size: 24px; font-weight: blod">点赞数</li>
                                    <li style="color: white; font-size: 30px; font-weight: blod">{{ thumbNum }}</li>
                                </ul>
                            </div>
                        </el-card>
                    </el-col>
                </el-row>
                <el-row>
                    <el-col :span="12">
                        <div id="publish" style="width: 100%; height: 400px"></div>
                    </el-col>
                    <el-col :span="12">
                        <div id="category" style="width: 100%; height: 400px"></div>
                    </el-col>
                </el-row>
            </div>
        </div>
        <div class="site-version">
            <div>
                <h3 class="version-title">版本迭代</h3>
            </div>
            <div class="version-content">
                <div style="margin-bottom: 40px">
                    <div class="item-title">Ver 1.0</div>
                    <div class="item-content">
                        <p>技术栈：Django + SQLite + JQuery + BootStrap</p>
                        <p>架构方式：前后端不分离</p>
                        <p>优点：前端直接通过 Django 模板渲染方式渲染数据，速度快</p>
                        <p>缺点：每篇博客要单独生成一个静态资源文件，数据库操作直接使用 Django admin，部分操作不方便</p>
                        <p>博客界面展示：</p>
                        <div class="site-show">
                            <img src="/static/img/archive/v_1_1.png" style="width: 49%">
                            <img src="/static/img/archive/v_1_2.png" style= "width: 49%">
                        </div>
                    </div>
                </div>
                
                <div style="margin-bottom: 40px">
                    <div class="item-title">Ver 2.0</div>
                    <div class="item-content">
                        <p>技术栈：Django + MySql + Vue + ElementUI</p>
                        <p>架构方式：前后端分离</p>
                        <p>优点：前端后端分离，工程解耦，前端样式可多样化；有专门的管理后台，可实时在线修改</p>
                        <p>缺点：前端组件嵌套太复杂，服务器带宽较小，访问首页响应时间太长</p>
                        <p>博客界面展示：</p>
                        <div class="site-show">
                            <img src="/static/img/archive/v_2_1.png" style="width: 49%">
                            <img src="/static/img/archive/v_2_2.png" style= "width: 49%">
                        </div>
                    </div>
                </div>
                
                <div style="margin-bottom: 40px">
                    <div class="item-title">Ver 3.0</div>
                    <div class="item-content">
                        <p>技术栈：Django + MySql + Vue + ElementUI</p>
                        <p>架构方式：前后端分离</p>
                        <p>优点：在版本2的基础上拆分了组件，整体UI风格设置动态效果，优化压缩打包方式，提高前端加载速度</p>
                        <p>博客界面展示：</p>
                        <div class="site-show">
                            <img src="/static/img/archive/v_3_1.png" style="width: 50%">
                        </div>
                    </div>
                </div>
            </div>
        </div>
        </div>
    </div>
</template>

<script>
    export default {
        created(){
            this.getDashboardDate()
        },

        data(){
            return {
                browseNum: 0,
                readNum: 0,
                thumbNum: 0,
                articleNum: 0,
                publishDateList: [],
                publishNumList: [],
                articleCategory: [],
            }
        },

        methods: {
            publishDetail(){
                var myChart = this.$echarts.init(document.getElementById('publish'));

                var option = {
                    title: [
                        {
                            left: 'center',
                            text: '博客发布'
                        }
                    ],

                    tooltip: {
                        trigger: 'axis'
                    },

                    dataZoom:[
                        {
                            type: "inside"
                        }
                    ],

                    xAxis: {
                        type: 'category',
                        data: this.publishDateList,
                        axisLabel: {
                            interval: 0,
                            rotate: -45,
                        }
                    },
                    
                    yAxis: {
                        type: 'value'
                    },
                    series: [
                        {   
                            type: 'line',
                            data: this.publishNumList,
                        }
                    ]
                };

                myChart.setOption(option);
            },

            categoryDetail(){
                var myChart = this.$echarts.init(document.getElementById('category'));

                var option = {
                    title: {
                        text: '博客分类',
                        left: 'center'
                    },

                    tooltip: {
                        trigger: 'item'
                    },

                    legend: {
                        orient: 'vertical',
                        left: 'left'
                    },

                    series: [
                        {
                            name: '博客分类详情',
                            type: 'pie',
                            radius: '70%',
                            data: this.articleCategory,
                            emphasis: {
                                itemStyle: {
                                    shadowBlur: 10,
                                    shadowOffsetX: 0,
                                    shadowColor: 'rgba(0, 0, 0, 0.5)'
                                }
                            }
                        }
                    ]
                };
                myChart.setOption(option);
            },

            getDashboardDate(){

                this.$http.get("q/about_site").then(response => {
                    const res = response.data;
                    if (res.status_code === 1000){
                        this.readNum = res.data.read_num
                        this.thumbNum = res.data.thumb_num
                        this.articleNum = res.data.article_num
                        this.browseNum = res.data.browse_num
                        this.publishDateList = res.data.publish_date_list
                        this.publishNumList = res.data.publish_num_list
                        this.articleCategory = res.data.category_list

                        this.publishDetail();
                        this.categoryDetail();
                    }
                })
            },
        }
    }
</script>

<style scoped>

    .box-all {
        height: 100%;
        width: 100%;
        background-color: #fff;
        margin-top: 20px;
        padding: 20px;
    }

    ul, li {
        padding: 0;
        margin: 0;
        list-style: none;
    }

    .count-title, .version-title, .desc-title {
        border-bottom: 1px solid rgba(0, 0, 0, .2);
        padding-bottom: 10px;
    }

    /deep/.count-content .el-card__body {
        padding: 20px 40px;
    }

    .version-content .item-title {
        line-height: 30px;
        height: 30px;
        font-weight: bold;
        padding-left: 10px;
        border-left: 5px solid #0bbd87;
    }

    .item-content {
        padding-left: 10px;
    }

    .item-content p {
        font-size: 14px;
    }

    .desc-content {
        font-size: 14px;
        width: 90%;
    }

    .site-show {
        display: flex;
        justify-content: space-between;
    }

</style>