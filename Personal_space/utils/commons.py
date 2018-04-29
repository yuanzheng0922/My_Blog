# -*- coding: utf-8 -*-
# @Author : yz
# @Time   : 2018/4/29-14:53
from werkzeug.routing import BaseConverter

# 自定义路由转换器
class RouteConverter(BaseConverter):
	"""自定义路由转换器"""
	def __init__(self,url_map,regex):
		super(RouteConverter, self).__init__(url_map)
		#保存路由转换规则
		self.regex = regex