新建Django项目

![1526987726133](C:\Users\Lenovo\AppData\Local\Temp\1526987726133.png)



python -m pip install --upgrade pip    更新pip

![1526987974658](C:\Users\Lenovo\AppData\Local\Temp\1526987974658.png)

查看django版本    现在可能用的多的是1.1.1版本 

![1526988109296](C:\Users\Lenovo\AppData\Local\Temp\1526988109296.png)

django1.1.1版本里面不叫path 而是url函数

![1526988284529](C:\Users\Lenovo\AppData\Local\Temp\1526988284529.png)

启服务：

![1526988642676](C:\Users\Lenovo\AppData\Local\Temp\1526988642676.png)

浏览器输入locallhost:80可以访问

![1526988613011](C:\Users\Lenovo\AppData\Local\Temp\1526988613011.png)

如果直接执行命令   python manage.py runserver   会默认开启8000端口

![1526988740498](C:\Users\Lenovo\AppData\Local\Temp\1526988740498.png)

ps：端口号作用是区分是哪个服务，  ip地址区分主机



首先更改语言配置：

![1526989101775](C:\Users\Lenovo\AppData\Local\Temp\1526989101775.png)

```
下面这个
STATIC_URL = '/static/'
#static静态资源的前缀，所有静态文件都在这，
统一资源定位符，这里是两个斜杠，表示路径，不能写错了
```



所以接下来要新建一个static文件![1526989449937](C:\Users\Lenovo\AppData\Local\Temp\1526989449937.png)

添加静态资源文件目录（这是个列表，可以配多个路径）：

![1526989915602](C:\Users\Lenovo\AppData\Local\Temp\1526989915602.png)

为了创建一个首页，先加载图片

![1526990227614](C:\Users\Lenovo\AppData\Local\Temp\1526990227614.png)



再创建一个应用hrs

![1526990338323](C:\Users\Lenovo\AppData\Local\Temp\1526990338323.png)

创建一个试图，写入函数

![1526990609217](C:\Users\Lenovo\AppData\Local\Temp\1526990609217.png)

创建视图：

在应用hrs下面的views视图里面写入path('',views.index),

这是告诉在我的views里面有一个index的函数

![1526990762109](C:\Users\Lenovo\AppData\Local\Temp\1526990762109.png)

注册应用

![1526991077389](C:\Users\Lenovo\AppData\Local\Temp\1526991077389.png)



现在 在Terminal里面执行运行命令就可以在浏览器看到首页图片了：

python manage.py runserver

![1526991196775](C:\Users\Lenovo\AppData\Local\Temp\1526991196775.png)

ps:

{% load static %} 这是加载静态资源 

凡是要使用静态资源的地方就 加上:     static +"资源名字"

ex:

{% load static %}<img src="{% static "my_app/example.jpg" %}" alt="My image"/>

接下来我们就用这种做法，把index.html文件里的改了，运行python manage.py runserver 一样可以看到效果

![1526992098427](C:\Users\Lenovo\AppData\Local\Temp\1526992098427.png)

这样就是相对路径了，不再是绝对路径

![1526992230057](C:\Users\Lenovo\AppData\Local\Temp\1526992230057.png)





写占位符

![1526992521940](C:\Users\Lenovo\AppData\Local\Temp\1526992521940.png)

传入h1标签里面的东西，要在应用里面的views里面传：

![1526992642115](C:\Users\Lenovo\AppData\Local\Temp\1526992642115.png)



动态页面来自于持久化系统，做数据持久化可以用关系型持久化和非关系型数据库。如果用关系型数据库，将来加载数据都是从关系型数据库去加载数据。



![1526993167329](C:\Users\Lenovo\AppData\Local\Temp\1526993167329.png)



在系统命令下启动mysql:

![1526993275213](C:\Users\Lenovo\AppData\Local\Temp\1526993275213.png)

新建数据库：

在Navicat下打开MySQL连接，可以右键新建数据库新建数据库名oa 字符集utf8 或者命令创建数据库

![1526993643285](C:\Users\Lenovo\AppData\Local\Temp\1526993643285.png)



连接数据库 ，运行python manage.py runserver  如果不报错就连接成功了

![1526993913429](C:\Users\Lenovo\AppData\Local\Temp\1526993913429.png)

但是会报向下面这样的错：因为还没有装依赖库



![1526993996810](C:\Users\Lenovo\AppData\Local\Temp\1526993996810.png)

pip install pymysql  安装依赖库

这里要注意pymysql 和mysql不一样

所以我们要写入下面：

![1526994188222](C:\Users\Lenovo\AppData\Local\Temp\1526994188222.png)

这样做是把pymysql当作mysqldb来用，这样就和mysqldb接口一样

再运行命令看看有没问题

