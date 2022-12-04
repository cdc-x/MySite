<template>
    <div class="content">
        <el-row>
            <el-col :span="12" class="dash-head">
                <div style="line-height: 60px; margin-left: 16px; margin-bottom: 16px; font-size: 24px; font-weight: bold;">后台数据统计</div>
            </el-col>
        </el-row>

        <!-- 顶部卡片信息 -->
        <div style="margin-bottom: 24px; display: flex; justify-content: space-between;">
            <div>
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
            </div>

            <div>
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
            </div>

            <div>
                <el-card class="box-card" style="background-color: #1CAF9A; width: 300px">
                    <div style="display: flex; justify-content: space-between;"> 
                        <div>
                            <i class="iconfont icon-yuedu" style="font-size: 64px; color: white"></i>
                        </div>
                        <ul>
                            <li style="color: white; font-size: 24px; font-weight: blod">阅读量</li>
                            <li style="color: white; font-size: 30px; font-weight: blod">{{ readNum }}</li>
                        </ul>
                    </div>
                </el-card>
            </div>

            <div>
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
            </div>
        </div>

        <el-row :gutter="10">
            <el-col :span="12">
                <el-card class="box-card" style="margin-bottom: 16px;">
                    <div id="daliy-browse" style="width: 100%; height: 400px"></div>
                </el-card>
                <el-card class="box-card" style="margin-bottom: 16px;">
                     <div id="daliy-user" style="width: 100%; height: 400px"></div>
                </el-card>
                <el-card class="box-card">
                     <div id="browse" style="width: 100%; height: 400px"></div>
                </el-card>
            </el-col>
            <el-col :span="12">
                <el-card class="box-card" style="margin-bottom: 16px;">
                    <div id="category" style="width: 100%; height: 400px"></div>
                </el-card>
                <el-card class="box-card">
                    <div id="tag" style="width: 100%; height: 400px"></div>
                </el-card>
            </el-col>
        </el-row>
    </div>
</template>

<script>
export default {
    data(){
        return {
            readNum: 0,
            thumbNum: 0,
            articleNum: 0,
            browseNum: 0,
            articleTitleList: [],
            articleBrowseList: [],
            dateList: [],
            dailyBrowseList: [],
            dailyUserList: [],
            categoryList: [],
            tagList: []
       }
    },

    created(){
        this.getDashboardData()
    },


    methods: {
        dailyBrowse(){
            var myChart = this.$echarts.init(document.getElementById('daliy-browse'));

            var option = {
                title: {
                    text: '日访问量',
                    x: 'center'
                },
                dataZoom:[
                    {
                        type: "inside"
                    }
                ],
                xAxis: {
                    type: 'category',
                    data: this.dateList,
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
                    data: this.dailyBrowseList,
                    type: 'line'
                    }
                ],
                tooltip: { 
                        backgroundColor: 'rgba(32, 33, 36,.7)',
                        borderColor: 'rgba(32, 33, 36,0.20)',
                        borderWidth: 1,
                        textStyle: {
                            color: '#fff',
                            fontSize: '12'
                    }
                }
            };
            myChart.setOption(option);

        },

        dailyUser(){
            var myChart = this.$echarts.init(document.getElementById('daliy-user'));

            var option = {
                title: {
                    text: '日用户量',
                    x: 'center'
                },
                dataZoom:[
                    {
                        type: "inside"
                    }
                ],
                xAxis: {
                    type: 'category',
                    data: this.dateList,
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
                    data: this.dailyUserList,
                    type: 'line'
                    }
                ],
                tooltip: { 
                        backgroundColor: 'rgba(32, 33, 36,.7)',
                        borderColor: 'rgba(32, 33, 36,0.20)',
                        borderWidth: 1,
                        textStyle: { 
                            color: '#fff',
                            fontSize: '12'
                    }
                }
            };
            myChart.setOption(option);

        },

        browseCount(){
            var myChart = this.$echarts.init(document.getElementById('browse'));

            var option = {
                title: {
                    text: '文章阅读量排名',
                    x: 'center'
                },
                dataZoom:[
                    {
                        type: "inside"
                    }
                ],
                xAxis: {
                    type: 'category',
                    data: this.articleTitleList,
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
                        type: 'bar',
                        data: this.articleBrowseList
                    }
                ],
                tooltip: { 
                        backgroundColor: 'rgba(32, 33, 36,.7)',
                        borderColor: 'rgba(32, 33, 36,0.20)',
                        borderWidth: 1,
                        textStyle: { 
                            color: '#fff',
                            fontSize: '12'
                    }
                }
            };
            myChart.setOption(option);
        },

        categoryDetail(){
            var myChart = this.$echarts.init(document.getElementById('category'));

            var option = {
                title: {
                    text: '文章分类',
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
                        name: '文章分类详情数据',
                        type: 'pie',
                        radius: '70%',
                        data: this.categoryList,
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

        tagDetail(){
            var myChart = this.$echarts.init(document.getElementById('tag'));

            var option = {
                title: {
                    text: '文章标签',
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
                    name: '文章标签详情数据',
                    type: 'pie',
                    radius: '70%',
                    data: this.tagList,
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

        getDashboardData(){
            this.$http.get("admin/dashboard"). then(response => {
                const res = response.data;
                if (res.status_code === 1000){
                    this.readNum = res.data.read_num
                    this.thumbNum = res.data.thumb_num
                    this.articleNum = res.data.article_num
                    this.articleTitleList = res.data.article_title_list
                    this.articleBrowseList = res.data.article_browse_list
                    this.dateList = res.data.date_list
                    this.dailyBrowseList = res.data.daily_browse_list
                    this.dailyUserList = res.data.daily_user_list
                    this.browseNum = res.data.browse_num
                    this.categoryList = res.data.category_list
                    this.tagList = res.data.tag_list

                    this.dailyBrowse();
                    this.dailyUser();
                    this.browseCount();
                    this.categoryDetail();
                    this.tagDetail();
                }
            })
        },
    },
}
</script>

<style scoped>
    .content {
        width: 90%;
        margin: 0 auto;
    }

    .dash-head {
        display: flex;   
    }

    /deep/ .el-card__header {
        border-bottom: none;
        
    }

</style>