/**
 * Created by Administrator on 2016/9/13.
 */
//Ajax导入数据
// $(function(){
//
//     if(location.search){
//         var id = location.search
//
//         id = id.split("?")[1];
//     }
//
//     $.get("json/1f.json",function(data) {
//         for(var i=1 ; i<data.length ; i++){
//             var obj = data[i];
//             if (id == obj.id) {
//                 var img = $("<img src="+ obj.goodimg.big +">");
//                 $(".goodimg").append(img);
//                 var h1 = $("<h1></h1>").html("【顺丰包邮】")
//                 var span = $("<span class='detail'>"+obj.p +"</span>");
//                 var h2 = $("<h2>价格<i>￥" + obj.price + "</i></h2>");
//                 $(".gooddetail").prepend(h1,span,h2);
//                 for(var j=0 ; j<obj.goodimg.small.length; j++){
//                     var simg = $("<li><img src="  + obj.goodimg.small[j].img+   "></li>");
//                     $(".smallgood").append(simg);
//                 }
//             }
//         }
//         //切换大图
//         $(function(){
//             $(".smallgood li img").mouseenter(function() {
//                 $(".goodimg img").attr("src",$(this).attr("src"))
//             })
//         });
//
//         //放大镜
//         $(function(){
//             var _smallImg = $(".goodimg img");
//             var _smallArea = $(".smallArea");
//             var _bigImg = $(".bigArea img");
//             var _bigArea = $(".bigArea");
//             var scale = _bigImg.width() / _smallImg.width();
//             $(".goodimg").mousemove(function(e) {
//                 _bigImg.attr("src",$(".goodimg img").attr("src"));
//                 _smallArea.show();
//                 _bigArea.show()
//
//                 var x= e.pageX-  _smallImg.offset().left -_smallArea.width()/2;
//                 var y = e.pageY - _smallImg.offset().top - _smallArea.height()/2
//                 if(x<0){
//                     x = 0;
//                 }
//                 else if(x > _smallImg.width() - _smallArea.width()){
//                     x = _smallImg.width() - _smallArea.width();
//                 }
//                 if(y<0){
//                     y = 0;
//                 }
//                 else if(y > _smallImg.height() - _smallArea.height()){
//                     y = _smallImg.height() - _smallArea.height();
//                 }
//
//                 _smallArea.css({left:x,top:y});
//
//                 _bigImg.css({left:-x*scale,top:-y*scale});
//
//             }).mouseleave(function() {
//                 $(".smallArea").hide();
//                 $(".bigArea").hide()
//             })
//
//         });
//
//     })
// });

$(function(){
    $(".category_nav .menu_nav_container").hide();
    $(".nav_list li").find("a").eq(0).css("color","balck");

});

$(function(){
    $(".category_nav h2").mouseenter(function() {
        $(".category_nav .menu_nav_container").show();
    }).mouseleave(function() {
        $(".category_nav .menu_nav_container").hide();
    })

    $(".category_nav .menu_nav_container").mouseleave(function() {
        $(this).hide();
    }).mouseenter(function() {
        $(this).show();
    })
});



//购物车特效
// $(function(){
//     $(".add").click(function(e) {
//         var users = $.cookie("users") ? JSON.parse( $.cookie("users") ) : [];
//         if(users.length <= 0){
//             alert("未登录,跳转登录界面");
//             window.location.href = "login.html";
//             return
//         }
        // var src = $(".goodimg").find("img").attr("src")
        // var flyer = $("<img class='u-flyer'/>");
        // flyer.attr("src",src);
        // flyer.fly({
        //     start:{
        //         left : e.pageX,
        //         top : e.pageY,
        //         width : 90,
        //         height : 90
        //     },
        //     end : {
        //         left : $(".ico li").eq(2).offset().left,
        //         top : $(".ico li").eq(2).offset().top,
        //         width : 0,
        //         height : 0
        //     },
        //     onEnd : function() {
        //         $("#msg").show().animate({width : "250px"},200).fadeOut(1000);
        //         coding();
        //     }
        // });
    // });
    //加入购物车的时候写入cookie
//     function coding () {
//         var usersgood = $.cookie("usersgood") ? JSON.parse( $.cookie("usersgood") ) : [];
//         var users = $.cookie("users") ? JSON.parse( $.cookie("users") ) : [];
//         var user = "";
//         for(var r=0 ; r<users.length ; r++){
//             if(users[r].status == 1){
//                 user = users[r].user;
//             }
//         }
//         users = user;
//         var goodid = location.search.split("?")[1];
//         var num = $(".buy-number li").eq(1).html();
//         var color = $(".active").eq(0).html()
//         var suit = $(".active").eq(1).html()
//         var pass = true;
//         //该买家买过商品
//         for(var i=0 ; i<usersgood.length ; i++){
//             (function(index) {
//                 if (users == usersgood[index].user) {
//                     var data = usersgood[index].data;
//                     data.push({id: goodid,num:num,color:color,suit:suit});
//                     $.cookie("usersgood",JSON.stringify(usersgood),{expires: 7, path: "/"});
//                     pass  = false;
//                 }
//             })(i);
//         }
//
//         //该买家没有买过商品(一次都没)
//         if (pass) {
//             var obj ={user : users,data : [{id: goodid,num:num,color:color,suit:suit}]};
//             usersgood.push(obj);
//             $.cookie("usersgood",JSON.stringify(usersgood),{expires: 7, path: "/"});
//         }
//     }
// });







/*cookie格式 买家购买相关信息
*当前用户名var users = $.cookie("users") ? JSON.parse( $.cookie("users") ) : []
* users[users.length-1].user
* cookie名称usersgood
*[
*   {user : 手机号,
*    data:[
*               {id:商品ID,num:商品数量},
*               {id:商品ID,num:商品数量},
*               ......
*           ]
*   },
*   {user : 手机号,
*    data:[
*               {id:商品ID,num:商品数量},
*               {id:商品ID,num:商品数量},
*               ......
*           ]
*   }
* ]
*
*
* */