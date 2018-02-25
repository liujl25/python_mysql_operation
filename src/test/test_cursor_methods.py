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

sql = "select * from python"
cursor.execute(sql)

print(cursor.rowcount)

rs = cursor.fetchone()  #输出一条
print(rs)

rs = cursor.fetchmany(3)    #获取三条，从第二条开始 2、3、4
print(rs)

rs = cursor.fetchall()  #第四条后的 5...
print(rs)

cursor.close()
conn.close()