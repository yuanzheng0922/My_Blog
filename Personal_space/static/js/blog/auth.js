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

$(document).ready(function(){
    // TODO: 查询用户的实名认证信息
    $.ajax({
        "url":"/api/v1.0/auth_users",
        "success":function (resp) {
            if(resp.errno == "0"){
                $("#real-name").val(resp.data.real_name);
                $("#real-name").attr("disabled","disabled");
                $("#id-card").val(resp.data.id_card);
                $("#id-card").attr("disabled",true);
                $(".btn-success").hide()
            }
        }
    });

    // TODO: 管理实名信息表单的提交行为
    $("#form-auth").submit(function (e) {
        e.preventDefault();
        var real_name = $("#real-name").val();
        var id_card = $("#id-card").val();
        var params = {
            "real_name":real_name,
            "id_card":id_card
        };
        $.ajax({
            "url":"/api/v1.0/auth_users",
            "type":"post",
            "contentType":"application/json",
            "data":JSON.stringify(params),
            "headers":{
                "X-CSRFToken":getCookie("csrf_token")
            },
            "success":function (resp) {
                if(resp.errno == "0"){
                    showSuccessMsg()
                    $(".error-msg").hide()
                }else if(resp.errno == "4102"){
                    location.href = "login.html"
                }
                else if(resp.errno == "4003"){
                    $(".error-msg").text(resp.errmsg)                }
                else{
                    $(".error-msg").show()
                }
            }
        })
    })
});