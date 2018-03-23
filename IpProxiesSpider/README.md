# python
功能简介：
	爬取西刺免费代理IP网站中的代理服务器ip，
	将爬取到的所有ip做telnet测试检测是否可用，
	将可用的ip写入数据库。
	
	
文件：
	-
	--ConfigStruct 		存储数据对象文件夹
	    -DBHosts.py   		数据库对象文件
	--Json		   		配置文件夹
	    -db_hosts.json	数据库配置文件
	--Config.py			配置数据管理类
	--DB.py				数据库操作类
	--IPProxies.py		IP代理对象类
	--main.py			程序入口
	--Spider.py			爬虫类
	--Sqls.py			Sql语句的定义
	--TelnetTest.py		Telnet测试类
	--Urls.py			网站地址容器（存储待爬取的链接以及获取链接）
	--start_spider.bat	运行批处理文件（不通过pycharm运行该爬虫）
	

该项目的作用是为了以后的爬虫做准备，对于许多网站针对单次ip访问次数
过多导致的ip封锁提供了解决方案。为以后的爬虫提供对应的代理IP的支持。