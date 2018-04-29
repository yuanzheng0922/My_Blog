# -*- coding: utf-8 -*-
# @Author : yz
# @Time   : 2018/4/28-21:45
import os, base64
import redis


# 自定义配置文件
class Config(object):
	'''配置类'''
	SECRET_KEY = base64.b64encode(os.urandom(48))  # 使用base64 生成48位随机编码

	#常量
	REDIS_IP = '140.143.249.76'
	REDIS_PORT = 6379
	# 设置session配置项
	SESSION_TYPE = 'redis'  #数据库类型
	SESSION_KEY_PREFIX = 'session='  # redis存储前缀
	SESSION_REDIS = redis.StrictRedis(host=REDIS_IP, port=REDIS_PORT)
	SESSION_USE_SIGNER = True  # 签名加密
	PERMANENT_SESSION_LIFETIME = 60*60  #过期时间


	# 配置SQLALchemy
	SQLALCHEMY_DATABASE_URI = 'mysql://user:yuanzheng3@140.143.249.76:3306/blog'
	SQLALCHEMY_TRACK_MODIFICATIONS = False  # 不追踪

class Development_Env(Config):
	'''开发环境'''
	DEBUG = True


class Product_Env(Config):
	'''线上环境'''
	DEBUG = False

config_dict= {
	'Development_Env':Development_Env,
	'Product_Env':Product_Env
}

