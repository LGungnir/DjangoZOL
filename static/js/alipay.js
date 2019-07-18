$(function () {

    // 点击支付
    $('#pay').click(function () {
        // 将订单id提交后台， 后台根据订单id获取订单信息（订单编号，订单金额等）
        $.post("/ZOL/pay/", function (data) {
            console.log(data);
            let re_url = data.re_url;
            location.href = re_url;
        });

    });

    // 自动点击
    $("#pay").trigger("click");
});

