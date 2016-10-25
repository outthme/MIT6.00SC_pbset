## -*- coding: utf-8 -*-
#"""
#Spyder Editor
#
#This is a temporary script file.
#"""
#import md5
#import MySQLdb
#def coupon_gen(amounts):
#    key_list=[]
#    for i in range(0, amounts-1):
#        key_list.append('Kkey' + str(i))
#    return key_list
#
#m = md5.new()
#key_dic = {}
#key_accept = coupon_gen(200)
#for i in key_accept:
#    m.update(i)
#    key_dic[m.hexdigest()] = 0
#
##use MySQLdb.connect to create a connection and create a cursor
#conn = MySQLdb.connect(db='testbase', host='localhost', user='testuser',passwd='225157aa')
#cursor = conn.cursor()
#
##put the key data which from key_dic into the connection path 
#for i in key_dic:
#    cursor.execute("INSERT INTO coupon(coupon_keys) VALUES('" + i +"')")
#    print cursor.fetchall()
#
#cursor.close()
#conn.commit() #Be attention to commit your affairs
#conn.close()
line = raw_input()
print type(line)

line2 = raw_input()

print line+line2