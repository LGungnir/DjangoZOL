// 顶部导航栏
// 买家中心
$(function () {
    $(".buycenter").mouseover(function () {
        $(".buycenter_info").show();
    }).mouseout(function () {
        $(".buycenter_info").hide();
    })
});

// 手机商城
$(function () {
    $(".menu_phone").mouseover(function () {
        $(".menu_phone_pic").show();
    }).mouseout(function () {
        $(".menu_phone_pic").hide()
    })
});

// 联系客服
$(function () {
    $(".con_ser").mouseover(function () {
        $(".con_ser_phone").show();
    }).mouseout(function () {
        $(".con_ser_phone").hide();
    })
});


// 右侧导航栏
//  toolbar
$(function(){
    $("#toolbar .ico li").mouseenter(function() {
        $(this).find("a").show().stop().animate({"width":68,"left":-68});
        $(this).css("background","red");
    }).mouseleave(function() {
        $(this).find("a").stop().animate({"width":0,"left":0}).hide()
        $(this).css("background","#2d2d2d");
    })
});


// 搜索框
$(function () {
    $('.kw_search').click(function () {
        if($(this).prev().val()){

        }
        else{
            alert('请输入关键词');
            return false
        }
    })
})