#coding=gbk

#coding=utf-8

#-*- coding: UTF-8 -*-  

from YTX_SDK.CCPRestSDK import REST
import ConfigParser

#���ʺ�
accountSid= '8a216da862cc8f910162d857f3f308c2'

#���ʺ�Token
accountToken= 'a8510c2c2a294210b5482441396d5689'

#Ӧ��Id
appId='8a216da862cc8f910162d857f45008c9'

#�����ַ����ʽ���£�����Ҫдhttp://
serverIP='app.cloopen.com'

#����˿� 
serverPort='8883'

#REST�汾��
softVersion='2013-12-26'

  # ����ģ�����
  # @param to �ֻ�����
  # @param datas �������� ��ʽΪ���� ���磺{'12','34'}���粻���滻���� ''
  # @param $tempId ģ��Id

# ����ģʽ
class SendSms(object):
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls,'_isinstance'):
            obj = object.__new__(cls)
            obj.rest = REST(serverIP, serverPort, softVersion)
            obj.rest.setAccount(accountSid,accountToken)
            obj.rest.setAppId(appId)

            cls._isinstance = obj
        # ����ʵ������
        return cls._isinstance

    def send_sms(self,to,datas,tempId):
        ret = self.rest.sendTemplateSMS(to,datas,tempId)
        # print ret
        if ret['statusCode'] == '000000':
            return 'OK'
        else:
            raise Exception('���Ͷ�����֤��ʧ��')

# SendSms().send_sms('15010033033',['168',1],1)  # ���Գɹ�

# # �����Ͷ������� ��ȡ�ɵ���ģʽ,������Դ�˷�
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
#     def send_sms(obj,to,datas,tempId):  # ���Ͷ��ŷ���
#         ret = obj.rest.sendTemplateSMS(to,datas,tempId)
#         return ret


# if __name__ == '__main__':
#     a = SendSms()
#     a.send_sms('18888888888',['123123',1],1)


    # print id(a),id(b)
# def sendTemplateSMS(to,datas,tempId):
#     #��ʼ��REST SDK
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
# # sendTemplateSMS(�ֻ�����,��������,ģ��Id)
# sendTemplateSMS('15010033036',['123123',60],1)


