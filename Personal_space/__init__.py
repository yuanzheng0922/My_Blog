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

db = SQLAlchemy()
redis_storage = None

def create_app(config_name):
	config_cls = config_dict[config_name]
	# 创建app
	app = Flask(__name__,)

	# 添加配置类
	app.config.from_object(config_cls)
	app.url_map.converters['re']=RouteConverter

	# 创建数据库关系映射对象
	db.init_app(app)
	# 创建redis对象
	global redis_storage
	redis_storage = redis.StrictRedis(host=config_cls.REDIS_IP, port=config_cls.REDIS_PORT)
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
