# RhymeSearch 疯狂押韵
![RhymeSearch](https://github.com/Jezemy/ChineseRhymePhraseSearch/blob/master/pic/rhymeSearch.png?raw=true)

在线预览网站：[疯狂押韵 - 有一天你也能Freestyle](http://www.jezemy.cn/rhyme/)
注：网站可能在2020年9月失效，不一定会续期，若过期可以下载源码进行编译


# 制作初衷
一方面是作为本人数据库课程的设计作品，另一方面觉得有些押韵网站的押韵规则较多照搬百度百科上的古代押韵规则，已经过时，实际上使用起来匹配规则还不算好，比较常见错误比如：
- “存”cun 和“陈”chen 虽然韵母不同，但是实际上押韵
- “梦”meng 和 "碰" peng 虽然韵母相同，但是不押韵。因为“梦”字习惯读“mong”的音
-  “只”zhi 和 “机”ji 不押韵，但是和"四" si却押韵

因此结合自身的写词经历，将押韵规则做一些更细的划分，使得匹配结果更好些。

详细可以查看我的[中文押韵对应表](https://github.com/Jezemy/ChineseRhymeRules)

# 功能简单说明
-  可以根据输入的短语搜索到与其押韵的其他词语
-  支持双押，三押等多音节押韵
-  支持声调匹配约束
-  内含30w+的短语，足以满足基本需求。

# 缺陷与不足
- 数据比较杂乱，大多数词可能不会用得到，也有部分词比较冗余
- 由于是旧项目，重新启用后发现查询速度比较慢，暂不清楚是什么原因，与原始版本查询速度相比差距较大。想体验原来的速度可以进在线网站进行查看
- 后台记录好像出现一些未捕获的异常，不过还好不影响使用。

# 运行环境需求
- Python3
- Django

django2.1版本需要：
- 将本项目代码转移到2.1版本的django项目中
- pymysql 并且取消掉RhymeSearch/__init__.py下注释的代码

django3.0 版本需要:
- mysqldb

# 安装说明
### 1. 配置数据库
首先需要在RhymeSearch\setting.py内设置好连接数据库的方式，建议不改我的设置
```
DATABASES = {
    # 在这里设置你的mysql
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'RhymeSearch', # 数据库名
        'USER': 'root', # 用户名
        'PASSWORD': 'root', # 密码
        'HOST': 'localhost', # mysql服务器地址
        'PORT': '3306', #端口号
    }
}
```
### 2. 还原数据
登录mysql，然后在mysql中创建相同名的数据库，然后把db\rhymesearch.sql恢复到数据库中

### 3. 运行django项目
进入项目目录下（manage.py所在目录）,执行下列代码
```
python manage.py runserver
```
进入执行命令后显示的网站即可。

# 额外说明
本项目短时间内不会再继续更新，后续如若更新的话，有可能会增加新的东西

# 附图
![数据库表图](https://github.com/Jezemy/ChineseRhymePhraseSearch/blob/master/pic/tables.png?raw=true)

![预览图1](https://github.com/Jezemy/ChineseRhymePhraseSearch/blob/master/pic/display1.png?raw=true)

![预览图2](https://github.com/Jezemy/ChineseRhymePhraseSearch/blob/master/pic/display2.png?raw=true)
