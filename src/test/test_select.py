'''
Created on 2018年2月24日

@author: Administrator
'''
import pymysql

conn = pymysql.Connect(
                       host = 'localhost', #本地mysql地址
                       port = 3306,  #端口
                       user = 'root',   #用户名
                       passwd = 'root', #密码
                       db = 'test',   #数据库
                       charset = 'utf8' #字符
                       )

cursor = conn.cursor()   #获取游标对象

sql_insert = "insert into python values(10, 'name10')"
sql_update = "update python set username = 'myname' where userid=5"
sql_delete = "delete from python where userd<3" # userid

try:
    cursor.execute(sql_insert)
    print(cursor.rowcount)
    cursor.execute(sql_update)
    print(cursor.rowcount)
    cursor.execute(sql_delete)
    print(cursor.rowcount)

    conn.commit()       #提交
except Exception as e:
    print(e)
    conn.rollback       #回滚
    
cursor.close()
conn.close()