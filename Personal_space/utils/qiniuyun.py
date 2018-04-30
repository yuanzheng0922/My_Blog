# -*- coding: utf-8 -*-
# @Author : yz
# @Time   : 2018/4/30-13:35
from qiniu import Auth, put_data, etag, urlsafe_base64_encode
import qiniu.config

# 需要填写你的 Access Key 和 Secret Key
access_key = 'TNFYJcRZ8f7oNLjm-7mIIcII4zmnEpwer8Bp4u-4'
secret_key = 'mfuizJMh3p3-wa0H9cFheOs27hJopg39OfxE_wgu'
# 要上传的空间
bucket_name = 'blog'

def upload_img(file_data):
	# 构建鉴权对象
	q = Auth(access_key, secret_key)
	# 上传到七牛后保存的文件名
	key = None
	# 生成上传 Token，可以指定过期时间等
	token = q.upload_token(bucket_name, key, 3600)
	# 要上传文件的本地路径,测试
	# localfile = './fendou.jpg'
	ret, info = put_data(token, key, file_data)
	# print info  #返回类对象
	# print type(info)
	# print ret   # 返回字典
	# print type(ret)
	if info.status_code == 200:
		return ret['key']
	else:
		raise Exception('上传图片失败')

# upload_img('fendou.jpg')
#成功返回
"""
exception:None, status_code:200, _ResponseInfo__response:<Response [200]>, text_body:{"hash":"FtF48jPJQeYzqAXZvkH-YHA4pOKQ","key":"FtF48jPJQeYzqAXZvkH-YHA4pOKQ"}, req_id:XjwAAFoMts9TICoV, x_log:body;0s.ph;0s.put.in;0s.put.disk;0s.put.out;1s.put.in;1s.put.disk;1s.ph;PFDS;PFDS;body;rs38_9.sel:4;rwro.ins:4/same entry;rs38_9.sel:4;rwro.get:4;MQ;RS.not:;RS:9;rs.put:10;rs-upload.putFile:11;UP:13
{u'hash': u'FtF48jPJQeYzqAXZvkH-YHA4pOKQ', u'key': u'FtF48jPJQeYzqAXZvkH-YHA4pOKQ'}
"""