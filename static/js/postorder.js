$(function () {
    $('.order_submit').click(function () {
        // 获取被选取的收货信息的id
        let receive_id = $('input[name="receive_select"]:checked').parents('.receive_info').attr('receive_id');
        if(!receive_id){
            alert('收货地址尚未选择')
            return false
        }
        let order_id = $('.order_submit').attr('order_id');

        data = {
            receive_id:receive_id,
            order_id:order_id,
        }

        $.post('/ZOL/orderaddreceive/',data,function (response) {
            if(response.status == 1){
                location.href = '/ZOL/api/'
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

