//颜色类别color - suit
$(function(){
    $(".size i").click(function() {
        $(this).addClass("active").siblings("i").removeClass("active");
    });
    $(".color i").click(function() {
        $(this).addClass("active").siblings("i").removeClass("active");
    });
});


//商品数量
$(function(){
    $(".buy-number li").eq(1).siblings().css("cursor","pointer");
    $(".buy-number li").eq(0).click(function() {
        var num = parseInt($(".number li").eq(1).html());
        if(num==1){
            $(".buy-number li").eq(1).html(1);
            return
        }
        $(".buy-number li").eq(1).html(num-1);
    });
    $(".buy-number li").eq(2).click(function() {
        var num =parseInt($(".buy-number li").eq(1).html());
        $(".buy-number li").eq(1).html(num+1);
    });
});


$(function () {
    // 加入购物车
    $('.add').click(function (e) {
        let goodId = $(this).attr('goodId');        // 商品id
        let num = parseInt($('.goodNum').html());   // 商品数量

        let count = $('.active').length;            // 颜色，ram，rom的class被选中的数量
        if(count != 3){
            alert('尚未选择完全，请检查');
            return false;
        }
        let color = $('.active').eq(0).html();      // 颜色
        let ram = $('.active').eq(1).html();        // ram
        let rom = $('.active').eq(2).html();        // rom

        let data = {
            goodId: goodId,
            num: num,
            color:color,
            ram:ram,
            rom:rom,
        };

        //发送请求
        $.post('/ZOL/addcart/',data,function (response) {

            //没有登录
            if(response.status == 0){
                alert(response.msg);
                location.href = '/ZOL/login/'
            }
            else if(response.status == 1){
                // 购物车添加的特效
                var src = $(".goodimg").find("img").attr("src")
                var flyer = $("<img class='u-flyer'/>");
                flyer.attr("src",src);
                flyer.fly({
                    start:{
                        left : e.pageX,
                        top : e.pageY,
                        width : 90,
                        height : 90
                    },
                    end : {
                        left : $(".ico li").eq(2).offset().left,
                        top : $(".ico li").eq(2).offset().top,
                        width : 0,
                        height : 0
                    },
                    onEnd : function() {
                        $("#msg").show().animate({width : "250px"},200).fadeOut(1000);
                        coding();
                    }
                });
            }
        })
    })

    // 立即购买
    $('.buy').click(function () {
        let goodId = $(this).attr('goodId');        // 商品id
        let num = parseInt($('.goodNum').html());   // 商品数量

        let count = $('.active').length;            // 颜色，ram，rom的class被选中的数量
        if(count != 3){
            alert('尚未选择完全，请检查');
            return false;
        }
        let color = $('.active').eq(0).html();      // 颜色
        let ram = $('.active').eq(1).html();        // ram
        let rom = $('.active').eq(2).html();        // rom

        let data = {
            goodId: goodId,
            num: num,
            color:color,
            ram:ram,
            rom:rom,
        };

        $.post('/ZOL/buynow/',data,function (response) {
            if(response.status == 1){
                // 再跳转到提交订单页面
                location.href = '/ZOL/postorder/' + response.order_id
            }
            else if (response.status == 0){
                // 未登录，跳转到登录页面
                location.href = '/ZOL/login/'
            }
            else {
                // 弹出提示
                alert(response.msg)
            }
        })
    })
})



