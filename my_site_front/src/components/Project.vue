<template>
    <div class="box-all">
        <div class="useful-tools clearfix">
            <div>
                <h3 class="tools-title">刷刷题(正在开发中)</h3>
            </div>
            <div class="search-area">
                <el-input placeholder="请输入内容" prefix-icon="el-icon-search" v-model="input2"></el-input>
            </div>
            <div>
                <el-collapse v-model="activeName" accordion>
                    <el-collapse-item :title=item.title :name=item.id v-for="item in proList" :key="item.id">
                        <mavon-editor 
                            v-model="item.content"
                            :external-link="externalLink" 
                            :subfield="false"
                            :defaultOpen="'preview'"
                            :editable="false"
                            :toolbarsFlag="false"
                            :scrollStyle="true"
                            :ishljs="true">
                        </mavon-editor>
                    </el-collapse-item>
                </el-collapse>
            </div>
            <div class="pro-page">
                <el-pagination
                    @current-change="handleCurrentChange"
                    :current-page="currentPage"
                    :page-size="100"
                    layout="total, prev, pager, next"
                    :total="400"
                    background>
                </el-pagination>
            </div>
            
        </div>

        <div class="front-tools clearfix">
            <div>
                <h3 class="tools-title">项目合集(正在开发中)</h3>
            </div>
            <ul class="tool-list">
                <li>
                    <div class="pd-lr-10">
                        <a href="https://www.cnblogs.com/cdc1216/" target="_blank">
                            <img src="/static/img/links/cdc_bky.png">
                            <h3>cdcx</h3>
                            <p>cdc的博客园</p>
                        </a>
                    </div>
                </li>
                 <li>
                    <div class="pd-lr-10">
                        <a href="https://www.cnblogs.com/cdc1216/" target="_blank">
                            <img src="/static/img/links/cdc_bky.png">
                            <h3>cdcx</h3>
                            <p>cdc的博客园</p>
                        </a>
                    </div>
                </li>
                 <li>
                    <div class="pd-lr-10">
                        <a href="https://www.cnblogs.com/cdc1216/" target="_blank">
                            <img src="/static/img/links/cdc_bky.png">
                            <h3>cdcx</h3>
                            <p>cdc的博客园</p>
                        </a>
                    </div>
                </li>
                 <li>
                    <div class="pd-lr-10">
                        <a href="https://www.cnblogs.com/cdc1216/" target="_blank">
                            <img src="/static/img/links/cdc_bky.png">
                            <h3>cdcx</h3>
                            <p>cdc的博客园</p>
                        </a>
                    </div>
                </li>
                 <li>
                    <div class="pd-lr-10">
                        <a href="https://www.cnblogs.com/cdc1216/" target="_blank">
                            <img src="/static/img/links/cdc_bky.png">
                            <h3>cdcx</h3>
                            <p>cdc的博客园</p>
                        </a>
                    </div>
                </li>
                 <li>
                    <div class="pd-lr-10">
                        <a href="https://www.cnblogs.com/cdc1216/" target="_blank">
                            <img src="/static/img/links/cdc_bky.png">
                            <h3>cdcx</h3>
                            <p>cdc的博客园</p>
                        </a>
                    </div>
                </li>
            </ul>
        </div>

        <!-- <div class="back-tools clearfix">
            <div>
                <h3 class="tools-title">后端项目</h3>
            </div>
            <ul class="tool-list">
                <li>
                    <div class="pd-lr-10">
                        <a href="https://www.cnblogs.com/cdc1216/" target="_blank">
                            <img src="/static/img/links/cdc_bky.png">
                            <h3>cdcx</h3>
                            <p>cdc的博客园</p>
                        </a>
                    </div>
                </li>
                 <li>
                    <div class="pd-lr-10">
                        <a href="https://www.cnblogs.com/cdc1216/" target="_blank">
                            <img src="/static/img/links/cdc_bky.png">
                            <h3>cdcx</h3>
                            <p>cdc的博客园</p>
                        </a>
                    </div>
                </li>
                 <li>
                    <div class="pd-lr-10">
                        <a href="https://www.cnblogs.com/cdc1216/" target="_blank">
                            <img src="/static/img/links/cdc_bky.png">
                            <h3>cdcx</h3>
                            <p>cdc的博客园</p>
                        </a>
                    </div>
                </li>
                 <li>
                    <div class="pd-lr-10">
                        <a href="https://www.cnblogs.com/cdc1216/" target="_blank">
                            <img src="/static/img/links/cdc_bky.png">
                            <h3>cdcx</h3>
                            <p>cdc的博客园</p>
                        </a>
                    </div>
                </li>
                 <li>
                    <div class="pd-lr-10">
                        <a href="https://www.cnblogs.com/cdc1216/" target="_blank">
                            <img src="/static/img/links/cdc_bky.png">
                            <h3>cdcx</h3>
                            <p>cdc的博客园</p>
                        </a>
                    </div>
                </li>
                 <li>
                    <div class="pd-lr-10">
                        <a href="https://www.cnblogs.com/cdc1216/" target="_blank">
                            <img src="/static/img/links/cdc_bky.png">
                            <h3>cdcx</h3>
                            <p>cdc的博客园</p>
                        </a>
                    </div>
                </li>
            </ul>
        </div>

        <div class="front-back-tools clearfix">
            <div>
                <h3 class="tools-title">前后端交互</h3>
            </div>
            <ul class="tool-list">
                <li>
                    <div class="pd-lr-10">
                        <a href="https://www.cnblogs.com/cdc1216/" target="_blank">
                            <img src="/static/img/links/cdc_bky.png">
                            <h3>cdcx</h3>
                            <p>cdc的博客园</p>
                        </a>
                    </div>
                </li>
                 <li>
                    <div class="pd-lr-10">
                        <a href="https://www.cnblogs.com/cdc1216/" target="_blank">
                            <img src="/static/img/links/cdc_bky.png">
                            <h3>cdcx</h3>
                            <p>cdc的博客园</p>
                        </a>
                    </div>
                </li>
                 <li>
                    <div class="pd-lr-10">
                        <a href="https://www.cnblogs.com/cdc1216/" target="_blank">
                            <img src="/static/img/links/cdc_bky.png">
                            <h3>cdcx</h3>
                            <p>cdc的博客园</p>
                        </a>
                    </div>
                </li>
                 <li>
                    <div class="pd-lr-10">
                        <a href="https://www.cnblogs.com/cdc1216/" target="_blank">
                            <img src="/static/img/links/cdc_bky.png">
                            <h3>cdcx</h3>
                            <p>cdc的博客园</p>
                        </a>
                    </div>
                </li>
                 <li>
                    <div class="pd-lr-10">
                        <a href="https://www.cnblogs.com/cdc1216/" target="_blank">
                            <img src="/static/img/links/cdc_bky.png">
                            <h3>cdcx</h3>
                            <p>cdc的博客园</p>
                        </a>
                    </div>
                </li>
                 <li>
                    <div class="pd-lr-10">
                        <a href="https://www.cnblogs.com/cdc1216/" target="_blank">
                            <img src="/static/img/links/cdc_bky.png">
                            <h3>cdcx</h3>
                            <p>cdc的博客园</p>
                        </a>
                    </div>
                </li>
            </ul>
        </div> -->
    </div>    
