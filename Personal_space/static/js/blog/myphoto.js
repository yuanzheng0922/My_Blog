$(document).ready(function(){
    // TODO: 对于发布房源，只有认证后的用户才可以，所以先判断用户的实名认证状态
    $.ajax({
        "url":"/api/v1.0/auth_users",
        "success":function (resp) {
            if (resp.errno == "0"){
                // alert('ok')
                $(".auth-warn").hide();

            }else{
               $(".auth-warn").show();

            }

        }
    });

    // TODO: 如果用户已实名认证,那么就去请求之前发布的房源

});
