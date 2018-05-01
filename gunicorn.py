# -*- coding: utf-8 -*-
# @Author : yz
# @Time   : 2018/5/1-2:11


# 指定web服务器监听的ip和端口号
bind = "0.0.0.0:8000"
# 指定工作进程数
workers = 1
# 指定服务器后台运行
daemon = True
# 启动服务器之后生成gunicorn.pid, 保存主进程id
pidfile = 'gunicorn.pid'
# 启动服务器之后生成access.log, 保存访问日志信息
# accesslog = 'access.log'
# 启动服务器之后生成error.log, 保存错误日志信息
# errorlog = 'error.log'
