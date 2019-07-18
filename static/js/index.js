/**
 * Created by Administrator on 2016/9/10.
 */

// //读取cookie并显示在左上角
// $(function(){
//     var users = $.cookie("users") ? JSON.parse( $.cookie("users") ) : [];
//     var usersgood = $.cookie("usersgood") ? JSON.parse( $.cookie("usersgood") ) : [];
//     var num = 0;
//     var user  = "";
//     for(var k=0 ;k<users.length  ; k++){
//         if(users[k].status == 1){
//             user = users[k].user;
//         }
//     }
//
//     for(var i=0 ; i < usersgood.length ; i++){
//             if ( user == usersgood[i].user ) {
//                 var obj = usersgood[i];
//                 for(var x=0 ; x<obj.data.length ; x++){
//                     num += parseInt(obj.data[x].num);
//                 }
//         }
//     }
//     $(".shopcar a").find("span").html(num);
//     if(user !=""){
//         $(".login").find("a").html(user);
//         $(".login").find("a").attr("href","index.html")
//         $(".register").hide();
//         $(".cancell").show();
//     }else {
//         $(".login").find("a").html("登录");
//         $(".login").find("a").attr("href","login.html")
//     }
// });
//
// //注销当前用户
// $(function(){
//     $(".cancell a").click(function() {
//         var users = $.cookie("users")? JSON.parse( $.cookie("users") ) : [];
//         for(var i=0 ; i<users.length ; i++){
//             users[i].status = 0 ;
//         }
//         $.cookie("users", JSON.stringify(users), {expires: 7, path: "/"});
//         window.location.reload();
//     });
// });

//toolbar
$(function(){
    $("#toolbar .ico li").mouseenter(function() {
        $(this).find("a").show().stop().animate({"width":68,"left":-68});
        $(this).css("background","red");
    }).mouseleave(function() {
        $(this).find("a").stop().animate({"width":0,"left":0}).hide()
        $(this).css("background","#2d2d2d");
    })
});

//悬浮搜索框
$(function(){
    $(window).scroll(function() {
        //700显示
        if ($(document).scrollTop()>700) {
            $("#search-layer").show()
        }else{
            $("#search-layer").hide()
        }
    });
});

//Ajax请求数据 轮播图
$(  function(){
    // $.get("/static/json/banner.json",function(data) {
    $.get("/ZOL/getbanners/",function(data) {
        for(var i=0 ; i<data.length ; i++){
            var li = $("<li><a href='#'><img src=" +data[i].img +"></a></li>");
            $(".changeimg").append(li);
            var barli = $("<li>" + i + "</li>");
            $(".bar").append(barli);
        }
        //$(function () {
        var _width = $(".changeimg").find("li").width();
        var index = 0;
        var change = $(".changeimg");
        $(".bar li").eq(0).css("background", "red");
        showImg(0, change);
        $(".bar li").mouseenter(function () {
            window.clearInterval(change.timer);
            index = $(this).index();
            change.stop().animate({"left": "-" + index * _width + "px"});
            $(this).css("background", "red").siblings().css("background", "#000");
        }).mouseleave(function() {
            showImg(index++, change)
        })
        //target :滚动ul
        function showImg(index, target) {
            target.timer = window.setInterval(function () {
                index++;
                var end = false;
                if (index >= target.find("li").length) {
                    index = 0;
                    target.stop().animate({"left": "0"}, 800);
                    target.stop().animate({"left": "0"}, 1000);
                    $(".bar li").eq(0).css("background", "red").siblings().css("background", "#000")
                    end = true;
                }
                if (!end) {
                    target.stop().animate({"left": "-=" + _width + "px"}, 1000);
                    $(".bar li").eq(index).css("background", "red").siblings().css("background", "#000")
                }
            }, 3000)
        }
        //});
    })

});

