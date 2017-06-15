
目录结构：

|controller #存放控制器类
|models	    #存放概念/数据类
|pictures   #存放界面用的贴图
|views      #存放具体的界面类
每个目录又分main和servent两个子目录，分开放主从机的东西
|*.sql里面放建表语句

|M_database.py
|S_DBFacade.py
	两个类都接了数据库，需要更改库名用户名和密码，都有个实例化好了的游标cursor可以用，为了在并发访问的时候不出错，每次使用cursor之前先用一个已经实例化好了的互斥锁db_lock

|client和server分别是从机和主机的通信类，里面分别有c和server两个实例化的communication,要通信的时候先import c/server，然后调用相应的协议函数。

·另外，主机的入口是main.py，从机是S_main.py，分别运行即可开启主机和从机

