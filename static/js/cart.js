$(function () {
    // 进入先计算单个商品的总价
    $('.good_total').each(function () {
        good_total(this);
    })


    // + 号 增加数量
    $('.add').click(function () {
        cart_id = $(this).parents('tr').attr('cartid');
        let that = this;

        $.get('/ZOL/numadd/',{cart_id:cart_id},function (response) {
            handle_response(response,function () {
                // 修改页面的商品
                $(that).prev().html(response.num)
                good_total(that);
                cart_total();
            })
        })
    });


    // - 号 减少数量
    $('.reduce').click(function () {
        cart_id = $(this).parents('tr').attr('cartid');
        let that = this;

        $.get('/ZOL/numreduce/',{cart_id:cart_id},function (response) {
            handle_response(response,function () {
                if(response.msg != 'ok'){
                    alert(response.msg);
                    return false
                }
                // 修改页面的商品
                $(that).next().html(response.num)
                good_total(that);
                cart_total();
            })
        })
    });


    // 删除
    $('.del').click(function () {
        cart_id = $(this).parents('tr').attr('cartid');
        let that = this;

        if (confirm("是否确认删除")) {
            $.get('/ZOL/gooddel/',{cart_id:cart_id},function (response) {
                handle_response(response,function () {
                    $(that).parents('tr').remove();
                })
            })
        }
        else{
            return false
        }

    });


    // 勾选状态
    $('.good_select').click(function () {
        cart_id = $(this).parents('tr').attr('cartid');
        let that = this;

        $.get('/ZOL/selectchange/',{cart_id:cart_id},function (response) {
            handle_response(response,function () {
                // 修改状态
                $(that).toggleClass('glyphicon glyphicon-ok');
                get_num();
                cart_total();
                checkAll()
            })
        })
    });

    // 全选状态
    $('.all_select').click(function () {
        let isAllSelect = $(this).hasClass('glyphicon-ok') ? 1:0;

        
        $.get('/ZOL/allselect/',{isAllSelect:isAllSelect},function (response) {
            handle_response(response,function () {
                if(response.is_all_select){
                    $('.good_select').addClass('glyphicon glyphicon-ok')
                }else{
                    $('.good_select').removeClass('glyphicon glyphicon-ok')
                }
                $('.all_select').toggleClass('glyphicon glyphicon-ok');
                get_num();
                cart_total();
            })
        })
    });


    // 结算生成订单
    $('.cart_submit').click(function () {
        if($('.glyphicon-ok').length){
            $.post('/ZOL/addorder/',function (response) {
                handle_response(response,function () {
                    location.href = '/ZOL/postorder/' + response.order_id
                })
            })
        }else{
            alert('尚未选中商品');
            return false;
        }
    });


    // 单个商品总价
    function good_total(that) {
        $(that).parents('tr').find('.good_total span').html(
            parseInt($(that).parents('tr').find('.good_num span').html()) *
            parseInt($(that).parents('tr').find('.good_price span').html())
        )
    }

    // 购物车总价
    function cart_total() {
        let total = 0;
        $('.good_select.glyphicon-ok').each(function () {
            total += parseInt($(this).parents('tr').find('.good_total span').html());
        });
        $('.cart_total').find('b').html(total);
    }

    
    // 已选择商品的数目
    function get_num() {
        let num = $('.good_select.glyphicon-ok').length
        $('.cart_num').find('b').html(num)
    }

    // 判断是否为全选
    function checkAll() {
        // ok数目(不包括all)=商品勾选框数
        if($('.glyphicon-ok:not(.all_select)').length == $('.good_select').length){
            $('.all_select').addClass('glyphicon glyphicon-ok')
        }else{
            $('.all_select').removeClass('glyphicon glyphicon-ok')
        }
    }


    // 处理response
    function handle_response(response,fun) {
        if(response.status == 1){
            fun()
        }
        else if (response.status == 0){
            // 未登录，跳转到登录页面
            location.href = '/ZOL/login/'
        }
        else {
            // 弹出提示
            alert(response.msg)
        }
    }
});