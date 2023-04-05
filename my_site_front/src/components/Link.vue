<template>
    <div class="box-all">
        <div style="padding: 0 10px;">
            <div class="about-banner">
                <div class="about-title">
                    <h1>友情链接</h1>
                    <p>有朋自远方来，不亦乐乎</p>
                </div>
            </div>
        </div>
        
        
        <div style="padding: 0 10px">
            <div class="link-desc">
                <div>
                    <h3 class="desc-title">友情链接申请说明</h3>
                </div>
                <div class="desc-require">
                    <span style="margin-right: 5px"><i class="el-icon-error" style="color: red;"></i> 经常宕机</span>
                    <span style="margin-right: 5px"><i class="el-icon-error" style="color: red;"></i> 不合法规</span>
                    <span style="margin-right: 5px"><i class="el-icon-error" style="color: red;"></i> 擦边球站</span>
                    <span style="margin-right: 5px"><i class="el-icon-error" style="color: red;"></i> 红标报毒</span>
                    <span style="margin-right: 5px"><i class="el-icon-success" style="color: #0bbd87;"></i> 原创优先</span>
                    <span style="margin-right: 5px"><i class="el-icon-success" style="color: #0bbd87;"></i> 技术优先</span>
                </div>
                <div class="desc-content">
                    <p>如需交换友链，可通过以下方式联系本人</p>
                    <p>微信号：CDC1275500642</p>
                    <p>QQ号：1275500642</p>
                    <p>邮箱：CDC1275500642@qq.com</p>
                </div>
            </div>
        </div>
        

        <ul class="link-list">
            <li>
                <div class="pd-lr-10">
                    <a href="https://www.cnblogs.com/cdc1216/" target="_blank">
                        <img src="/static/img/links/cdc_bky.png">
                        <h3>cdcx</h3>
                        <p>cdcx的博客园</p>
                    </a>
                </div>
            </li>
            <li>
                <div class="pd-lr-10">
                    <a href="https://blog.csdn.net/cdc_tr" target="_blank">
                        <img src="/static/img/links/cdc_csdn.png">
                        <h3>cdc-x</h3>
                        <p>cdc-x的CSDN</p>
                    </a>
                </div>
            </li>  
            <li>
                <div class="pd-lr-10">
                    <a href="https://www.jianshu.com/u/cbf200981ecd" target="_blank">
                        <img src="/static/img/links/cdc_js.png">
                        <h3>cdc_x</h3>
                        <p>cdc_x的简书</p>
                    </a>
                </div>
            </li>
            <li>
                <div class="pd-lr-10">
                    <a href="https://www.zhihu.com/people/cdc1216/" target="_blank">
                        <img src="/static/img/links/cdc_zh.png">
                        <h3>cdc1216</h3>
                        <p>cdc1216的知乎</p>
                    </a>
                </div>
            </li>  
            <li>
                <div class="pd-lr-10">
                    <a href="https://www.cnblogs.com/tongh/" target="_blank">
                        <img src="/static/img/links/huitong_bky.png">
                        <h3>Hui_Tong</h3>
                        <p>Hui_Tong的博客园</p>
                    </a>
                </div>
            </li>  
        </ul>  
    </div>    
</template>

<script>
    export default {
        
    }
</script>

<style scoped>
    h1 {
        font-weight: 400;
        margin: 0;
    }
    
    a:hover {
        cursor: pointer;
    }

    a {
        color: black;
    }

    a, img {
        text-decoration: none;
        border: none;
    }

    .box-all {
        height: 100%;
        width: 100%;
    }

    .about-banner {
        background-image: -webkit-gradient(linear,left top,left bottom,color-stop(0,#3b87a5),color-stop(1,#1c1f22));
        margin-top: 20px;
        width: 100%;
        height: 260px;
        overflow: hidden;
    }

    .about-banner .about-title {
        position: relative;
        z-index: 9;
        padding-top: 70px;
        color: #fff;
        text-align: center;
    }

    .about-banner .about-title h1 {
        font-size: 2.5rem;
    }

    .link-desc {
        height: 260px;
        background-color: #fff;
        margin-top: 20px;
        margin-bottom: 20px;
        padding: 20px;
    }

    .desc-title {
        line-height: 30px;
        height: 30px;
        font-weight: bold;
        padding-left: 10px;
        border-left: 5px solid #0bbd87;
    }

    .desc-require {
        margin: 30px 0;
        padding-left: 5px;
    }

    .desc-content {
        font-size: 14px;
        padding-left: 5px;
    }

    .desc-content p {
        margin: 0;
        margin-top: 5px;
    }

    .link-list {
        padding: 0;
    }

    .link-list li {
        float: left;
        width: 25%;
    }

    li {
        list-style: none;
    }

    .link-list .pd-lr-10 {
       padding: 0 10px 20px;
    }

    .link-list li a {
        display: block;
        padding: 20px;
        background: #fff;
        transition: all .3s ease-in-out;
    }

    .link-list li h3 {
        overflow: hidden;
        padding: 10px 15px 9px;
        height: 21px;
        margin: 0;
        font-weight: 400;
    }

    .link-list li img {
        float: left;
        width: 40px;
        height: 40px;
        border-radius: 100%;
    }

    .link-list li a:hover:hover {
        box-shadow: 2px 5px 14px #c5c5c5;
        -webkit-transform: translate3d(0,-3px,0);
        transform: translate3d(0,-2px,0);
    }

</style>