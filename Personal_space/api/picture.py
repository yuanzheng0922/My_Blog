# -*- coding: utf-8 -*-
# @Author : yz
# @Time   : 2018/5/4-0:46
from . import api

@api.route('/pics',methods=["POST"])
def upload_pic():
    """图片上传处理"""

