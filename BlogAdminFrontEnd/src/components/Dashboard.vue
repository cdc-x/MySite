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
                            <li style="color: white; font-size: 30px; font-weight: blod">50, 000</li>
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
                            <li style="color: white; font-size: 30px; font-weight: blod">50, 000</li>
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
                            <li style="color: white; font-size: 30px; font-weight: blod">50, 000</li>
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
                            <li style="color: white; font-size: 30px; font-weight: blod">50, 000</li>
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
                     <div id="thumb" style="width: 100%; height: 400px"></div>
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
          
       }
   },

   mounted(){
        this.dailyBrowse();
        this.dailyUser();
        this.thumbCount();
        this.categoryDetail();
        this.tagDetail();
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
                    data: ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun', 'Sun', 'Sun', 'Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun', 'Sun', 'Sun', 'Sun']
                },
                yAxis: {
                    type: 'value'
                },
                series: [
                    {
                    data: [150, 230, 224, 218, 135, 147, 260, 260, 260, 260, 150, 230, 224, 218, 135, 147, 260, 260, 260, 260],
                    type: 'line'
                    }
                ],
                tooltip: { 
                        backgroundColor: 'rgba(32, 33, 36,.7)',
                        borderColor: 'rgba(32, 33, 36,0.20)',
                        borderWidth: 1,
                        textStyle: { // 文字提示样式
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
                    data: ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun', 'Sun', 'Sun', 'Sun']
                },
                yAxis: {
                    type: 'value'
                },
                series: [
                    {
                    data: [150, 230, 224, 218, 135, 147, 260, 260, 260, 260],
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

        thumbCount(){
            var myChart = this.$echarts.init(document.getElementById('thumb'));

            var option = {
                title: {
                    text: '点赞数排名',
                    x: 'center'
                },
                dataZoom:[
                    {
                        type: "inside"
                    }
                ],
                xAxis: {
                    type: 'category',
                    data: ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun', 'Sun', 'Sun', 'Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun', 'Sun', 'Sun', 'Sun']
                },
                yAxis: {
                    type: 'value'
                },
                series: [
                    {
                        data: [150, 230, 224, 218, 135, 147, 260, 260, 260, 260, 150, 230, 224, 218, 135, 147, 260, 260, 260, 260],
                        type: 'bar'
                    }
                ],
                tooltip: { 
                        backgroundColor: 'rgba(32, 33, 36,.7)',
                        borderColor: 'rgba(32, 33, 36,0.20)',
                        borderWidth: 1,
                        textStyle: { // 文字提示样式
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
                    subtext: 'Fake Data',
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
                    name: 'Access From',
                    type: 'pie',
                    radius: '70%',
                    data: [
                        { value: 1048, name: 'Search Engine' },
                        { value: 735, name: 'Direct' },
                        { value: 580, name: 'Email' },
                        { value: 484, name: 'Union Ads' },
                        { value: 300, name: 'Video Ads' }
                    ],
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
                    subtext: 'Fake Data',
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
                    name: 'Access From',
                    type: 'pie',
                    radius: '70%',
                    data: [
                        { value: 1048, name: 'Search Engine' },
                        { value: 735, name: 'Direct' },
                        { value: 580, name: 'Email' },
                        { value: 484, name: 'Union Ads' },
                        { value: 300, name: 'Video Ads' }
                    ],
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
        }
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