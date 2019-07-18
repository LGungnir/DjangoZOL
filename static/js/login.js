/**
 * Created by Administrator on 2016/9/14.
 */


/**
 * Created by Administrator on 2016/9/14.
 */

$(function() {
    // 验证码重载
    $('.vcode').click(function () {
        $(this)[0].src += "?"
    })

    // 注册前再次验证
    $("#enter").click(function () {
        if ($("#user").val().length <= 0) {
            alert("用户名/手机不能为空");
            return false;
        }

        if ($("#pwd").val().length <= 0) {
            alert("密码不能为空");
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



// $(function(){
//     $(".linkparter ul li").eq(0).siblings().css("cursor","pointer")
// });
//
// $(function(){
//     $("#enter").click(function() {
//         var user = $("#user").val();
//         var pwd = $("#pwd").val();
//         var users = $.cookie("users") ? JSON.parse( $.cookie("users") ) : []
//         for(var i = 0 ; i < users.length; i ++){
//             if(users[i].user == user && users[i].pwd == pwd ){
//                 users[i].status = 1;
//                 $.cookie("users", JSON.stringify(users), {expires: 7, path: "/"});
//                 window.location.href =  "index.html";
//                 return;
//             }
//         }
//
//         for(var k=0 ; k<users.length ; k++){
//             if(users[k].user == user && users[k].pwd != pwd){
//                 alert("密码错误");
//                 return;
//             }
//         }
//
//         alert("账号未注册");
//         if (confirm("是否跳转注册界面")) {
//             window.location.href = "register.html";
//         }
//     })
// });