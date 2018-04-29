# -*- coding: utf-8 -*-
# @Author : yz
# @Time   : 2018/4/29-11:20

from flask import Blueprint
from flask import current_app,make_response
from flask_wtf.csrf import generate_csrf

html = Blueprint('web_html', __name__,)


@html.route('/<re(".*"):file_name>')
def web(file_name):
	"""web访问html"""
	#判断url地址,为空跳转到index页面
	if file_name == "":
		file_name = 'index.html'
	# title logo设置
	if file_name !='favicon.ico':
		# 拼接url地址
		file_name='html/'+file_name
	#设置csrf_token
	response = make_response(current_app.send_static_file(file_name))
	response.set_cookie('csrf_token',generate_csrf())
	return response
