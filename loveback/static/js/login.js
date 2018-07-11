$(function(){
   $('.erweima_show').hover(function() {
       $('.erweima').show()
   }, function() {
       $('.erweima').hide()
   });
});

$(function(){
    $.ajaxSetup({
        headers: {
            'X-CSRF-TOKEN': $('meta[name="csrf-token"]').attr('content')
        }
    });
    $("#register-submit").click(function(e){
        e.preventDefault();
        var mobile = $.trim($("#register-mobile").val());

        if (mobile.length != 11 || !(/^1[3|4|5|7|8]\d{9}$/.test(mobile))) {
            $("label[for='register-mobile']").text('璇疯緭鍏ユ纭殑鎵嬫満鍙风爜').show();
            $("#register-mobile").parent().addClass('validate-has-error');
            return;
        }else{
            $("label[for='register-mobile']").text('').hide();
            $("#register-mobile").parent().removeClass('validate-has-error');
        }

        if ($.trim($("#register-password").val()).length == 0) {
            $("label[for='register-password']").text('璇疯緭鍏ュ瘑鐮�').show();
            $("#register-password").parent().addClass('validate-has-error');
            return;
        }else if ($.trim($("#register-password").val()).length > 20 || $.trim($("#register-password").val()).length < 6 ) {
            $("label[for='register-password']").text('瀵嗙爜蹇呴』涓�6浣嶅埌20涔嬮棿').show();
            $("#register-password").parent().addClass('validate-has-error');
            return;
        }else{
            $("label[for='register-password']").text('').hide();
            $("#register-password").parent().removeClass('validate-has-error');
        }

        if ($.trim($("#register-password2").val()).length == 0) {
            $("label[for='register-password2']").text('璇峰啀娆¤緭鍏ュ瘑鐮�').show();
            $("#register-password2").parent().addClass('validate-has-error');
            return;
        }else{
            $("label[for='register-password2']").text('').hide();
            $("#register-password2").parent().removeClass('validate-has-error');
        }
        if ($.trim($("#register-password").val()) !== $.trim($("#register-password2").val())) {
            $("label[for='register-password2']").text('瀵嗙爜涓嶄竴鑷�').show();
            $("#register-password2").parent().addClass('validate-has-error');
            return;
        }else{
            $("label[for='register-password2']").text('').hide();
            $("#register-password2").parent().removeClass('validate-has-error');
        }
        if ($.trim($("#register-code").val()).length == 0) {
            $("label[for='register-code']").text('璇疯緭鍏ラ獙璇佺爜').show();
            $("#register-code").parent().addClass('validate-has-error');
            return;
        }else{
            $("label[for='register-code']").text('').hide();
            $("#register-code").parent().removeClass('validate-has-error');
        }
        if (!$("#register-checkbox").prop('checked')) {
            alert("璇烽槄璇荤敤鎴峰崗璁�");
            return;
        }
        $.ajax({
            url: '/account/register',
            type: 'post',
            data: $("#register-form").serialize(),
            success: function(data) {
                window.location.href = data.redirect;
            },
            error: function(xhr) {
                alert((JSON.parse(xhr.responseText).errors).join('\n'));
            }
        });
    });

    $("#register-get-code").on('click', function(e){

        var mobile = $.trim($("#register-mobile").val());
        var captcha = $.trim($("#register-captcha").val());

        if (captcha.length != 4) {
            alert("璇峰畬鏁磋緭鍏ュ浘鐗囬獙璇佺爜");
            $(this).parent().addClass('validate-has-error');
            var captcha = $("#register-form .captcha");
            captcha.prop('src', captcha.prop('src') + ((new Date().getTime()) % 10));
            e.preventDefault();
            return;
        }

        if (mobile.length != 11 || !(/^1[3|4|5|7|8]\d{9}$/.test(mobile))) {
            $("label[for='register-mobile']").text('璇疯緭鍏ユ纭殑鎵嬫満鍙风爜').show();
            $("#register-mobile").parent().addClass('validate-has-error');
            e.preventDefault();
            return;
        }else{
            $("label[for='register-mobile']").text('').hide();
            $("#register-mobile").parent().removeClass('validate-has-error');
        }
        
        //$("#register-get-code").off('click', sendVerifyCode);
        $.ajax({
            url: '/account/send_verify_code',
            data: {mobile: mobile, captcha: captcha},
            async: true,
            type: 'post',
            success: function() {
                alert("楠岃瘉鐮佸凡鍙戦€侊紝璇锋敞鎰忔煡鏀�");
                time();
            },
            error: function(xhr) {
                alert(JSON.parse(xhr.responseText).error_msg);
                //$("#register-get-code").on('click', sendVerifyCode);
                var captcha = $("#register-form .captcha");
                captcha.prop('src', captcha.prop('src') + ((new Date().getTime()) % 10));
            }
        });
    });

    $("#register-form img.captcha").click(function(){

        var captcha = $(this);
        captcha.prop('src', captcha.prop('src') + ((new Date().getTime()) % 10));
    });

    $("#reset-submit").click(function(e){
        e.preventDefault();
        var mobile = $.trim($("#reset-mobile").val());

        if (mobile.length != 11 || !(/^1[3|4|5|7|8]\d{9}$/.test(mobile))) {
            $("label[for='reset-mobile']").text('璇疯緭鍏ユ纭殑鎵嬫満鍙风爜').show();
            $("#reset-mobile").parent().addClass('validate-has-error');
            return;
        }else{
            $("label[for='reset-mobile']").text('').hide();
            $("#reset-mobile").parent().removeClass('validate-has-error');
        }

        if ($.trim($("#reset-password").val()).length == 0) {
            $("label[for='reset-password']").text('璇疯緭鍏ュ瘑鐮�').show();
            $("#reset-password").parent().addClass('validate-has-error');
            return;
        }else if ($.trim($("#reset-password").val()).length > 20 || $.trim($("#reset-password").val()).length < 6 ) {
            $("label[for='reset-password']").text('瀵嗙爜蹇呴』涓�6浣嶅埌20涔嬮棿').show();
            $("#reset-password").parent().addClass('validate-has-error');
            return;
        }else{
            $("label[for='reset-password']").text('').hide();
            $("#reset-password").parent().removeClass('validate-has-error');
        }

        if ($.trim($("#reset-password2").val()).length == 0) {
            $("label[for='reset-password2']").text('璇峰啀娆¤緭鍏ュ瘑鐮�').show();
            $("#reset-password2").parent().addClass('validate-has-error');
            return;
        }else{
            $("label[for='reset-password2']").text('').hide();
            $("#reset-password2").parent().removeClass('validate-has-error');
        }
        if ($.trim($("#reset-password").val()) !== $.trim($("#reset-password2").val())) {
            $("label[for='reset-password2']").text('瀵嗙爜涓嶄竴鑷�').show();
            $("#reset-password2").parent().addClass('validate-has-error');
            return;
        }else{
            $("label[for='reset-password2']").text('').hide();
            $("#reset-password2").parent().removeClass('validate-has-error');
        }
        if ($.trim($("#reset-code").val()).length == 0) {
            alert("璇疯緭鍏ラ獙璇佺爜");
            $("#reset-code").parent().addClass('validate-has-error');
            return;
        }else{
            $("#reset-code").parent().removeClass('validate-has-error');
        }
        $.ajax({
            url: '/account/reset_password',
            type: 'post',
            data: $("#reset-form").serialize(),
            success: function(data) {
                alert("瀵嗙爜閲嶇疆鎴愬姛锛岃閲嶆柊鐧婚檰");
                window.location.href = "/account";
            },
            error: function(xhr) {
                alert(JSON.parse(xhr.responseText).errors.join('\n'));
            }
        });
    });
   $("#reset-get-code").on('click', function(e){
        var mobile = $.trim($("#reset-mobile").val());

        if (mobile.length != 11 || !(/^1[3|4|5|7|8]\d{9}$/.test(mobile))) {
            $("label[for='reset-mobile']").text('璇疯緭鍏ユ纭殑鎵嬫満鍙风爜').show();
            $("#reset-mobile").parent().addClass('validate-has-error');
            e.preventDefault();
            return;
        }else{
            $("label[for='reset-mobile']").text('').hide();
            $("#reset-mobile").parent().removeClass('validate-has-error');
        }
        //$("#reset-get-code").off('click', sendVerifyCode);
        $.ajax({
            url: '/account/send_reset_verify_code',
            data: {mobile: mobile},
            async: true,
            type: 'post',
            success: function() {
                alert("楠岃瘉鐮佸凡鍙戦€侊紝璇锋敞鎰忔煡鏀�");
                time();
            },
            error: function(xhr) {
                alert(JSON.parse(xhr.responseText).error_msg);
                //$("#reset-get-code").on('click', sendVerifyCode);
            }
        });
    });
    //楠岃瘉鐮佸彂閫�
    var wait = 60;
    function time() {
        var o = document.getElementById("register-get-code");
        if(o==null){
           o = document.getElementById("reset-get-code"); 
        }
        if (wait == 0) {
            o.removeAttribute("disabled");           
            o.value="鑾峰彇楠岃瘉鐮�";
            o.style.border="1px solid #ff5562";
            o.style.color="#ff5562";
            wait = 60;
        } else {
            o.style.border="1px solid transparent";
            o.style.color="#000";
            o.setAttribute("disabled", true);
            o.value="閲嶆柊鍙戦€�(" + wait + ")";
            wait--;
            console.log(o.innerHtml="閲嶆柊鍙戦€�(" + wait + ")")
            setTimeout(function() {
                time(o)
            },
            1000)
        }
    }

    $('input').keydown(function () {
        $('.error').hide();
        $('.error1').hide();
    })




});
