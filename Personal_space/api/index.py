# -*- coding: utf-8 -*-
# @Author : yz
# @Time   : 2018/4/28-23:50
from . import api


@api.route('/')
def index():
	# session['name'] = 'value'  # 测试session
	# from Personal_space import redis_storage
	# redis_storage.set('hahaha','gogogo')  # 测试redis存储
	return 'hello world'

# import random
# print '%06d'%random.randint(1,9999)

# class A(object):
# 	__num = False
# 	def __new__(cls, *args, **kwargs):
# 		if not hasattr(cls,'_isinstance'):
# 			obj = object.__new__(cls,*args, **kwargs)
# 			cls._isinstance = obj
# 		return cls._isinstance
#
# 	def __init__(self,num):
# 		if self.__num == False:
# 			self.num = num
# 			self.__num = True
#
# a = A(3)
# # a.num = 1
# print a.num
# print id(a)
#
# b = A(9)
# # b.num = 2
# print b.num
# print id(b)
#
# a = 555
# print id(a)
# print id(555)
# b=a
# print id(b)
# class A(object):
# 	pass
#
# a = A()
# a.num = 1
# print a.num
#
