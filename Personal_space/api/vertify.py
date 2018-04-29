# -*- coding: utf-8 -*-
# @Author : yz
# @Time   : 2018/4/29-2:02
from . import api
from flask import request, current_app, make_response, jsonify, abort
from Personal_space.utils.captcha.captcha import captcha
from Personal_space import redis_storage
from Personal_space import constants
from Personal_space.response_code import RET
import random
from Personal_space.utils.sms import SendSms
import re


@api.route('/image_code')
def generate_img_code():  # 获取图片验证码
	# 获取uu_id,存储再redis中作为标识
	uu_id = request.args.get('uu_id')
	# 如果异常没有获取到uuid
	if not uu_id:
		abort(403)
	# 生成图片验证码
	name, text, data = captcha.generate_captcha()
	current_app.logger.info('图片验证码内容::%s' % text)

	try:
		# 将图片验证码保存再redis中并设置过期时间
		redis_storage.set('imageCode:%s' % uu_id, text, constants.IMAGE_CODE_REDIS_EXPIRES)
	except Exception as e:
		current_app.logger.error(e)
		return jsonify(errno=RET.DBERR, errmsg='保存图片验证码失败')
	# 设置响应content-type
	response = make_response(data)
	response.headers['Content-Type'] = 'image/jpg'  # 兼容不同浏览器
	return response


@api.route('/sms_code', methods=['POST'])
def send_sms_code():  # 发送短信验证码
	'''
	.获取手机号,图片验证码,进行校验
	.生成短信验证码
	.发送短信验证码
	.保存短信验证码到redis
	.返回响应
	'''
	print ('请求成功')
	resp_dict = request.json
	mobile = resp_dict.get('mobile')
	img_code = resp_dict.get('img_code')
	img_code_id = resp_dict.get('img_code_id')
	# 判断参数有效性
	if not all([mobile, img_code, img_code_id]):
		return jsonify(errno=RET.PARAMERR, errmsg='参数有误')
	#判断手机号有效性
	if not re.match(r'^1[34578]\d{9}$',mobile):
		return jsonify(errno=RET.PARAMERR, errmsg='手机号码错误')
	# 从redis中获取图片验证码校验
	try:
		image_code = redis_storage.get('imageCode:%s' %img_code_id)
	except Exception as e:
		current_app.logger.error(e)
		return jsonify(errno=RET.DBERR, errmsg='查询redis中图片验证码信息失败')
	# 判断验证码是否存在
	if not image_code:
		return jsonify(errno=RET.NODATA, errmsg='没有找到图片验证码')
	#判断验证码是否匹配
	if image_code.lower() != img_code.lower():
		return jsonify(errno=RET.DATAERR, errmsg='输入的验证码不一致')
	#生成短信验证码
	sms_code = "%06d"%random.randint(1,9999)
	current_app.logger.info("短信验证码为:"+sms_code)
	#使用第三方云通讯发送短信验证码
	try:
		# SendSms().send_sms(mobile,[sms_code,constants.SMS_CODE_REDIS_EXPIRES/60],1)
		pass
	except Exception as e:
		current_app.logger.error(e)
		return jsonify(errno=RET.THIRDERR, errmsg='发送短信验证码失败')
	#将短信验证码保存到redis中,表单提交时验证
	try:
		redis_storage.set('mobile:%s'%mobile,sms_code,constants.SMS_CODE_REDIS_EXPIRES)
	except Exception as e:
		current_app.logger.error(e)
		return jsonify(errno=RET.DBERR, errmsg='短信验证码存储失败')
	# 返回响应
	return jsonify(errno=RET.OK, errmsg='ok')





