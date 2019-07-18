$(function () {
    // 检测是否存在收货信息
    $('.topay').click(function () {
        if($(this).parents('tr').find('.toreceive').html()){
            alert('请填写收货信息')
            return false;
        }
    })
})