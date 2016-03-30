#!/usr/bin/python
# encoding=utf-8
import os,sys,sqlite3,string 
import datetime 
import sqlite3 as sqlite
from xlwt import *

#获取脚本文件的当前路径
def cur_file_dir():
     #获取脚本路径
     path = sys.path[0]
     #判断为脚本文件还是py2exe编译后的文件，如果是脚本文件，则返回的是脚本的目录，如果是py2exe编译后的文件，则返回的是编译后的文件路径
     if os.path.isdir(path):
         return path
     elif os.path.isfile(path):
         return os.path.dirname(path)

def sqlite_get_col_names(cur, table):
    query = 'select * from  %s' % table
    cur.execute(query)
    return [tuple[0] for tuple in cur.description]

def sqlite_query(cur,  table, col = '*', where = ''):
    if where != '':
        query = 'select %s from %s where %s' % (col, table, where)
        #print 'select %s from %s where %s' % (col, table, where)
    else:
        query = 'select %s from %s ' % (col, table)
        #print 'select %s from %s ' % (col, table) 
    cur.execute(query)

    return cur.fetchall()

def sqlite_to_workbook(cur, table, workbook):
    ws = workbook.add_sheet(table)
    print 'create table %s.'  % table
    for colx, heading in enumerate(sqlite_get_col_names(cur, table)):
            ws.write(0,colx, heading)
    for rowy,row in enumerate(sqlite_query(cur, table)):
        for colx, text in enumerate(row):
            ws.write(rowy+ 1, colx, text)

def db2xls():
    print "cur_file_dir: " + cur_file_dir()	
    now = datetime.datetime.now()
    time = now.strftime("%Y%m%d")
    homedir = cur_file_dir()
    dbpath = homedir + "\MYDB.DB"
    xlspath = homedir + '\DataBak\MYDB_' + time +'.xls'
    #xlspath = dbpath[0:dbpath.rfind('.')] + '_' + time +'.xls'
    if os.path.exists(xlspath):
		print r'%s exist' % xlspath
    else:
		print "<%s> --> <%s>"% (dbpath, xlspath)

		db = sqlite.connect(dbpath)
		cur = db.cursor()
		w = Workbook()
		tbl_names = ["inventory_color","inventory_inventory","inventory_type","inventory_vender"]
		for tbl_name in tbl_names:
			sqlite_to_workbook(cur,tbl_name, w)
		#tbl_name = tbl_names[3]
		#sqlite_to_workbook(cur,tbl_name, w)
		#tbl_name = "inventory_inventory"
		#sqlite_to_workbook(cur,tbl_name, w)
		#for tbl_name in [row[0] for row in sqlite_query(cur, 'sqlite_master', 'tbl_name', 'type = \'table\'')]:
		#    sqlite_to_workbook(cur,tbl_name, w)
		cur.close()
		db.close()
		if tbl_name !=[]: w.save(xlspath)

if __name__ == "__main__":
    # arg == database path
    db2xls()