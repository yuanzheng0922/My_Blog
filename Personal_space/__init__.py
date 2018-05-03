# -*- coding: utf-8 -*-
# @Author : yz
# @Time   : 2018/4/28-21:41

from flask import Flask, session
import redis
import pymysql
pymysql.install_as_MySQLdb()
from flask_session import Session
from flask_wtf import CSRFProtect
from flask_sqlalchemy import SQLAlchemy
from config import config_dict
from utils.commons import RouteConverter

import logging
from logging.handlers import RotatingFileHandler

def set_log_level(level_name):
	"""设置log等级函数"""
	# 设置日志的记录等级
	logging.basicConfig(level=level_name)  # 调试debug级
	# 创建日志记录器，指明日志保存的路径、每个日志文件的最大大小、保存的日志文件个数上限
	file_log_handler = RotatingFileHandler("logs/log", maxBytes=1024*1024*100, backupCount=10)
	# 创建日志记录的格式                 日志等级    输入日志信息的文件名 行数    日志信息
	formatter = logging.Formatter('%(levelname)s %(filename)s:%(lineno)d %(message)s')
	# 为刚创建的日志记录器设置日志记录格式
	file_log_handler.setFormatter(formatter)
	# 为全局的日志工具对象（flask app使用的）添加日志记录器
	logging.getLogger().addHandler(file_log_handler)


db = SQLAlchemy()
redis_storage = None

def create_app(config_name):
	config_cls = config_dict[config_name]
	# 创建app
	app = Flask(__name__,)

	# 添加配置类
	app.config.from_object(config_cls)
	app.url_map.converters['re']=RouteConverter
	# 调用日志函数设置log等级
	# set_log_level(config_cls.LOG_LEVEL)
	# 创建数据库关系映射对象
	db.init_app(app)
	# 创建redis对象
	global redis_storage
	redis_storage = redis.StrictRedis(host=config_cls.REDIS_IP, port=config_cls.REDIS_PORT,db=1)
	# session存储
	Session(app)
	# csrf防护
	CSRFProtect(app)

	#注册api接口蓝图
	from Personal_space.api import api
	app.register_blueprint(api,url_prefix='/api/v1.0')
	#注册html接口蓝图
	from Personal_space.web_html import html
	app.register_blueprint(html)

	return app
