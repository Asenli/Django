$(function () {
    $('.hy_show6').hover(function() {
        $(this).children('.user-card').show();
    }, function() {
        $(this).children('.user-card').hide();
    });

    $(window).scroll(function () {
        if($(window).scrollTop() > 3200){
            $(".item8-img1,.item8-img2").addClass("on");
        }
        // console.log($(window).scrollTop())
    })

    //下拉菜单
    $('.new_nav .new_list').hover(function() {
        $(this).children('div').show();

    }, function() {
        $(this).children('div').hide();
    });
    //切换新闻
    $(".con05-tab ul li").mouseenter(function(){
        $(this).addClass("on").siblings().removeClass("on");

        var _index = $(this).index();
        // var _news = ".con05-news"+_index;
        // $(".con05-zx").hide();
        // $(_news).show();
        $('.con05-zx').eq(_index).show().siblings('.con05-zx').hide();

    });

    // 顶部二维码
    $('.new_header-top .wx').hover(function() {
        $('.new_header-top .new_top-right p').show();
    }, function() {
        $('.new_header-top .new_top-right p').hide();
    });

//     //#登录时获取
//     $.ajax({
//     url:  "love/login/",
//     data:$("form").serialize(),
//     dataType:'json',
//     type:'post',
//     success:function(data){
//     var h="<p>用户名："+data.name+"欢迎来到XXX"
//     if(msg.code == '200'){
//             if(data.username){
//                 $('.new_login-in').hide()
//                 $('.user-info').show(h)
//             }
//         }
//         }
// })
    })
// $(document).ready(function() {
//
//     $.get('love/index/', function (data) {
//         alert(data.username)
//         if (data.username) {
//
//             $('.lg_user-info').html(data.username)
//             $('.lg_hide').hide()
//         }
//         else {
//             $('.lg_user').show()
//             $('.user-info').hide()
//         }
//     })
// })
