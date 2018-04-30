# -*- coding: utf-8 -*-
# @Author : yz
# @Time   : 2018/4/29-14:53
from werkzeug.routing import BaseConverter
from flask import session,g,jsonify
from Personal_space.response_code import RET
import functools

# 自定义路由转换器
class RouteConverter(BaseConverter):
	"""自定义路由转换器"""
	def __init__(self,url_map,regex):
		super(RouteConverter, self).__init__(url_map)
		#保存路由转换规则
		self.regex = regex



def login_required(func):
	@functools.wraps(func)
	def inner(*args,**kwargs):
		# session中获取user_id
		user_id = session.get('user_id')
		if user_id:
			# 设置g变量
			g.user_id = user_id
			return func(*args,**kwargs)
		else:
			return jsonify(errno=RET.LOGINERR, errmsg='用户没有登陆')
	return inner




