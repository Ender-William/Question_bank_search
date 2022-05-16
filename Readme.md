[TOC]

# 1.关于自建题库

这个是我在空闲时间里用来练手的一个项目，利用一晚上的时间，利用从未接触过的框架完成一些简单的应用操作。

可以完成题目的录入，精细查询和模糊查询。

使用Python Flask作为后端进行数据的操作。

整体项目结构如下：

```
CXProject					#项目文件夹
|Readme.md					#说明文件
|app.py						#flask起始文件，包含路由
|requirement.txt			#环境配置文件
|QATab.sql					#MySQL数据库表结构文件
|venv						#环境
|templates					#动态页面文件夹
|	|BRSearch.html			#操作页面
|
|CXServices					#数据库操作相关服务
	|cxservice_index.py		#业务选择
	|uitls					#工具类程序
	 	|DatabaseUitls.py	#数据库操作程序
		|Uitls.py			#其他工具程序
```



# 2.参与开发

## 2.1 环境

- Pycharm
- conda
- Python 3.8 或 Python 3.9
- MySQL 8.x

## 2.2 新建数据库

需要现在MySQL里新建一个数据库。

之后使用Navicat或其他数据库可视化工具，运行`QATab.sql`文件新建数据表。

- title：题目
- ans：答案
- id：题目编号

![Screen Shot 2022-05-16 at 08.30.56](https://raw.githubusercontent.com/Ender-William/Question_bank_search/main/Readme.assets/Screen%20Shot%202022-05-16%20at%2008.30.56.png)

## 2.3 修改配置文件

修改`DatabaseUitls.py`中的数据库配置信息

```python
Host = "xxx.xxx.xxx.xxx"    #IP 地址
Port = 3306                 #端口号
UserName = "username"       #用户名
PassWord = "passwd"         #密码
DBName = "Database"         #数据库名称
```

## 2.4 贡献流程

1. Fork

2. Pull Request，简要描述更改的内容

3. CI检查通过

4. CodeReview

5. 合并到项目仓库

    

------

# 3.题库界面展示

## 3.1 运行

![Screen Shot 2022-05-16 at 08.35.13](https://github.com/Ender-William/Question_bank_search/raw/main/Readme.assets/Screen%20Shot%202022-05-16%20at%2008.35.13.png)

在`app.py`中，右键运行。

![Screen Shot 2022-05-16 at 08.36.26](https://github.com/Ender-William/Question_bank_search/raw/main/Readme.assets/Screen%20Shot%202022-05-16%20at%2008.36.26.png)

可以看见运行在`5000`端口。

## 3.2 搜索界面展示

界面默认选择为模糊搜索页面

![Screen Shot 2022-05-16 at 08.40.39](https://github.com/Ender-William/Question_bank_search/raw/main/Readme.assets/Screen%20Shot%202022-05-16%20at%2008.40.39.png)

通过按钮选择模式

如果有多条结果，则显示多条信息，例如搜索`计算机`:

![Screen Shot 2022-05-16 at 08.41.34](https://github.com/Ender-William/Question_bank_search/raw/main/Readme.assets/Screen%20Shot%202022-05-16%20at%2008.41.34.png)

## 3.3 录入界面

这个项目不包含题库部分，题库需要自行录入，答案在答题结束后会出现

![Screen Shot 2022-05-16 at 08.42.42](https://github.com/Ender-William/Question_bank_search/raw/main/Readme.assets/Screen%20Shot%202022-05-16%20at%2008.42.42-2661766.png)

![Screen Shot 2022-05-16 at 08.43.04](https://github.com/Ender-William/Question_bank_search/raw/main/Readme.assets/Screen%20Shot%202022-05-16%20at%2008.43.04.png)

提交后，会出现`Success Insert`信息，并反馈一个提交成功的时间戳。

![Screen Shot 2022-05-16 at 08.44.08](https://github.com/Ender-William/Question_bank_search/raw/main/Readme.assets/Screen%20Shot%202022-05-16%20at%2008.44.08.png)

数据库中有显示。

# 4. 免责声明

项目完全开源，仅供学习参考使用，自建题库分享需咨询题目原版权方，本人从未提供题库内容。请用于学习内容，考试时禁止使用自建题库进行作弊行为，要建设良好的学习与考试氛围。