</template>

<script>
    export default {
        data(){
            return {
                proList: [
                    {id: 1, title: "No1 猜数字", content: "# Golang 指针\n\n## 一、指针简介\n\n当我们运行一段程序，首先程序会被从硬盘读取到内存中，每块内存都会有一个地址，用来标识数据在内存中存储的位置，而为了保存一个数据在内存中的地址，我们就需要指针变量。\n\n区别于 C/C++ 中的指针，Go 语言中的指针不能进行偏移和运算，是安全指针，因此Go语言中的指针操作非常简单，我们只需要记住两个符号：`&`（取地址）和 `*`（根据地址取值）。\n\n## 二、指针的使用\n\n### 1. 指针地址\n\nGo 语言中使用 `&` 字符放在变量前面对变量进行**取地址**操作：\n\n```go\npackage main\n\nimport \"fmt\"\n\nfunc main() {\n\ta := \"cdc\"\n\tb := &a\n\n\tfmt.Printf(\"变量b的类型：%T\\n\", b)  // 变量b的类型：*string\n\n\t// 使用 %p 接收指针类型的值\n\tfmt.Printf(\"变量b的值：%p\\n\", b)  // 变量b的值：0xc000040240\n\n\t// 变量b的值为变量a的内存地址，可以继续对变量b进行取地址操作\n\tc := &b\n\tfmt.Printf(\"b的内存地址为：%p\\n\", c)  // b的内存地址为：0xc000006028\n\td := &c\n\tfmt.Printf(\"c的内存地址为：%p\\n\", d)  // c的内存地址为：0xc000006038\n}\n```\n\n在内存中，上述几个变量的存储如下：\n\n<img src=\"/static/img/GoLang专题/26.png\" style=\"zoom: 80%;\" /> \n\n### 2. 指针类型\n\n用于接收指针地址的变量对应的数据类型为指针类型，Go语言中的值类型（int、float、bool、string、array、struct）都有对应的指针类型，如：`*int`、`*int64`、`*string` 等。指针类型也可以直接声明使用。\n\n```go\npackage main\n\nimport \"fmt\"\n\nfunc main() {\n\t// 声明一个整型类型的指针\n\tvar ptr1 *int\n\n\t// 声明一个数组类型的指针\n\tvar ptr2 *[3]int\n\n\t// 声明一个值为整型类型的数组\n\tvar ptr3 [3]*int\n\n\tnum := 10\n\tptr1 = &num\n\tfmt.Println(ptr1)  // 0xc00000a0b8\n\n\tarray1 := [3]int{10, 20, 30}\n\tptr2 = &array1\n\tfmt.Println(ptr2)  // &[10 20 30]\n\n\tarray2 := [3]*int{}\n\tfor i := 0; i < 3; i++ {\n\t\tarray2[i] = &i\n\t}\n\tptr3 = array2\n\tfmt.Println(ptr3)  // [0xc00000a0f8 0xc00000a0f8 0xc00000a0f8]\n}\n```\n\n### 3. 通过指针操作值\n\n#### 3.1 取值\n\n在对普通变量使用 `&` 操作符取地址后会获得这个变量的指针，然后可以对指针使用 `*` 操作获取地址对应内存中存储的值。\n\n```go\npackage main\n\nimport \"fmt\"\n\nfunc main() {\n\ta := 10\n\tb := &a\n\tc := &b\n\td := &c\n\n\tfmt.Printf(\"d：%v  %v\\n\", d, *d)  // d：0xc000006030  0xc000006028\n\tfmt.Printf(\"c：%v  %v\\n\", c, *c)  // c：0xc000006028  0xc00000a0b8\n\tfmt.Printf(\"b：%v  %v\\n\", b, *b)  // b：0xc00000a0b8  10\n\n\t// 只要时指针，就可以取值\n\tfmt.Println(***d)  // 10\n    \n    // 也可以通过取值操作对原来的值进行修改\n    *b = 100\n    fmt.Println(a)  // 100\n}\n```\n\n#### 3.2 修改值\n\n函数传值时，尤其是针对值类型的变量，都是先将变量的值拷贝一份，然后传递给函数使用，即在函数中修改变量的值不会影响原来的变量：\n\n```go\npackage main\n\nimport \"fmt\"\n\nfunc changeValue1(num int) int {\n\tnum = 100\n\treturn num\n\n}\n\nfunc main() {\n\tnum := 10\n\tchangeValue1(num)\n\tfmt.Println(num)  // 10\n\n}\n```\n\n如果想要原来的值也随着函数的操作而修改，可以通过指针传值的方式：\n\n```go\npackage main\n\nimport \"fmt\"\n\nfunc changeValue2(num *int) {\n\t*num = 100\n\n}\n\nfunc main() {\n\tnum := 10\n\n\tchangeValue2(&num)\n\tfmt.Println(num)  // 100\n}\n```\n\n使用指针传参的好处，除了可以实现修改原来参数的值的功能，还可以减少传参时的内存消耗，例如：如果一个参数是一个字符串类型的值，且内容比较大，那所有要使用该变量的函数，都要将其拷贝一份，再拿过来使用，因此会占用很大的内存。但是如果只传递该变量的内存地址，则能减小内存不必要的浪费。"},
                    {id: 2, title: "No2 数字迷宫", content: "# Golang 指针\n\n## 一、指针简介\n\n当我们运行一段程序，首先程序会被从硬盘读取到内存中，每块内存都会有一个地址，用来标识数据在内存中存储的位置，而为了保存一个数据在内存中的地址，我们就需要指针变量。\n\n区别于 C/C++ 中的指针，Go 语言中的指针不能进行偏移和运算，是安全指针，因此Go语言中的指针操作非常简单，我们只需要记住两个符号：`&`（取地址）和 `*`（根据地址取值）。\n\n## 二、指针的使用\n\n### 1. 指针地址\n\nGo 语言中使用 `&` 字符放在变量前面对变量进行**取地址**操作：\n\n```go\npackage main\n\nimport \"fmt\"\n\nfunc main() {\n\ta := \"cdc\"\n\tb := &a\n\n\tfmt.Printf(\"变量b的类型：%T\\n\", b)  // 变量b的类型：*string\n\n\t// 使用 %p 接收指针类型的值\n\tfmt.Printf(\"变量b的值：%p\\n\", b)  // 变量b的值：0xc000040240\n\n\t// 变量b的值为变量a的内存地址，可以继续对变量b进行取地址操作\n\tc := &b\n\tfmt.Printf(\"b的内存地址为：%p\\n\", c)  // b的内存地址为：0xc000006028\n\td := &c\n\tfmt.Printf(\"c的内存地址为：%p\\n\", d)  // c的内存地址为：0xc000006038\n}\n```\n\n在内存中，上述几个变量的存储如下：\n\n<img src=\"/static/img/GoLang专题/26.png\" style=\"zoom: 80%;\" /> \n\n### 2. 指针类型\n\n用于接收指针地址的变量对应的数据类型为指针类型，Go语言中的值类型（int、float、bool、string、array、struct）都有对应的指针类型，如：`*int`、`*int64`、`*string` 等。指针类型也可以直接声明使用。\n\n```go\npackage main\n\nimport \"fmt\"\n\nfunc main() {\n\t// 声明一个整型类型的指针\n\tvar ptr1 *int\n\n\t// 声明一个数组类型的指针\n\tvar ptr2 *[3]int\n\n\t// 声明一个值为整型类型的数组\n\tvar ptr3 [3]*int\n\n\tnum := 10\n\tptr1 = &num\n\tfmt.Println(ptr1)  // 0xc00000a0b8\n\n\tarray1 := [3]int{10, 20, 30}\n\tptr2 = &array1\n\tfmt.Println(ptr2)  // &[10 20 30]\n\n\tarray2 := [3]*int{}\n\tfor i := 0; i < 3; i++ {\n\t\tarray2[i] = &i\n\t}\n\tptr3 = array2\n\tfmt.Println(ptr3)  // [0xc00000a0f8 0xc00000a0f8 0xc00000a0f8]\n}\n```\n\n### 3. 通过指针操作值\n\n#### 3.1 取值\n\n在对普通变量使用 `&` 操作符取地址后会获得这个变量的指针，然后可以对指针使用 `*` 操作获取地址对应内存中存储的值。\n\n```go\npackage main\n\nimport \"fmt\"\n\nfunc main() {\n\ta := 10\n\tb := &a\n\tc := &b\n\td := &c\n\n\tfmt.Printf(\"d：%v  %v\\n\", d, *d)  // d：0xc000006030  0xc000006028\n\tfmt.Printf(\"c：%v  %v\\n\", c, *c)  // c：0xc000006028  0xc00000a0b8\n\tfmt.Printf(\"b：%v  %v\\n\", b, *b)  // b：0xc00000a0b8  10\n\n\t// 只要时指针，就可以取值\n\tfmt.Println(***d)  // 10\n    \n    // 也可以通过取值操作对原来的值进行修改\n    *b = 100\n    fmt.Println(a)  // 100\n}\n```\n\n#### 3.2 修改值\n\n函数传值时，尤其是针对值类型的变量，都是先将变量的值拷贝一份，然后传递给函数使用，即在函数中修改变量的值不会影响原来的变量：\n\n```go\npackage main\n\nimport \"fmt\"\n\nfunc changeValue1(num int) int {\n\tnum = 100\n\treturn num\n\n}\n\nfunc main() {\n\tnum := 10\n\tchangeValue1(num)\n\tfmt.Println(num)  // 10\n\n}\n```\n\n如果想要原来的值也随着函数的操作而修改，可以通过指针传值的方式：\n\n```go\npackage main\n\nimport \"fmt\"\n\nfunc changeValue2(num *int) {\n\t*num = 100\n\n}\n\nfunc main() {\n\tnum := 10\n\n\tchangeValue2(&num)\n\tfmt.Println(num)  // 100\n}\n```\n\n使用指针传参的好处，除了可以实现修改原来参数的值的功能，还可以减少传参时的内存消耗，例如：如果一个参数是一个字符串类型的值，且内容比较大，那所有要使用该变量的函数，都要将其拷贝一份，再拿过来使用，因此会占用很大的内存。但是如果只传递该变量的内存地址，则能减小内存不必要的浪费。"},
                ],
                currentPage: 1
            }
        },

        methods: {
            handleCurrentChange(val) {
                console.log(`当前页: ${val}`);
            }
        }
        
    }
