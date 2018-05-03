# -*- coding: utf-8 -*-
# @Author : yz
# @Time   : 2018/4/28-21:50

from flask import Blueprint

api = Blueprint('blog',__name__,static_url_path='/static/html')

from . import index,vertify,register,profile,picture