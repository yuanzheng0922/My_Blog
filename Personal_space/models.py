# -*- coding: utf-8 -*-
# @Author : yz
# @Time   : 2018/4/28-21:42
from . import db
from werkzeug.security import generate_password_hash, check_password_hash


class User(object):
	'''用户表'''
	__tablename__ = 'user'
	id = db.Column(db.Integer, primary_key=True)  # 用户id
	name = db.Column(db.String(32), unique=True, nullable=False)  # 用户name
	password_hash = db.Column(db.Integer, unique=True, nullable=False)  # 用户密码加密
	mobile = db.Column(db.Integer, unique=True, nullable=False)  # 电话号码
	real_name = db.Column(db.String(32))  # 真实姓名
	id_card = db.Column(db.String(20))  # 身份证号
	avatar_url = db.Column(db.String(256))  # 用户头像
	pics = db.relationship('Photo',backref='user') #用户相册
	arts = db.relationship('Article',backref='user') # 用户文章


	@property
	def passwd(self):
		return AttributeError('不能读取密码')

	@passwd.setter
	def passwd(self, value):
		"""将密码加密并保存"""
		self.password_hash = generate_password_hash(value)

	def check_password(self,pwd):
		"""验证用户密码"""
		return check_password_hash(self.password_hash,pwd)


	def to_dict(self):
		resp = {
			'user_id': self.id,
			'user_name': self.name,
			'user_pwd': self.password_hash,
			'user_mobile': self.mobile,
			'user_avatar_url': self.avatar_url,
			'real_name':self.real_name,
			'id_card':self.id_card
		}
		return resp


class Photo(object):
	'''相册'''
	__tablename__ = 'pic'
	id = db.Column(db.Integer, primary_key=True)
	title = db.Column(db.String(32), unique=True, nullable=False) #标题
	img_url = db.Column(db.String(256)) #图片地址
	user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

	def to_dict(self):
		resp={
			'pic_id':self.id,
			'img_url':self.img_url,
		}
		return resp

class Article(object):
	'''文章'''
	__tablename__ = 'article'
	id = db.Column(db.Integer, primary_key=True)
	content = db.Column(db.String(2048)) #文章
	user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

	def to_dict(self):
		resp={
			'art_id':self.id,
			'content':self.content,
		}
		return resp

