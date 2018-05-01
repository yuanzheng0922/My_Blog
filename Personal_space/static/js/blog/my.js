function getCookie(name) {
    var r = document.cookie.match("\\b" + name + "=([^;]*)\\b");
    return r ? r[1] : undefined;
}

// TODO:退出执行操作
function logout() {
    $.ajax({
        "url":"/api/v1.0/auth_users",
        "type":"delete",
        "headers":{
            "X-CSRFToken":getCookie("csrf_token")
        },
        "success":function (resp) {
            if (resp.errno == "0"){
                location.href = "index.html"
            }
        }
    })
}

$(document).ready(function(){

    // TODO: 在页面加载完毕之后去加载个人信息
    $.ajax({
        "url":'/api/v1.0/users_info',
        "success":function (resp) {
            if(resp.errno == "0"){
                $('#user-avatar').attr('src',resp.data.avatar_url);
                $('#user-name').html(resp.data.user_name);
                $('#user-mobile').html(resp.data.user_mobile);
            }else{
                alert(resp.errmsg)
            }

        }
    })

});
