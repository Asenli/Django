


//  $(function(){
//     $('.apply_box_btn').live('click',function(event) {
//         console.log($(this).data('channel'));
//         if($(this).data('channel'))
//            $('.contact-box  input[name="channel"]').val($(this).data('channel'));
//         $('.contact-box').show();
        
//     });
//     $('.contact-box .close').live('click',function(event) {
//         $('.contact-box').hide();
//     });
// });

// 意向单提交
 $(function(){
    var $form = $('#contact-form');

    $form.submit(function (e) {
        e.preventDefault();

        var name = $form.find('input[name="realname"]').val();
        var phone = $form.find('input[name="mobile"]').val();

        if (!/^1[3|4|5|7|8]\d{9}$/.test(phone)) {
            alert('号码格式错误～请检查～');
            return false;
        }

        $.ajax({
            url: 'http://api.junzhinuo1314.com/api/newWillInput',
            type: 'post',
            data: $form.serialize(),
            // xhrFields: {
            //     withCredentials: true
            // },
            success: function () {
                alert('感谢提交,我们的顾问会稍后联系您!');
                $('.contact-box').slideUp();
                $form[0].reset();
            },
            error: function () {
                alert('抱歉～出错了～请稍后重试～');
            }
        });
    })
 });


$(function(){
	$('.arr_top').click(function(e) {

			$('html,body').animate({ scrollTop:0 },500)
	    });



		//修改头像
	 $('.bg-banner .avatar .avat').click(function(event) {
	 	$('.tx_fixed').show();
	 });
	//头像选择
	$('.tx_fixed .pre span').click(function(event) {
		$(this).addClass('on').siblings().removeClass('on')
	});

	//关闭上传头像
	$('.tx_fixed .close').click(function(event) {
		$('.tx_fixed').hide();
	});


	$(window).scroll(function(){
				var x = $(window).scrollTop();	//得到现在的卷动高度
				if(x > 500){
					$(".s_top").fadeIn();
				}else{
					$(".s_top").fadeOut();
				}
			});

	$('.side_fixed ul .ab').hover(function() {
		$(this).children('a').css('display', 'block').siblings().hide();

	}, function() {
		$(this).children('a').css('display', 'none').siblings().show();
	});
	// 意向单
	$('.side_qgzx').hover(function() {
		$(this).children('.side_yxd').show();
	}, function() {
		$(this).children('.side_yxd').hide();
	});

	// 二维码
	$('.side_ewm').hover(function() {
		$(this).children('.hz_ewm').show();
	}, function() {
		$(this).children('.hz_ewm').hide();
	});

	// 回到顶部
	$('.s_top').click(function(e) {
	        
			$('html,body').animate({ scrollTop:0 },500)
	    });


	// 用户登录下滑
	$('.hy_show').hover(function() {
		$(this).children('.user-card').show();
	}, function() {
		$(this).children('.user-card').hide();
	});

	$('.dl-avatar').hover(function() {
		$(this).children('.user-card').show();
	}, function() {
		$(this).children('.user-card').hide();
	});

	


});