# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import md5
def coupon_gen(amounts):
    key_list=[]
    for i in range(0, amounts-1):
        key_list.append('Kkey' + str(i))
    return key_list

m = md5.new()
key_dic = {}
key_accept = coupon_gen(200)
for i in key_accept:
    m.update(i)
    key_dic[m.hexdigest()] = 0

