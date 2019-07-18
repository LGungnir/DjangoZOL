$(function () {
    // 前端做本地校验
    var flag = true;

    // # 检测手机号格式是否正确
    $('#phone').blur(function () {
        let phone = $(this).val();
        if(/^1[34578]\d{9}$/.test(phone)){
            flag = true;
            $('#phone_msg').html('');
        }
        else{
            flag = false;
            $('#phone_msg').html('手机格式错误').css({'color':'red','font-size':'14px'});
        }
    })

    $('#receive_submit').click(function () {
        if(!flag){
           // 有输入不合法
            alert('输入不合法,请检查！');
            return false
        }
    })
})