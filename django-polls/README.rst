============
Polls
============
polls 是个简单的示例程序


Quick Start
------------
1.增加“polls”到你的 INSTALLED_APPS setting 如下：
 INSTALLLED_APPS=[
 ...
 'polls',
 ]
 2.把这个polls URLconf 写入你的项目的url.py如下：
 path('polls/',include('polls.urls'))
 3.运行 python manage.py migrate 创建数据库
 4.运行调试服务器并访问 http://127.0.0.1:8000/admin/
     需要登记相关表
 5.访问访问 http://127.0.0.1:8000/polls/

