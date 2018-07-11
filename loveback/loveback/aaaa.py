#
# <script>
#    // 顶部二维码
#     $('.new_header-top .wx').hover(function() {
#         $('.new_header-top .new_top-right p').show();
#     }, function() {
#         $('.new_header-top .new_top-right p').hide();
#     });
#
#     //下拉菜单
#     $('.new_nav .new_list').hover(function() {
#         $(this).children('div').show();
#
#     }, function() {
#         $(this).children('div').hide();
#     });
#     $('.header-wxyz').click(function(event) {
#         $('.wechat').show();
#     });
#     $('.wechat .close').click(function(event) {
#         $(".isHzhy").hide();
#         $(".isNotHzhy").hide();
#         $('.now-show').show();
#         $('.wechat').hide();
#
#     });
#
#     $(".f-tap-btn").on("click",function(){
#
#         $.post('/web_wechat_validate' , {'wechat_id':$(".f-input").val(),'_token':"UTwE94sTgaYvOrfbtLsDxGT6AE6iy3Fn3Otk5INz"} , function(json){
#             if(json.status) {
#                 $(".isHzhy").show();
#                 $(".isNotHzhy").hide();
#                 $('.now-show').hide();
#             }
#             else{
#                 $(".isHzhy").hide();
#                 $(".isNotHzhy").show();
#                 $('.now-show').hide();
#             }
#         });
#      });
#
#     $('.new_hy_show').hover(function() {
#        $('.new_user-card').show();
#     }, function() {
#         $('.new_user-card').hide();
#     });
#
# </script>
#
# <style>
#     .popup1 .popup-close.shanchu{
#         right: 33px;
#         top: 43px;
#         width: 45px;
#         height: 38px;
#     }
#     .popup1 .popup-img.add{
#         width: 650px;
#         height: 518px;
#     }
# </style>
#
#
# <!--            					##轮播图-->
#                                 <!--<div class="swiper-slide" style="background-image: url(//huazhen-upload.oss-cn-hangzhou.aliyuncs.com/index-image/201803/09/9kssws65bea7wv9ku3ylb6j6tvanerbb.jpg)">
#                         <a href="/whlq/a"></a>
#                     </div>
#                                 <div class="swiper-slide" style="background-image: url(//huazhen-upload.oss-cn-hangzhou.aliyuncs.com/index-image/201803/09/kdrohouonwxjesugz4snl1h4ufvf98kf.jpg)">
#                         <a href="http://kf7.kuaishang.cn/bs/im.htm?cas=56293___998837&amp;fi=66510&amp;vi=ef8d86d3da574969a9730a41b8b16813&amp;dp=http%3A%2F%2Fwww.huazhen.com%2F&amp;_tk=9db519f7"></a>
#                     </div>
#                                 <div class="swiper-slide" style="background-image: url(//huazhen-upload.oss-cn-hangzhou.aliyuncs.com/index-image/201803/09/jsap3h3oc1ky0omc8ztpp1blkspeessr.jpg)">
#                         <a href="http://www.huazhen.com/article/3589.html"></a>
#                     </div>
#                                 <div class="swiper-slide" style="background-image: url(//huazhen-upload.oss-cn-hangzhou.aliyuncs.com/index-image/201805/25/cdivud1j4fvvpwpxl15wqmz6myhbhsqt.png)">
#                         <a href="/fhns/a"></a>
#                     </div>
#                                 <div class="swiper-slide" style="background-image: url(//huazhen-upload.oss-cn-hangzhou.aliyuncs.com/index-image/201805/19/l2y34hmls9jlrxaviekgmov1umaftg2u.jpg)">
#                         <a href="/hyxf/a/"></a>-->
#                     </div>
#                     </div>
#         <!-- Add Pagination -->
#         <div class="swiper-pagination" id="swiper1-but"></div>
#     </div>
# </div>
#
# <div class="con01">
#     <ul style="text-align:center;">
#         <li>
#             <div>
#                 <div class="font0"><span>9</span>年</div>
#
#                 <div class="font1">爱·回来团队创办于2008年，专注<br>情感 咨询服务9年，经验丰富</div>
#             </div>
#         </li>
#         <li>
#             <div>
#                 <div class="font0"><span>34</span>万</div>
#                 <div class="font1">至今，已超过34万位用户通<br>过爱·回来咨询获得了幸福</div>
#             </div>
#         </li>
#         <!-- <li>
#             <div>
#                 <div class="font0"><span>300</span>位</div>
#                 <div class="font1">近300位咨询师获得国家<br>或行业协会相关资格认证</div>
#             </div>
#         </li> -->
#         <li>
#             <div>
#                 <div class="font0"><span>NO.1</span></div>
#                 <div class="font1">国内情感咨询和规划标杆品牌，<br>2015年/2016年中国最佳创新公司</div>
#             </div>
#         </li>
#         <li>
#             <div>
#                 <div class="font0"><span>500</span>家</div>
#                 <div class="font1">被500多家媒体深度报道，备 <br>受大众的推崇与信赖</div>
#             </div>
#         </li>
#     </ul>
#
# </div>
# <div class="con02">
#     <div class="con02-in">
#         <div class="con02-Top">
#             <div class="tit">
#                 <hr class="tit-hr">
#                 爱·回来项目
#                 <hr class="tit-hr">
#             </div>
#             <div class="tit2">
#                 幸福从这里开始
#             </div>
#         </div>
#         <div class="con02-body">
#             <div class="con02-bodyL">
#                 <a href="http://www.huazhen.com/love3"><img src="http://huazhen-poster.oss-cn-hangzhou.aliyuncs.com/imgfiles/pic_img_aqgj.png" alt=""></a>
#             </div>
#             <div class="con02-bodyR">
#                 <a href="http://www.huazhen.com/hpjht2"><img class="con02-bodyRm" src="http://a3.huazhen.com/huazhen_revision/pc/home/images/tp_02.png" alt=""></a>
#                 <a href="http://www.huazhen.com/zmb/a"><img src="http://a3.huazhen.com/huazhen_revision/pc/home/images/tp_03.png" alt=""></a>
#             </div>
#         </div>
#     </div>
# </div>
# <body class="con03">
#     <div class="con03-in">
#         <div class="con02-Top">
#             <div class="tit">
#                 <hr class="tit-hr">
#                 花粉心声
#                 <hr class="tit-hr">
#             </div>
#             <div class="tit2">
#                 用户分享的心声，还原我们的服务
#             </div>
#         </div>
#
#
#  <div class="con02-con">
#             <div class="tabBar" >
#                 <div class="tabBarCon swiper-container">
#                     <div class="swiper-wrapper">
#                         <div class="swiper-slide con02-left con02-new">
#                             <h3>婚姻修复</h3>
#                             <div class="kh-video qy-video">
#                                 <img src="http://a3.huazhen.com/huazhen_revision/pc/home/images/pcshipin1.jpg" alt="" class="fm show">
#                                  <video id="qiye-video" class="video-js vjs-default-skin" controls="" >
#                                     <source src="http://520qinggan.oss-cn-hangzhou.aliyuncs.com/20171024%20%E8%8A%B1%E9%95%8730%E7%A7%92%E3%80%8A%E5%A9%9A%E5%A7%BB%E4%BF%AE%E5%A4%8D%E7%AF%87%E3%80%8BFinal%EF%BC%8816%EF%BC%9A9%EF%BC%89.mp4" type="video/mp4">
#                                 </video>
#                                 <img src="http://huazhen-poster.oss-cn-hangzhou.aliyuncs.com/huazhen.com/zanting.png" alt="" class="mb">
#                             </div>
#                         </div>
#                         <div class="swiper-slide con02-right">
#                             <h3>恋爱脱单</h3>
#                             <div class="kh-video kehu-video">
#                                 <img src="http://a3.huazhen.com/huazhen_revision/pc/home/images/pctuodan.jpg" alt="" class="fm show">
#                                  <video id="kehu-video" class="video-js vjs-default-skin" controls="" >
#                                     <source src="http://520qinggan.oss-cn-hangzhou.aliyuncs.com/20171024%20%E8%8A%B1%E9%95%8730%E7%A7%92%E3%80%8A%E6%81%8B%E7%88%B1%E8%84%B1%E5%8D%95%E7%AF%87%E3%80%8BFinal%EF%BC%8816%EF%BC%9A9%EF%BC%89.mp4" type="video/mp4">
#
#                                 </video>
#                                 <img src="http://huazhen-poster.oss-cn-hangzhou.aliyuncs.com/huazhen.com/zanting.png" alt="" class="mb">
#                             </div>
#                         </div>
#                         <div class="swiper-slide con02-left con02-new">
#                             <h3>恋情挽回</h3>
#                             <div class="kh-video qy-video">
#                                 <img src="http://a3.huazhen.com/huazhen_revision/pc/home/images/pcwanhuilianq.jpg" alt="" class="fm show">
#                                  <video id="qiye-video" class="video-js vjs-default-skin" controls="" >
#                                     <source src="http://520qinggan.oss-cn-hangzhou.aliyuncs.com/20171024%20%E8%8A%B1%E9%95%8730%E7%A7%92%E3%80%8A%E6%81%8B%E6%83%85%E6%8C%BD%E5%9B%9E%E7%AF%87%E3%80%8BFinal%EF%BC%8816%EF%BC%9A9%EF%BC%89.mp4" type="video/mp4">
#                                 </video>
#                                 <img src="http://huazhen-poster.oss-cn-hangzhou.aliyuncs.com/huazhen.com/zanting.png" alt="" class="mb">
#                             </div>
#                         </div>
#                         <div class="swiper-slide con02-right">
#                             <h3>品牌宣传片</h3>
#                             <div class="kh-video kehu-video">
#                                 <img src="http://a3.huazhen.com/huazhen_revision/pc/home/images/sp01.jpg" alt="" class="fm show">
#                                  <video id="kehu-video" class="video-js vjs-default-skin" controls="" >
#                                     <source src="http://huazhen-poster.oss-cn-hangzhou.aliyuncs.com/huazhen.com/qiye.mp4" type="video/mp4">
#
#                                 </video>
#                                 <img src="http://huazhen-poster.oss-cn-hangzhou.aliyuncs.com/huazhen.com/zanting.png" alt="" class="mb">
#                             </div>
#                         </div>
#                         <div class="swiper-slide con02-left con02-new">
#                             <h3>品牌宣传片</h3>
#                             <div class="kh-video qy-video">
#                                 <img src="http://a3.huazhen.com/huazhen_revision/pc/home/images/sp01.jpg" alt="" class="fm show">
#                                  <video id="qiye-video" class="video-js vjs-default-skin" controls="" >
#                                     <source src="http://huazhen-poster.oss-cn-hangzhou.aliyuncs.com/huazhen.com/qiye.mp4" type="video/mp4">
#                                 </video>
#                                 <img src="http://huazhen-poster.oss-cn-hangzhou.aliyuncs.com/huazhen.com/zanting.png" alt="" class="mb">
#                             </div>
#                         </div>
#                         <div class="swiper-slide con02-right">
#                             <h3>用户心声</h3>
#                             <div class="kh-video kehu-video">
#                                 <img src="http://huazhen-poster.oss-cn-hangzhou.aliyuncs.com/video/sp02.jpg" alt="" class="fm show">
#                                  <video id="kehu-video" class="video-js vjs-default-skin" controls="" >
#                                     <source src="http://huazhen-poster.oss-cn-hangzhou.aliyuncs.com/huazhen.com/kehu.mp4" type="video/mp4">
#
#                                 </video>
#                                 <img src="http://huazhen-poster.oss-cn-hangzhou.aliyuncs.com/huazhen.com/zanting.png" alt="" class="mb">
#                             </div>
#                         </div>
#                     </div>
#                     <div class="tabBarprev swiper-button-prev"></div>
#                     <div class="tabBarnext swiper-button-next"></div>
#                 </div>
#                 <div style="clear: both"></div>
#             </div>
#     </div>
# </div>
# <div class="con04">
#     <div class="con04-in">
#         <div class="con02-Top">
#             <div class="tit">
#                 <hr class="tit-hr">
#                 爱·回来资深情感团队
#                 <hr class="tit-hr">
#             </div>
#             <div class="tit2">
#                 业界资深情感咨询师团队
#             </div>
#         </div>
#         <div class="con04-body">
#             <div class="con04-bodyL">
#                 <img src="http://huazhen-poster.oss-cn-hangzhou.aliyuncs.com/imgfiles/pc_pic_1.jpg" alt="">
#             </div>
#             <div class="con04-bodyR">
#                 <div class="con04-tab">
#                     <a class="con04-tabA1 on" href="javascript:;" target="_self">情感督导师</a>
#                     <a class="con04-tabA2" href="javascript:;" target="_self">情感咨询师</a>
#                 </div>
#                 <div class="con04-con cur">
#                     <!-- Swiper -->
#                     <div class="swiper-container" id="swiper2">
#                         <div class="swiper-wrapper" >
#                             <div class="swiper-slide">
#                                 <a href="/zhuanjia/1.html">
#                                     <img class="daoshi" src="http://a3.huazhen.com/huazhen_revision/pc/home/images/dd02.png" alt="">
#                                     <div class="daoshi-desc">
#                                         <p class="daoshi-descP">冷爱</p>
#                                         <p>爱·回来联合创始人 <br>深度情感维系导师 <br>中国情感学习先驱<br>中国男性情感解读导师<br>理性爱情经营导师</p>
#
#                                     </div>
#                                 </a>
#                             </div>
#                             <div class="swiper-slide">
#                                 <a href="http://www.huazhen.com/tutor/3218.html">
#                                     <img class="daoshi" src="http://huazhen-poster.oss-cn-hangzhou.aliyuncs.com/huazhen.com/zzy.png" alt="">
#                                     <div class="daoshi-desc">
#                                         <p class="daoshi-descP">张政鹰</p>
#                                         <p>爱·回来督导师 <br>国家三级婚姻家庭咨询师<br>临床心理学博士Dr.Albert chan长期督导<br>美国情绪聚焦疗法(EFT)连续培养项目组成员</p>
#                                         <!-- <p class="daoshi-descP">擅长</p>
#                                         <p>恋爱实战绿茶话术，段位技巧、长期关系宝宝吵架术提升感情浓度、情绪聚焦(EFT)  、情感挽回焦点治疗、认知行为疗法(CBT)、叙事疗法(NT)、结构式家庭治疗(SFT)、灵气疗愈重塑自我认知</p> -->
#                                     </div>
#                                 </a>
#                             </div>
#                             <div class="swiper-slide">
#                                 <a href="/zhuanjia/5.html">
#                                     <img class="daoshi" src="http://a3.huazhen.com/huazhen_revision/pc/home/images/dd03.png" alt="">
#                                     <div class="daoshi-desc">
#                                         <p class="daoshi-descP">陈柏宇</p>
#                                         <p>爱·回来情感高级咨询导师 <br>婚姻家庭咨询师 <br>爱·回来形象导师</p>
#                                         <!-- <p class="daoshi-descP">擅长</p>
#                                         <p>魅力提升  情感挽回</p> -->
#                                     </div>
#                                 </a>
#                             </div>
#                             <div class="swiper-slide">
#                                 <a href="/zhuanjia/7.html">
#                                     <img class="daoshi" src="http://a3.huazhen.com/huazhen_revision/pc/home/images/dd04.png" alt="">
#                                     <div class="daoshi-desc">
#                                         <p class="daoshi-descP">彭亮</p>
#                                         <p>爱·回来情感高级咨询导师 <br>三级婚姻家庭咨询师 <br>三级心理咨询师<br>高级催眠师<br>高级私人心理顾问</p>
#
#                                     </div>
#                                 </a>
#                             </div>
#                         </div>
#                         <!-- Add Arrows -->
#                         <div class="swiper-button-prev"></div>
#                         <div class="swiper-button-next"></div>
#                     </div>
#
#                 </div>
#                 <div class="con04-con">
#                     <!-- Swiper -->
#                     <div class="swiper-container" id="swiper3">
#                         <div class="swiper-wrapper" >
#                             <div class="swiper-slide">
#                                 <a href="/tutor/3486.html">
#                                     <img class="daoshi" src="http://a3.huazhen.com/huazhen_revision/pc/home/images/zx01.jpg" alt="">
#                                     <div class="daoshi-desc">
#                                         <p class="daoshi-descP">崔雷</p>
#                                         <p>国家三级婚姻家庭咨询师 <br>爱·回来冷爱弟子班情感督导师 <br>黄埔计划培训讲师</p>
#                                         <p class="daoshi-descP">擅长</p>
#                                         <p>脱单  自我提升</p>
#                                     </div>
#                                 </a>
#                             </div>
#                             <div class="swiper-slide">
#                                 <a href="/tutor/2505.html">
#                                     <img class="daoshi" src="http://a3.huazhen.com/huazhen_revision/pc/home/images/zx02.png" alt="">
#                                     <div class="daoshi-desc">
#                                         <p class="daoshi-descP">哈雷</p>
#                                         <p>国家家庭婚姻三级咨询师 <br>爱·回来督导师 <br>应用心理学学士</p>
#                                         <p class="daoshi-descP">擅长</p>
#                                         <p>挽回  婚姻修复</p>
#                                     </div>
#                                 </a>
#                             </div>
#                             <div class="swiper-slide">
#                                 <a href="/tutor/3418.html">
#                                     <img class="daoshi" src="http://a3.huazhen.com/huazhen_revision/pc/home/images/zx03.png?v=12" alt="">
#                                     <div class="daoshi-desc">
#                                         <p class="daoshi-descP">罗琳</p>
#                                         <p>脱单成长导师 <br>爱·回来线下讲师 <br>爱·回来情感咨询师</p>
#                                         <p class="daoshi-descP">擅长</p>
#                                         <p>两性情感剖析  挽回</p>
#                                     </div>
#                                 </a>
#                             </div>
#                             <div class="swiper-slide">
#                                 <a href="/tutor/3291.html">
#                                     <img class="daoshi" src="http://a3.huazhen.com/huazhen_revision/pc/home/images/zx04.png" alt="">
#                                     <div class="daoshi-desc">
#                                         <p class="daoshi-descP">林莉</p>
#                                         <p>现任爱·回来情感咨询师 <br>国家婚姻家庭咨询师 <br>教育硕士</p>
#                                         <p class="daoshi-descP">擅长</p>
#                                         <p>脱单  长期关系维护</p>
#                                     </div>
#                                 </a>
#                             </div>
#                         </div>
#                         <!-- Add Arrows -->
#                         <div class="swiper-button-prev"></div>
#                         <div class="swiper-button-next"></div>
#                     </div>
#
#                 </div>
#             </div>
#         </div>
#     </div>
# </div>
#
# <div class="con06">
#     <div class="con06-in">
#         <div class="item8-L">
#             <img class="item8-img0" src="http://a3.huazhen.com/huazhen_revision/pc/home/images/img——29.png?v=125" alt="">
#             <img class="item8-img1 " src="http://a3.huazhen.com/huazhen_revision/pc/home/images/img——30.png?v=125" alt="">
#             <img class="item8-img2 " src="http://a3.huazhen.com/huazhen_revision/pc/home/images/img——31.png?v=125" alt="">
#         </div>
#         <div class="item8-R">
#             <p class="item8-Rtop">爱·回来 一个有温度的环境</p>
#             <div class="item8-Rtit">
#                 <p>想要脱单指导、提升魅力、重获爱情、修复婚姻?</p>
#                 <p>快联系爱·回来情感导师,第一时间解决你的情感问题，陪你学会爱！</p>
#             </div>
#             <div>
#                 <div class="download-but">
#
# {#                    <a class="an" style="margin-top: 50px;" href="http://huazhen-upload.oss-cn-hangzhou.aliyuncs.com/software/huazhenqingganhunyinlianqing_11.apk">Android版下载</a>#}
# {#                    <a class="ip" style="display:none;" href="https://itunes.apple.com/us/app/爱·回来/id1265707707?mt=8">iPhone版下载</a>#}
#                 </div>
#                 <div class="ewm">
#                     <img src="http://a3.huazhen.com/huazhenhome/images/tp_11.jpg" alt=""/>
#                     <div>扫一扫联系导师</div>
#                 </div>
#             </div>
#         </div>
#
#     </div>
# </div>
#
# <!-- 弹窗 -->
# <div class="popup1 fadeInUp" style="display: none;background: rgba(0,0,0,0.5)">
#     <div class="popup-img">
#         <img src="/static/img/pctc.jpg" class="kefu_btn" alt="popup">
#         <div class="popup-close" ><img src="http://a3.huazhen.com/huazhen_revision/pc/public/images/gb.png" alt="" class="iconfont icon-close"></div>
#     </div>
# </div>
# <div class="new_foot">
#     <div class="new_foot-in">
#         <ul>
#             <li>
#                 <img src="/static/img/logo.png" alt=""/>
#                 <p>在线咨询：400-0173-511</p>
#                 <p>公司地址：成都 - 高新区 - 天府四街</p>
# {#                <p></p>#}
#             </li>
#             <li class="on">
#                 <div class="new_foot-nav">
#
#                     <div>
#                         <a href="http://www.hen.com/ppzx">爱·回来介绍</a>
#
#                     </div>
#                     <div>
#                         <a href="http://www.en.com/ppzx/hzdz.html">联系我们</a>
#
#                     </div>
#                 </div>
#                 <div class="new_foot-bq">
#                     Copyright© 2008-2017 IHuiLai,lnc.All Rights Reserved.  <br/>
#                     <a href="http://www.miitbeian.gov.cn" target="_blank" style="color: #666"></a>     版权所有：成都爱·回来教育咨询有限公司
#                 </div>
#             </li>
#             <li class="last">
#                 <div class="foot-ewm">
#                     <img style="width:102px" src="微信二维码客服1" alt=""/>
#                     <p>爱·回来</p>
#                 </div>
#                 <div class="foot-ewm">
#                     <img style="width: 102px" src="微信二维码" alt=""/>
#                     <p>爱·回来</p>
#                 </div>
#             </li>
#         </ul>
#     </div>
# </div>
#
# <div class="side_fixed">
#     <ul>
#        <span  >
#           <a target="_blank" href="http://wpa.qq.com/msgrd?v=3&uin=634163114&site=qq&menu=yes"><img border="0" src="http://wpa.qq.com/pa?p=2:634163114:53" alt="点击这里给我发消息" title="点击这里给我发消息" font-size:30px;/></a>
#         <li class="side_qgzx ab">
#         </span>
#             <span>  </span>
#         </li>
#         <li class="kefu_btn ab">
#             <a href="javascript:;" target="_self">售前<br>客服</a>
#             <span></span>
#         </li>
#         <li class="qq_btn ab" style="display: none;">
#             <a href="javascript:;" target="_self">11<br>服务</a>
#             <span></span>
#         </li>
#         <li class="side_ewm">
#             <a href="javascript:;" target="_self">爱·回来<br></a>
#             <span></span>
#             <div class="hz_ewm">
#                 <div class="ewm_in">
#                     <img src="http://a3.huazhen.com/huazhen_revision/pc/home/images/tp_11.jpg" alt="">
#                     <h4>扫一扫，情感问题就没了</h4>
#                 </div>
#                 <p></p>
#             </div>
#         </li>
#         <li class="s_top ab">
#             <a href="javascript:;" target="_self">返回<br>顶部</a>
#             <span></span>
#         </li>
#
#
#
#
#     </ul>
# </div>
#
#     <div class="popup gw-popup">
#           <div class="popup-label">
#               <div class="popup-hind">
#
#               </div>
#               <div class="popup-btn">
#                   朕知道了
#               </div>
#           </div>
#     </div>
#
#
#
#     <script>
#             var channel_code = '490640b43519c77281cb2f8471e61a71';
#             var channel = '竞价-爱·回来-官网';
#
#             if (location.pathname == '/srdz/a'){
#                 channel = '竞价-官网-私人定制'
#                 channel_code = '144a3f71a03ab7c4f46f9656608efdb2';
#             }
#             if (location.pathname == '/love3'){
#                 channel = '竞价-官网-爱情管家'
#                 channel_code = 'b710915795b9e9c02cf10d6d2bdb688c';
#             }
#             if (location.pathname == '/hyxf/shangwu/'){
#                 channel_code = '3c1e4bd67169b8153e0047536c9f541e';
#             }
#
#             var Index = new Submit('.gw-yxd', {
#                 submitSuccess: function (data) {
#                     $('.contact-box').hide();
#
#                 },
#                 submitError: function () {
#                     Index.popupShow('提交失败');
#                 },
#                 channel: channel,
#                 channel_code:channel_code,
#                 dataUrl: "http://www.huazhen2008.com/api/crm/huazhen_guests"
#             });
#
#     </script>
#
# <script>
# // 弹窗关闭
#     function tanku(ite){
#         setTimeout(function(){
#             $('.popup1').show().removeClass("fadeOutDown").addClass('fadeInUp');
#         },ite);
#     }
#     tanku(20000)
#     // $(".popup-close").click(function(){
#     //     $('.popup1').removeClass("fadeInUp").addClass('fadeOutDown');
#     //     setTimeout(function(){
#     //         $('.popup1').hide();
#     //     },500);
#     // })
#     $('.popup-close').click(function(event) {
#         $('.popup1').hide()
#     });
#     $(document).click(function(e){
#       var _con = $('.popup-img');   // 设置目标区域
#       if(!_con.is(e.target) && _con.has(e.target).length === 0){
#            $('.popup-img').hide();
#       }
#     });
#
# </script>
#
# </body>
#
#
# <script>
#     $('.con04-tab a').click(function(event) {
#        $(this).addClass('on').siblings().removeClass('on');
#        var num = $(this).index();
#        $('.con04-con').eq(num).show().siblings('.con04-con').hide();
#        var swiper2 = new Swiper('#swiper2', {
#             pagination: '#swiper2-but',
#             paginationClickable: true,
#             nextButton: '.swiper-button-next',
#             prevButton: '.swiper-button-prev',
#             prevButton: '.swiper-button-prev'
#         });
#         var swiper6 = new Swiper('#swiper3', {
#             paginationClickable: true,
#             nextButton: '.swiper-button-next',
#             prevButton: '.swiper-button-prev'
#         });
#     });
#
#     var qiyeVideo = document.getElementById('qiye-video')
#     var kehuVideo = document.getElementById('kehu-video')
#     var kehuImg = $('.kehu-video .fm')
#     var qiyeImg = $('.qy-video .fm')
#     $('.video-play').click(function(event) {
#         $(this).hide();
#         document.getElementById('home-video').play();
#     });
#     $('.kehu-video img').click(function(event) {
#         $(this).removeClass('show');
#         $(this).siblings('video').get(0).play();
#         // document.getElementById('kehu-video').play();
#         qiyeVideo.pause();
#         $('.qy-video .mb').show();
#         if( qiyeImg.hasClass('show') ){
#             $('.qy-video .mb').hide()
#         }
#
#     });
#     $('.qy-video img').click(function(event) {
#         $(this).removeClass('show');
#         $(this).siblings('video').get(0).play();
#         // document.getElementById('qiye-video').play();
#         kehuVideo.pause();
#         $('.kehu-video .mb').show();
#         if( kehuImg.hasClass('show') ){
#             $('.kehu-video .mb').hide()
#         }
#     });
#
#      $('.kh-video video').click(function(event) {
#          $(this).siblings('.mb').hide();
#
#      });
#      $('#qiye-video').click(function(event) {
#          qiyeVideo.pause()
#      });
#      $('#kehu-video').click(function(event) {
#          kehuVideo.pause()
#      });
#      $('.kh-video .mb').click(function(event) {
#          $(this).hide()
#      });
# </script>
# <script>
#     var mySwiper = new Swiper('.tabBarCon', {
#         slidesPerView : 2,
#         centeredSlides : false,
#         slidesPerGroup : 2,
#         prevButton:'.tabBarprev',
#         nextButton:'.tabBarnext',
#     })
#     //    autoPlay:true,interTime:3000,
#     jQuery(".tabBar").slide({ mainCell:".conWrap", effect:"left", trigger:"mouseover", pnLoop:false });
# </script>
#
#
#  <style>
#         .imgDiv{position: absolute; bottom: 24%;right: 33%;}
#         .imgDiv img{position: absolute;}
#         .ds-no{display: none}
#         .donghua{
#             animation: move 2.5s linear infinite;
#             -moz-animation: move 2.5s linear infinite;
#             -webkit-animation: move 2.5s linear infinite;
#             -o-animation: move 2.5s linear infinite;
#
#             animation-fill-mode:forwards;
#             -moz-animation-fill-mode: forwards;
#             -webkit-animation-fill-mode: forwards;
#             -o-animation-fill-mode: forwards;
#
#             animation-iteration-count:1;
#             -moz-animation-iteration-count:1;
#             -webkit-animation-iteration-count:1;
#             -o-animation-iteration-count:1;
#         }
#         @keyframes  move {
#             from {
#                 display:block;
#                 top:0;
#                 opacity:1;
#             }
#             to {
#                 top:-50px;
#                 opacity:0;
#             }
#         }
#     </style>
# </htm