//商品轮播图
$(function () {
    // $.get("/static/json/lun.json",function(data) {
    $.get("/ZOL/getluns/",function(data) {
        for(var i=0 ; i<data.length ; i++){
            (function(index) {
                var li = $("<li><a href='#'><img src=" +data[index].img +"></a></li>");
                $(".smalllun").append(li);
                var barli = $("<li>" + index + "</li>");
                $(".bar1").append(barli);
            })(i)
        }
        //$(function(){
        var _width = $(".smalllun").find("li").width();
        var index = 0;
        var changeUl = $(".smalllun");
        $(".main_list .bar1 li").eq(0).css("background", "red");
        showImg(0, changeUl);

        $(".main_list .bar1 li").mouseenter(function () {
            window.clearInterval(changeUl.timer);
            index = $(this).index();
            changeUl.stop().animate({"left": "-" + index * _width + "px"});
            $(this).css("background", "red").siblings().css("background", "#000");
        }).mouseleave(function() {
            showImg(index++, changeUl)
        })
        function showImg(index, target) {
            target.timer = window.setInterval(function () {
                index++;
                var end = false;
                if (index >= target.find("li").length) {
                    index = 0;
                    target.stop().animate({"left": "0"}, 800);
                    target.stop().animate({"left": "0"}, 1000);
                    $(".main_list .bar1 li").eq(0).css("background", "red").siblings().css("background", "#000")
                    end = true;
                }
                if (!end) {
                    target.stop().animate({"left": "-=" + _width + "px"}, 1000);
                    $(".main_list .bar1 li").eq(index).css("background", "red").siblings().css("background", "#000")
                }
            }, 3000)
        }
        //});
    })
});

//Ajax请求数据 加载图片
$(function(){
    // $.get("/static/json/tuanlist.json",function(data) {
    $.get("/ZOL/gettuans/",function(data) {
        for(var i=0 ; i<data.length ; i++){
            (function(index) {
                var li = $("<li><a href='#'><img src=" +data[index].img +"></a></li>");
                $(".tuan_list ul").append(li);
            })(i)
        }
    })
});

//买家中心
$(function () {
    $(".buycenter").mouseover(function () {
        $(".buycenter_info").show();
    }).mouseout(function () {
        $(".buycenter_info").hide();
    })
});

//手机商城
$(function () {
    $(".menu_phone").mouseover(function () {
        $(".menu_phone_pic").show();
    }).mouseout(function () {
        $(".menu_phone_pic").hide()
    })
});

//联系客服
$(function () {
    $(".con_ser").mouseover(function () {
        $(".con_ser_phone").show();
    }).mouseout(function () {
        $(".con_ser_phone").hide();
    })
});

//导航栏
$(function () {
    $(".menu_nav_container .menu_nav_containerli").mouseover(function () {
        $(this).find(".menu_nav_containerfirst").find("a").css("color", "#333");
        $(this).css("border-left", "1px solid #ccc");
        $(this).find(".service").show();
        var index = $(this).index();
        var top = -index * 39;
        $(this).find(".service").css("top", top);
    }).mouseout(function () {
        $(this).find(".menu_nav_containerfirst").find("a").css("color", "#fff");
        $(this).css("border-left", "1px solid #2d2d2d");
        $(this).find(".service").hide();
    })
});

//content图片浮动
$(function () {
    $(".listtall,.listshort").mouseenter(function () {
        $(this).find("img").stop().animate({"top": 65});
    }).mouseleave(function () {
        $(this).find("img").stop().animate({"top": 75});
    })
});

//一元夺宝特效
$(function () {
    $(".oneMoney").find("li").mouseenter(function () {
        $(this).find(".phoneScancode").show();
        $(this).find(".oneMoney_box").find("p").hide()
    }).mouseleave(function () {
        $(this).find(".phoneScancode").hide();
        $(this).find(".oneMoney_box").find("p").show()
    })
});

//使用Ajax获取1f的数据
$(function() {
    let num = 1;
    // $.get("/static/json/1f.json",function (data) {
    $.get("/ZOL/getfloorgoods/",{num:num},function (datas) {
        for(var j=0;j<datas.length;j++){
            data = datas[j];
            var a = $("<a href='#'><img src="+ data[0].img + "></a>");
            $(".secondfloor").eq(j).find(".main_sell").append(a);
            for(var i=1 ;i<3  ; i++){
                var x = i;
                var con =$(" <div><a href='#'>"+data[i].a+"</a> </div> <p>"+data[i].p+"</p> <a href='goodsdetail.html?"+data[i].id+"'><img src=" +data[i].img +" ></a>");
                $(".secondfloor").eq(j).find(".listtall").eq(x-1).append(con);
            }
            for(var i=3 ;i<data.length ; i++){
                var x = i;
                var con =$(" <div><a href='#'>"+data[i].a+"</a> </div> <p>"+data[i].p+"</p> <a href='goodsdetail.html?"+data[i].id+"'><img src=" +data[i].img +" ></a>");
                $(".secondfloor").eq(j).find(".listshort").eq(x-3).append(con);
            }
        }

    });
})
