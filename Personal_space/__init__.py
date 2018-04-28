# -*- coding: utf-8 -*-
# @Author : yz
# @Time   : 2018/4/28-21:41
from flask import Flask, session
from flask_session import Session
import redis
import pymysql
from config import config_dict
pymysql.install_as_MySQLdb()
from flask_wtf import CSRFProtect
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()
redis_storage = None

def create_app(config_name):
	config_cls = config_dict[config_name]
	# 创建app
	app = Flask(__name__)

	# 添加配置类
	app.config.from_object(config_cls)

	# 创建数据库关系映射对象
	db.init_app(app)
	# 创建redis对象
	global redis_storage
	redis_storage = redis.StrictRedis(host=config_cls.REDIS_IP, port=config_cls.REDIS_PORT)
	# session存储
	Session(app)
	# csrf防护
	CSRFProtect(app)

	#注册蓝图
	from Personal_space.api import api
	app.register_blueprint(api,url_prefix='/api/v1.0')

	return app
