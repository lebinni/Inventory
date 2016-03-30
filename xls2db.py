#!/usr/bin/python
# encoding=utf-8

'''
Created on 2013-4-2

@author: ting
'''
import os,sys,sqlite3,string 
from xlrd import open_workbook
import sqlite3
import types
import datetime 
import shutil

#获取脚本文件的当前路径
def cur_file_dir():
    #获取脚本路径
    path = sys.path[0]
    
    #判断为脚本文件还是py2exe编译后的文件，如果是脚本文件，则返回的是脚本的目录，如果是py2exe编译后的文件，则返回的是编译后的文件路径
    if os.path.isdir(path):
        return path
    elif os.path.isfile(path):
        return os.path.dirname(path)



def read_excel(sheet,str):
    # 判断有效sheet
    if sheet.nrows > 0 and sheet.ncols > 0:
        for row in range(1, sheet.nrows):
            row_data = []
            for col in range(sheet.ncols):
                data = sheet.cell(row, col).value
                # excel表格内容数据类型转换  float->int，unicode->utf-8
                #if type(data) is types.UnicodeType: data = data.encode("utf-8")
                #elif type(data) is types.FloatType: data = int(data)
                row_data.append(data)
            check_data_length(row_data,str)

# 检查row_data长度
def check_data_length(row_data,str):
    #if len(row_data) == 3:
    print row_data
    insert_sqlite(row_data,str)

def insert_sqlite(row_data,str):
    # 打开数据库（不存在时会创建数据库）
    
    #homedir = os.getcwd()
    #dbpath = homedir + "\MYDB1.DB"
    con = sqlite3.connect(cur_file_dir() + "\DataBak\DB_BAK\MYDB.DB")
    cur = con.cursor()
    try:
        #cur.execute("create table if not exists contacts(_id integer primary key "\
        #               "autoincrement,name text,age integer,number integer)")
        # 插入数据不要使用拼接字符串的方式，容易收到sql注入攻击
        #cur.execute("insert into inventory_inventory(InventoryId,ItemCode,Type_id,Vender_id,Color_id,Size_S,Size_M,Size_L,Size_XL,Size_2XL,Size_3XL,Size_4XL,Amount) values(?,?,?,?,?,?,?,?,?,?,?,?,?)", row_data)
        cur.execute(str,row_data)
        con.commit()
    except sqlite3.Error as e:
        print "An error occurred: %s", e.args[0]
    finally:
        cur.close
        con.close	

def xls2db():
	print "cur_file_dir: " + cur_file_dir()
	today = datetime.datetime.now()
	yesterday = today - datetime.timedelta(days=1)
	time = yesterday.strftime("%Y%m%d")
	#time = today.strftime("%Y%m%d")
	homedir = cur_file_dir()
	xlspath = homedir + '\DataBak\MYDB_' + time +'.xls'
	sourceFile = cur_file_dir() + "\DataBak\DB_BAK\MYDB_bak.DB"
	targetFile = os.path.dirname(sourceFile) + "\MYDB.DB"
	shutil.copy(sourceFile,targetFile)
	book = open_workbook(xlspath)
	str = ""
	i = 0 
	for sheet_name in book.sheet_names():
		if sheet_name == 'inventory_color':
			str = "insert into inventory_color values(?,?)"			
		elif sheet_name == 'inventory_inventory':
			str = "insert into inventory_inventory values(?,?,?,?,?,?,?,?,?,?,?,?,?)"
		elif sheet_name == 'inventory_type':
			str = "insert into inventory_type values(?,?)"
		elif sheet_name == 'inventory_vender':
			str = "insert into inventory_vender values(?,?)"
		else:
			print "The sheet %s do not exchange to DB" %sheet_name 
			
		print "The sheet %s will be exchange to DB" %sheet_name
		read_excel(book.sheets()[i],str)
		i +=1

	#for sheet in book.sheets():
	#	read_excel(sheet,str)
	sourceFile = cur_file_dir() + "\DataBak\DB_BAK\MYDB.DB"
	targetFile = cur_file_dir() + "\MYDB.DB"
	shutil.copy(sourceFile,targetFile)
	print "------ Done ------"

if __name__ == "__main__":
    # arg == database path
    xls2db()