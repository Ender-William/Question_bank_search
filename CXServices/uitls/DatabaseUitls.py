#用于操作数据库
import pymysql as pysql
import traceback

Host = "xxx.xxx.xxx.xxx"    #IP 地址
Port = 3306                 #端口号
UserName = "username"       #用户名
PassWord = "passwd"         #密码
DBName = "Database"         #数据库名称


def LoginProcess():
    conn = pysql.connect(host=Host, port=Port, db=DBName,
                         user=UserName, password=PassWord)
    return conn

def Check(arg,key,til):
    """
    :param arg: 要显示的字段
    :param key: 要查询的字段（只能有一个）
    :param til: 被查询的表头数值
    :return: 返回一个Json格式的数据
    """
    try:
        conn = LoginProcess()
        cursor = conn.cursor(pysql.cursors.DictCursor)
        SqlSet = "select " + arg +" from QATab where " + key + " = \'" + til + "\' ;"
        cursor.execute(SqlSet)
        data = cursor.fetchone()
        cursor.close()
        conn.close()
        return data
    except:
        return traceback.print_exc()

def CheckBre(arg,key,til):
    """
    模糊搜索
    :param arg: 要显示的字段
    :param key: 要查询的字段（只能有一个）
    :param til: 被查询的表头数值
    :return: 返回一个Json格式的数据
    """
    try:
        conn = LoginProcess()
        cursor = conn.cursor(pysql.cursors.DictCursor)
        SqlSet = "select " + arg +" from QATab where " + key + " like \'%" + til + "%\' ;"
        cursor.execute(SqlSet)
        data = cursor.fetchall()
        cursor.close()
        conn.close()
        return data
    except:
        return traceback.print_exc()

def CheckAll(key,til):
    """
    :param key: 要查询的字段（只能有一个）
    :param til: 被查询的表头数值
    :return: 返回一个Json格式的数据
    """
    try:
        conn = LoginProcess()
        cursor = conn.cursor(pysql.cursors.DictCursor)
        SqlSet = "select * from QATab where " + key + " = \'" + til + "\' ;"
        cursor.execute(SqlSet)
        data = cursor.fetchone()
        cursor.close()
        conn.close()
        return data
    except:
        return traceback.print_exc()

def Insert(title,anser):
    """
    :param title: 题目
    :param anser: 答案
    :return: 返回执行状态
    """
    try:
        conn = LoginProcess()
        cursor = conn.cursor(pysql.cursors.DictCursor)
        SqlSet_CheckRows = "SELECT count(*) from QATab"
        cursor.execute(SqlSet_CheckRows)
        Rows = str(int(str(cursor.fetchone()).split(":")[1].split("}")[0]) + 1)
        print(Rows)
        SqlSet_Insert = "INSERT INTO QATab(title,ans,id) VALUES ('%s','%s','%s')" % (title,anser,Rows)
        cursor = conn.cursor(pysql.cursors.DictCursor)
        cursor.execute(SqlSet_Insert)
        conn.commit()
        cursor.close()
        conn.close()
        result = CheckAll("id",Rows)
        return result
    except:
        return traceback.print_exc()


# # print(Insert("TEST2","TEST2"))
# for item in CheckBre("*","title","TEST"):
#     print(item)

