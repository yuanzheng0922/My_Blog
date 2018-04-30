# -*- coding: utf-8 -*-
# @Author : yz
# @Time   : 2018/4/30-13:24
from . import api
from Personal_space.utils.qiniuyun import upload_img
from flask import session, current_app, jsonify, g, json, request
from Personal_space.models import *
from Personal_space.response_code import RET
from Personal_space.utils.commons import login_required
from Personal_space.utils.qiniuyun import upload_img
from Personal_space import constants


@api.route('/users_info')
@login_required
def get_user_info():
	"""获取个人信息"""
	# 判断用户是否登陆
	# user_id = session.get('user_id')
	current_app.logger.info('当前用户id:%s' % g.user_id)
	# 数据库获取用户信息
	try:
		user = User.query.get(g.user_id)
	except Exception as e:
		current_app.logger.error(e)
		return jsonify(errno=RET.DBERR, errmsg='查询数据库失败')
	if not user:
		return jsonify(errno=RET.USERERR, errmsg='用户不存在')
	# 组织数据
	# 返回响应
	return jsonify(errno=RET.OK, errmsg='OK', data=user.user_to_dict())


@api.route('/users_info', methods=['PUT'])
@login_required
def update_user_name():
	"""更改用户名信息"""
	resp_dict = request.json
	user_name = resp_dict.get('user_name')
	# 查询数据库获取用户姓名
	try:
		user_name_count = User.query.filter(User.name == user_name, User.id != g.user_id).count()
	except Exception as e:
		current_app.logger.error(e)
		return jsonify(errno=RET.DBERR, errmsg='数据库查询用户名失败')
	if user_name_count > 0:
		return jsonify(errno=RET.DATAEXIST, errmsg='用户名已经存在')

	# 创建用户对象
	try:
		user = User.query.get(g.user_id)
		user.name = user_name
	except Exception as e:
		current_app.logger.error(e)
		return jsonify(errno=RET.DBERR, errmsg='更新用户名到数据库失败')
	# 保存到数据库
	try:
		db.session.commit()
	except Exception as e:
		current_app.logger.error(e)
		return jsonify(errno=RET.DBERR, errmsg='保存数据到数据库失败')
	return jsonify(errno=RET.OK, errmsg='OK', data={"user_name": user_name})


@api.route('/users_info', methods=['POST'])
@login_required
def upload_user_avatar():
	"""上传个人头像"""
	# 接收表单提交的图片信息
	user_file = request.files.get('avatar')
	if not user_file:
		return jsonify(errno=RET.NODATA, errmsg='没有上传文件')
	# 上传头像到七牛云
	try:
		key = upload_img(user_file)
	except Exception as e:
		current_app.logger.error(e)
		return jsonify(errno=RET.THIRDERR, errmsg='上传头像到七牛云失败')
	print key
	# 获取当前登陆用户的对象
	try:
		user = User.query.get(g.user_id)
	except Exception as e:
		current_app.logger.error(e)
		return jsonify(errno=RET.DBERR, errmsg='数据库读取用户失败')
	if not user:
		return jsonify(errno=RET.SESSIONERR, errmsg='用户未登录')
	user.avatar_url = key
	# 保存用户头像url地址信息到数据库
	try:
		db.session.commit()
	except Exception as e:
		current_app.logger.error(e)
		return jsonify(errno=RET.DBERR, errmsg='保存头像url失败')

	return jsonify(errno=RET.OK, errmsg='OK', data=user.user_to_dict())


@api.route('/auth_users', methods=["POST"])
@login_required
def user_auth():
	"""用户认证"""
	resp_dict = request.json
	real_name = resp_dict.get('real_name')
	id_card = resp_dict.get('id_card')
	# 校验参数
	if not all([real_name, id_card]):
		return jsonify(errno=RET.PARAMERR, errmsg='参数错误')

	# 对比参数与数据库数据,如果存在则用户注册过
	try:
		id_count = User.query.filter(User.id_card == id_card).first()
	except Exception as e:
		current_app.logger.error(e)
		return jsonify(errno=RET.DBERR, errmsg='数据库查询错误')
	if id_count != None:
		return jsonify(errno=RET.DATAEXIST, errmsg='id已经认证过')
	# 查询数据库
	try:
		user = User.query.get(g.user_id)
	except Exception as e:
		current_app.logger.error(e)
		return jsonify(errno=RET.DBERR, errmsg='数据库查询用户信息失败')
	if not user:
		return jsonify(errno=RET.SESSIONERR, errmsg='用户登陆过期')
	# 保存用户认证的信息
	user.id_card = id_card
	user.real_name = real_name
	try:
		db.session.commit()
	except Exception as e:
		current_app.logger.error(e)
		return jsonify(errno=RET.DBERR, errmsg='保存用户信息失败')

	return jsonify(errno=RET.OK, errmsg='OK')


@api.route('/auth_users')
@login_required
def get_auth_user():
	"""检测使用认证信息"""
	try:
		user = User.query.get(g.user_id)
	except Exception as e:
		current_app.logger.error(e)
		return jsonify(errno=RET.DBERR, errmsg='查询用户失败')

	user_info = {
		"real_name": user.real_name,
		"id_card": user.id_card
	}
	return jsonify(errno=RET.OK, errmsg='OK', data=user_info)

@api.route('/auth_users',methods=["DELETE"])
@login_required
def user_logout():
	"""用户退出"""
	#删除session数据
	session.clear()
	return jsonify(errno=RET.OK, errmsg='OK')