# -*- coding: utf-8 -*-
# @Author : yz
# @Time   : 2018/4/29-1:59
from . import api
from flask import request, jsonify, current_app
from Personal_space.response_code import RET
from Personal_space.models import *
import re


@api.route('/form_user', methods=["POST"])
def register():
	"""用户注册,表单提交处理"""
	'''
	接收参数,进行校验,手机号,密码,用户名设置为手机号
	保存数据到数据库
	返回响应
	:return: 
	'''
	# 接收参数
	resp = request.json
	mobile = resp.get('mobile')
	password = resp.get('password')
	rpassword = resp.get('rpassword')
	# 判断密码是否输入
	if not all([password, rpassword]):
		return jsonify(errno=RET.PARAMERR, errmsg='请核对密码')
	# 判断密码是否一致
	if password != rpassword:
		return jsonify(errno=RET.PWDERR, errmsg='二次密码不一致')

	# 创建数据库对象
	user = User()
	# 保存数据到数据库
	user.name = mobile
	user.mobile = mobile
	user.passwd = password
	try:
		db.session.add(user)
		db.session.commit()
	except Exception as e:
		current_app.logger.error(e)
		return jsonify(errno=RET.DBERR, errmsg='保存用户到数据库失败')

	return jsonify(errno=RET.OK, errmsg='OK')


@api.route('/users',methods=["POST"])
def login():
	"""用户登陆"""
	# 接收数据
	resp = request.json
	mobile = resp.get('mobile')
	passwd = resp.get('passwd')
	#判断有效性
	if not all([mobile,passwd]):
		return jsonify(errno=RET.PARAMERR, errmsg='参数有误')
	if not re.match(r'^1[35789]\d{9}$',mobile):
		return jsonify(errno=RET.DATAERR, errmsg='手机号格式不对')
	# 查询数据库
	try:
		user = User.query.filter(User.mobile == mobile).first()
	except Exception as e:
		current_app.logger.error(e)
		return jsonify(errno=RET.DBERR, errmsg='查询数据库失败')
	#判断用户是否存在
	if not user:
		return jsonify(errno=RET.NODATA, errmsg='手机号不存在,请立即注册')
	#判断密码
	if not user.check_password(passwd):
		return jsonify(errno=RET.PWDERR, errmsg='密码错误')

	#返回响应
	return jsonify(errno=RET.OK, errmsg='登陆成功')


@api.route('/hello')
def hello():
    return 'hello'