</script>

<style scoped>

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

    .clearfix::after {
        content: "";
        display: block;
        clear: both;
    }

    .box-all {
        height: 100%;
        width: 100%;
        background-color: #F1F1F1;
        margin-top: 20px;
        padding: 20px;
    }

    .tools-title {
        line-height: 30px;
        height: 30px;
        font-weight: bold;
        padding-left: 10px;
    }

    .useful-tools .tools-title {
        border-left: 5px solid #0bbd87;
    }

    .front-tools .tools-title {
        border-left: 5px solid #06a2c9;
    }

    .back-tools .tools-title {
        border-left: 5px solid #d25744;
    }

    .front-back-tools .tools-title {
        border-left: 5px solid #b952c5;
    }

    .tool-list {
        padding: 0;
    }

    .tool-list li {
        float: left;
        width: 25%;
    }

    li {
        list-style: none;
    }


    .tool-list li a {
        display: block;
        padding: 20px;
        background: #fff;
        transition: all .3s ease-in-out;
    }

    .tool-list li h3 {
        overflow: hidden;
        padding: 10px 15px 9px;
        height: 21px;
        margin: 0;
        font-weight: 400;
    }

    .tool-list li img {
        float: left;
        width: 40px;
        height: 40px;
        border-radius: 100%;
    }

    .tool-list li a:hover {
        box-shadow: 2px 5px 14px #c5c5c5;
        -webkit-transform: translate3d(0,-3px,0);
        transform: translate3d(0,-2px,0);
    }

    .tool-list .pd-lr-10 {
       padding: 0 10px 20px;
    }

    .pro-page {
        margin-top: 5px;
        display: flex;
        justify-content: end;
    }

    .search-area {
        display: flex;
        justify-content: end;
        margin-bottom: 5px;
    }

    /deep/ .search-area .el-input__inner {
        width: 250px;
    }

    /deep/ .el-collapse-item__header {
        padding: 10px;
        font-weight: bold;
        font-size: 14px;
    }

    /deep/ .el-collapse-item__content {
        padding: 10px;
        font-size: 14px;
    }

    /deep/ pre {
        border-radius: 3px;
        padding: 5px !important;
    
    }

    /deep/ .markdown-body .hljs {
        padding: 5px;
    }

</style>