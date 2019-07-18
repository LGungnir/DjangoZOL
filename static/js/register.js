/**
 * Created by Administrator on 2016/9/14.
 */

$(function() {
    $("#username").blur(function () {
        if($(this).val().length < 2 || $(this).val().length > 16 ) {
            $(this).next("i").html("用户名长度不对");
        }
        else{
            $(this).next("i").html("用户名长度正确");
        }
    });

    //手机号验证
    $("#phone").blur(function () {
        var reg = /^1[34578]\d{9}$/;
        if (!reg.test($(this).val())) {
            $(this).next("i").html("手机格式不对");
        } else {
            $(this).next("i").html("手机格式正确");
        }

    });

    $("#pwd").blur(function () {
        if($(this).val().length < 6 || $(this).val().length > 18 ) {
            $(this).next("i").html("密码长度不对");
        }
        else{
       	    $(this).next("i").html("密码长度正确");
       	}
    });


    // 验证密码是否一致
    $("#pwdc").blur(function () {
        var last = $("#pwd").val();
        var now = $(this).val();
        if (last == now) {
            $(this).next("i").html("密码一致");
        } else {
            $(this).next("i").html("密码不一致");
            $(this).val("");
            $("#pwd").val("");
        }
    });


    // 验证码重载
    $('.vcode').click(function () {
        $(this)[0].src += "?"
    })

    // 注册前再次验证
    $("#register").click(function () {
        if ($("#username").val().length <= 0) {
            alert("用户名不能为空");
            return false;
        }

        if ($('#username').val().length < 2 || $("#username").val().length > 16 ) {
            alert("用户名长度不对");
            return false;
        }


        if ($("#phone").val().length <= 0) {
            alert("手机号不能为空");
            return false;
        }

        var reg = /^1[34578]\d{9}$/;
        if (!reg.test($("#phone").val())) {
            alert("手机号格式不对");
            return false;
        }

        if ($("#pwd").val().length <= 0) {
            alert("密码不能为空");
            return false;
        }

        if ($('#pwd').val().length < 6 || $("#pwd").val().length > 18 ) {
            alert("密码长度不对");
            return false;
        }

        if (!($("#pwd").val() == $("#pwdc").val())) {
            alert("两次密码输入不一致");
            return false;
        }
        if ($("#sure").val().length <= 0) {
            alert("验证码不能为空");
            return false;
        }
    })
});




//
// //验证码
// $(function(){
//     $(".code").html(Random());
//     $("#register").click(function() {
//
//         var users = $.cookie("users")? JSON.parse( $.cookie("users") ) : [];
//
//         for(var i = 0 ; i < users.length; i ++){
//             if(users[i].user == $("#phone").val() ){
//                 alert("手机已注册，请直接登录");
//
//                 return;
//             }
//         }
//         var reg = /^1[34578]\d{9}$/;
//         if(! reg.test($("#phone").val())){
//             alert("手机号格式不对");
//             return
//         }
//
//         if($("#phone").val().length <= 0){
//             alert("手机号不能为空");
//             return;
//         }
//         if($("#pwd").val().length <= 0){
//             alert("密码不能为空");
//             return;
//         }
//         if(! ($("#pwd").val() == $("#pwdc").val()) ){
//             alert("两次密码输入不一致");
//             return;
//         }
//
//         if(! ( $(".sure").val() == $(".code").html()) ){
//             $(".code").html(Random());
//             alert("验证码错误")
//             return;
//         }
//
//         for(var p=0 ; p  < users.length  ; p++){
//             users[p].status = 0;
//         }
//
//         var user = {"user": $("#phone").val(), "pwd": $("#pwd").val(),"status" : 1};
//         users.push(user);
//         $.cookie("users", JSON.stringify(users), {expires: 7, path: "/"});
//         alert("注册成功。。。即将跳转");
//         window.location.href = "index.html";
//     });
//
//
//     function Random() {
//         var str = "";
//         for(var i=0 ; i<4 ; i++){
//             var a = parseInt(Math.random()*10)
//             str +=a;
//         }
//         return str;
//     }
// });