![1526994523987](C:\Users\Lenovo\AppData\Local\Temp\1526994523987.png)

这里是提示有14个迁移项没有迁移

执行命令：

python manage.py migrate

会出现很多okokok,然后我们来看MySQL下面的oa里面的表：（这些都是自动创建的表）

![1527001734329](C:\Users\Lenovo\AppData\Local\Temp\1527001734329.png)



这个和mysql关系：

ORM   --  对象关系映射

对象模型 <---> 关系模型

实体类 <---> 二维表

属性    <---> 列

对象    <----> 记录

注意注意！！！**实际开发中：我们一般用2个一对多去取代多对多！！！   一般ForeignKey就够用了**

![1527003085134](C:\Users\Lenovo\AppData\Local\Temp\1527003085134.png)

python manage.py makemigrations hrs  

会看到下面这样的报错

![1527003245200](C:\Users\Lenovo\AppData\Local\Temp\1527003245200.png)![1527003313763](C:\Users\Lenovo\AppData\Local\Temp\1527003313763.png)

总共有多少为数字7，和小数点2为设置

接下来执行

python manage.py makemigrations hrs

![1527003371838](C:\Users\Lenovo\AppData\Local\Temp\1527003371838.png)

再数据迁移：python manage.py migrate

![1527003445180](C:\Users\Lenovo\AppData\Local\Temp\1527003445180.png)

这样mysql里面就多了两个表

![1527003660582](C:\Users\Lenovo\AppData\Local\Temp\1527003660582.png)

重新改表命就要在类里面写类，写脚本：

![1527004029767](C:\Users\Lenovo\AppData\Local\Temp\1527004029767.png)

python manage.py migrate    迁移

在MySQL里面刷新表看更改成功没

这里要提醒以下，如果把刚刚两个表手动删除了，还要把下面这条迁移记录删了，才能正常操作其他的

![1527004206065](C:\Users\Lenovo\AppData\Local\Temp\1527004206065.png)





![1527004826535](C:\Users\Lenovo\AppData\Local\Temp\1527004826535.png)![1527004909672](C:\Users\Lenovo\AppData\Local\Temp\1527004909672.png)

如需重新迁移，就删除迁移记录，重新迁移，重新执行下面命令即可：

python manage.py makemigrations

python manage.py migrate



进入Django管理员平台：

先创建超级用户

python manage.py createsuperuser

账号admin

设置密码

![1527005519480](C:\Users\Lenovo\AppData\Local\Temp\1527005519480.png)



起来服务器命令后

浏览器打开输入刚刚账号密码

![1527005683327](C:\Users\Lenovo\AppData\Local\Temp\1527005683327.png)

然后模型注册

![1527005801601](C:\Users\Lenovo\AppData\Local\Temp\1527005801601.png)





然后刷新页面

点击添加后可以看到

![1527005994695](C:\Users\Lenovo\AppData\Local\Temp\1527005994695.png)

![1527006017948](C:\Users\Lenovo\AppData\Local\Temp\1527006017948.png)

这个都是管理员的网页，不是给用户的展示页面哦





接下来我们要在

http://127.0.0.1:8000/hrs/depts 这个网页下看到所有部门展示出来



先映射URL

新建一个dept.html文件写入显示内容

![1527006791773](C:\Users\Lenovo\AppData\Local\Temp\1527006791773.png)

创建视图拿对象拿结果

![1527007028915](C:\Users\Lenovo\AppData\Local\Temp\1527007028915.png)

![1527007087182](C:\Users\Lenovo\AppData\Local\Temp\1527007087182.png)

运行服务后浏览器可以看见，也可以在管理页面进行增加部门信息

![1527007155070](C:\Users\Lenovo\AppData\Local\Temp\1527007155070.png)



把下面改成中文的：

![1527007618788](C:\Users\Lenovo\AppData\Local\Temp\1527007618788.png)

![1527007739320](C:\Users\Lenovo\AppData\Local\Temp\1527007739320.png)

![1527007763179](C:\Users\Lenovo\AppData\Local\Temp\1527007763179.png)



![1527007778671](C:\Users\Lenovo\AppData\Local\Temp\1527007778671.png)在增加人员信息时可以设置不赋值栏：

![1527007886532](C:\Users\Lenovo\AppData\Local\Temp\1527007886532.png)

![1527007965392](C:\Users\Lenovo\AppData\Local\Temp\1527007965392.png)





在页面显示更多

![1527008157038](C:\Users\Lenovo\AppData\Local\Temp\1527008157038.png)

list_display是显示的内容：可以进行增删

![1527008113096](C:\Users\Lenovo\AppData\Local\Temp\1527008113096.png)

刷新页面进入Depts

![1527008137672](C:\Users\Lenovo\AppData\Local\Temp\1527008137672.png)