#coding=gbk

#coding=utf-8

#-*- coding: UTF-8 -*-  

from YTX_SDK.CCPRestSDK import REST
import ConfigParser

#主帐号
accountSid= '8a216da862cc8f910162d857f3f308c2'

#主帐号Token
accountToken= 'a8510c2c2a294210b5482441396d5689'

#应用Id
appId='8a216da862cc8f910162d857f45008c9'

#请求地址，格式如下，不需要写http://
serverIP='app.cloopen.com'

#请求端口 
serverPort='8883'

#REST版本号
softVersion='2013-12-26'

  # 发送模板短信
  # @param to 手机号码
  # @param datas 内容数据 格式为数组 例如：{'12','34'}，如不需替换请填 ''
  # @param $tempId 模板Id

# 单例模式
class SendSms(object):
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls,'_isinstance'):
            obj = object.__new__(cls)
            obj.rest = REST(serverIP, serverPort, softVersion)
            obj.rest.setAccount(accountSid,accountToken)
            obj.rest.setAppId(appId)

            cls._isinstance = obj
        # 返回实例对象
        return cls._isinstance

    def send_sms(self,to,datas,tempId):
        ret = self.rest.sendTemplateSMS(to,datas,tempId)
        # print ret
        if ret['statusCode'] == '000000':
            return 'OK'
        else:
            raise Exception('发送短信验证码失败')

# SendSms().send_sms('15010033033',['168',1],1)  # 测试成功

# # 将发送短信流程 提取成单例模式,较少资源浪费
# class SendSms(object):
# 
#     __isinstance = None
#     __init_num = True
#     def __new__(cls, *args, **kwargs):
#         if cls.__isinstance is None:
#             cls.__isinstance = object.__new__(cls)
#         return cls.__isinstance
# 
#     def __init__(obj):
#         if obj.__init_num:
#             obj.rest = REST(serverIP, serverPort, softVersion)
#             obj.rest.setAccount(accountSid,accountToken)
#             obj.rest.setAppId(appId)
#             obj.__init_num = False
# 
#     def send_sms(obj,to,datas,tempId):  # 发送短信方法
#         ret = obj.rest.sendTemplateSMS(to,datas,tempId)
#         return ret


# if __name__ == '__main__':
#     a = SendSms()
#     a.send_sms('18888888888',['123123',1],1)


    # print id(a),id(b)
# def sendTemplateSMS(to,datas,tempId):
#     #初始化REST SDK
#     rest = REST(serverIP,serverPort,softVersion)
#     rest.setAccount(accountSid,accountToken)
#     rest.setAppId(appId)
#
#     result = rest.sendTemplateSMS(to,datas,tempId)
#     for k,v in result.iteritems():
#
#         if k=='templateSMS' :
#                 for k,s in v.iteritems():
#                     print '%s:%s' % (k, s)
#         else:
#             print '%s:%s' % (k, v)
# # sendTemplateSMS(手机号码,内容数据,模板Id)
# sendTemplateSMS('15010033036',['123123',60],1)


