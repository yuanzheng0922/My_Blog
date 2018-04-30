function getCookie(name) {
    var r = document.cookie.match("\\b" + name + "=([^;]*)\\b");
    return r ? r[1] : undefined;
}

function generateUUID() {
    var d = new Date().getTime();
    if(window.performance && typeof window.performance.now === "function"){
        d += performance.now(); //use high-precision timer if available
    }
    var uuid = 'xxxxxxxx-xxxx-4xxx-yxxx-xxxxxxxxxxxx'.replace(/[xy]/g, function(c) {
        var r = (d + Math.random()*16)%16 | 0;
        d = Math.floor(d/16);
        return (c=='x' ? r : (r&0x3|0x8)).toString(16);
    });
    return uuid;
}
var imageCodeId = "";
// 生成一个图片验证码的编号，并设置页面中图片验证码img标签的src属性
function generateImageCode() {
    imageCodeId=generateUUID();  //生成uuid
    console.log(imageCodeId);
    var url = '/api/v1.0/image_code?uu_id='+imageCodeId;
    $('.image-code>img').attr('src',url)
}

function sendSMSCode() {
    // 校验参数，保证输入框有数据填写
    $(".phonecode-a").removeAttr("onclick");
    var mobile = $("#mobile").val();
    if (!mobile) {
        $("#mobile-err span").html("请填写正确的手机号！");
        $("#mobile-err").show();
        $(".phonecode-a").attr("onclick", "sendSMSCode();");
        return;
    } 
    var imageCode = $("#imagecode").val();
    if (!imageCode) {
        $("#image-code-err span").html("请填写验证码！");
        $("#image-code-err").show();
        $(".phonecode-a").attr("onclick", "sendSMSCode();");
        return;
    }
    var params = {
        "mobile":mobile,
        "img_code":imageCode,
        "img_code_id":imageCodeId
    };
    // TODO: 通过ajax方式向后端接口发送请求，让后端发送短信验证码
    $.ajax({
        "url":"/api/v1.0/sms_code",
        "type":'post',
        "data":JSON.stringify(params),
        "contentType":"application/json",
        "headers":{
            "X-CSRFToken":getCookie("csrf_token")
        },
        "success":function (resp) {
            //成功
            // console.log('成功从后端返回');
            if (resp.errno == "0"){
                alert('发送成功,请查看手机')
                // 设置倒计时
                var num = 60;
                var rid = setInterval(function () {
                    num -= 1;
                    if (num <= 0){
                        clearInterval(rid);  //清除定时器
                        $('.phonecode-a').html('获取短信码');
                        $(".phonecode-a").attr("onclick", "sendSMSCode();");
                    }else
                    {
                        $('.phonecode-a').html(num + '秒')
                    }
                },1000)
            }else if(resp.errno == "4003"){
                alert(resp.errmsg)
                $(".phonecode-a").attr('onclick',"sendSMSCode()")
            }
            else
            {
                $("#phone-code-err>span").html(resp.errmsg);
                $("#phone-code-err").show();
                //重新刷新点击获取sms_code事件
                $(".phonecode-a").attr('onclick',"sendSMSCode()")

            }

        }


    })
}

$(document).ready(function() {
    generateImageCode();  // 生成一个图片验证码的编号，并设置页面中图片验证码img标签的src属性
    $("#mobile").focus(function(){
        $("#mobile-err").hide();
    });
    $("#imagecode").focus(function(){
        $("#image-code-err").hide();
    });
    $("#phonecode").focus(function(){
        $("#phone-code-err").hide();
    });
    $("#password").focus(function(){
        $("#password-err").hide();
        $("#password2-err").hide();
    });
    $("#password2").focus(function(){
        $("#password2-err").hide();
    });


    // TODO: 注册的提交(判断参数是否为空)
    $('.form-register').submit(function (e) {
        //阻止表单默认提交
        e.preventDefault();
        var mobile = $("#mobile").val();
        var password=$("#password").val();
        var rpassword=$("#password2").val();

        var params = {
            "mobile": mobile,
            "password":password ,
            "rpassword":rpassword
         };
        $.ajax({
            "url":"/api/v1.0/form_user",
            "type":"post",
            "contentType":"application/json",
            "data":JSON.stringify(params),
            "headers":{
                "X-CSRFToken":getCookie("csrf_token")
            },
            "success":function (resp) {
                if(resp.errno == "0"){
                    location.href = 'login.html'
                }else if(resp.errno == "4106"){
                    alert(resp.errmsg)
                }
                else{
                    alert('提交失败,请核实填入信息')
                }

            }


        })
    })
});
