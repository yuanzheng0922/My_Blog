# -*- coding: utf-8 -*-
# @Author : yz
# @Time   : 2018/4/30-13:24
from . import api

@api.route('/user_avatar',methods=['POST'])
def upload_user_avatar():
    """上传个人头像"""
