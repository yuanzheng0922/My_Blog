# -*- coding: utf-8 -*-
# @Author : yz
# @Time   : 2018/4/28-20:14
from Personal_space import db,create_app
from flask_migrate import MigrateCommand, Manager, Migrate

app = create_app('Development_Env')
# 创建对象
Migrate(app, db)
manager = Manager(app)
# 添加数据库迁移命令
manager.add_command('db', MigrateCommand)



if __name__ == '__main__':
	# print app.url_map
	#启动程序入口
	manager.run()
