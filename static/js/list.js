/**
 * Created by Administrator on 2016/9/19.
 */
$(function(){
    $.get("json/1f.json",function(data) {
        for(var i=1 ; i < data.length ; i++){
            var a = "<a href='goodsdetail.html?" + data[i].id + "'><img src='"+data[i].img +"'/></a>";
            var div = "<div class='goods-title'>【顺丰包邮】"+data[i].a+data[i].p +"</div>";
            var span = "<span>￥"+data[i].price +"</span>"
            var li = $("<li><div>" +a + div+ span + "</div></li>");
            $(".goods-list-detail").append(li);
        }

    })
});