function showSuccessMsg() {
    $('.popup_con').fadeIn('fast', function() {
        setTimeout(function(){
            $('.popup_con').fadeOut('fast',function(){}); 
        },1000) 
    });
}

function getCookie(name) {
    var r = document.cookie.match("\\b" + name + "=([^;]*)\\b");
    return r ? r[1] : undefined;
}

$(document).ready(function () {

    // TODO: 在页面加载完毕向后端查询用户的信息
    $.ajax({
        "url":"/api/v1.0/users_info",
        "success":function (resp) {
            if(resp.errno == "0"){
                $('#user-name').val(resp.data.user_name);
                $('#user-avatar').attr('src',resp.data.avatar_url)
            }else if(resp.errno == "4102"){
                location.href='login.html'
            }
            else{
                alert(resp.errmsg)
            }
        }
    });

    // TODO: 管理上传用户头像表单的行为
    $('#form-avatar').submit(function (e) {
        e.preventDefault();
        $(this).ajaxSubmit({
            "url":'/api/v1.0/users_info',
            "type":'post',
            "contentType":'application/json',
            "headers":{
                "X-CSRFToken":getCookie('csrf_token')
            },
            "success":function (resp) {
                if(resp.errno == "0"){
                    console.log('上传成功');
                    $('#user-avatar').attr('src',resp.data.avatar_url)
                }else{
                    alert(resp.errmsg)
                }

            }
        })

    });


    // TODO: 管理用户名修改的逻辑
    $('#form-name').submit(function (e) {
        e.preventDefault();
        var user_name = $('#user-name').val();
        $.ajax({
            "url":'/api/v1.0/users_info',
            "type":'put',
            "contentType":'application/json',
            "data":JSON.stringify({'user_name':user_name}),
            "headers":{
                "X-CSRFToken":getCookie('csrf_token')
            },
            "success":function (resp) {
                if (resp.errno == "0"){
                    $('#user-name').val(resp.data.user_name);
                    showSuccessMsg();
                    $('.error-msg').hide()
                }else{
                    $('.error-msg').show()
                }

            }
        })

    })

});

