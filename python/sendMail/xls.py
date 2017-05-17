#!/usr/bin/env python
#_*_ coding:utf-8 _*_

import xlwt
import json
import os
import time

from bak import query_pay as query_pay
from bak import query_user as query_user


topic = [
        '用户ID', 
        '订单时间',
        '订单类型',
        '购买的渠道',
        '订单来源渠道',
        '优惠码',
        '金额(分)',
        '用户ID',
        '注册类型',
        '注册平台',
        '体验卡次数',
        '创建时间',
        '有效状态'
        ]


def get_timestamp():
    t = time.localtime()
    day = int(time.mktime(t))
    t2 = list(t)
    t2[2] = t2[2] - 1
    yesterday = int(time.mktime(t2)) 
    
    return yesterday, day


def ret_local_time(stamp):
    tmp = time.localtime(stamp)
    return time.strftime('%Y/%m/%d %H:%M:%S', tmp)


def ret_buy_platform(channel_id):
    if channel_id == 3:
        return 'android'
    elif channel_id == 5:
        return 'ios'
    else :
        return 'web'

#1-手机号码;2-QQ登录;3-微信登录;4-微博;5-邮件;6-卡号登录
def ret_register_platform(platform_id):
    if platform_id == 1:
        return '手机'
    elif platform_id == 2:
        return 'QQ登陆'
    elif platform_id == 3:
        return '微信'
    elif platform_id == 4:
        return '微博'
    elif platform_id == 5:
        return '卡号'
    else:
        return 'unknown'


#0-UNKNOWN;1-IPIN_PC;2-OTHER;3-WMZY_IOS;4-WMZY_ANDROID;5-WMZY_H5;6-WMZY_PC;7-IPIN_H5
def ret_register_channel(channel_id):
    if channel_id == 1:
        return 'iPIN-pc'
    elif channel_id == 2:
        return 'other'
    elif channel_id == 3:
        return 'wmzy-ios'
    elif channel_id == 4:
        return 'wmzy-android'
    elif channel_id == 5:
        return 'wmzy-h5'
    elif channel_id == 6:
        return 'wmzy-pc'
    elif channel_id == 7:
        return 'iPIN-h5'
    else:
        return 'unknown'
        

def rename_file(path, day):
    d = ret_local_time(day)
    file_name = d.replace('/', '-').split()[0]
    #file_name = file_name + '.xls'
    for file in os.listdir(path):
        if os.path.isfile(os.path.join(path, file)) == True: 
            if file.find('.xls') > 0:
                newname = file_name + '.xls'
                os.rename(os.path.join(path, file), os.path.join(path, newname))
                

def remove_dir_file(t_dir):
    # t_file = './xls'
    for file in os.listdir(t_dir):
        t_file = os.path.join(t_dir, file)
        if os.path.isfile(t_file):
            os.remove(t_file)

#ret = query('user_package_order','order_time', 1477929600, 1485878400, 'pay_status=1 limit 3')


def init_data(user_pay_list):
    user_id_list = []
    user_list = []
    size_list = len(user_pay_list)
    
    for i in range(size_list):
            user_id_list.append(user_pay_list[i][0]) #获取用ID列表
    
    for id_num in user_id_list:
        one_user = query_user('user_account', 'user_id', id_num)
        user_list.extend(one_user)
    
    for t in range(size_list):
        user_pay_list[t].extend(user_list[t])

    for i in range(size_list):
            user_pay_list[i][1] = ret_local_time(user_pay_list[i][1]) #转换订单时间
            user_pay_list[i][3] = ret_buy_platform(user_pay_list[i][3])
            user_pay_list[i][8] = ret_register_platform(user_pay_list[i][8])
            user_pay_list[i][9] = ret_register_channel(user_pay_list[i][9])
            user_pay_list[i][11] = ret_local_time(user_pay_list[i][11])
    
    #print user_pay_list
    return user_pay_list


def save2excel(excel_name, data):
    wb = xlwt.Workbook(encoding = 'utf-8', style_compression=0)
    sheet = wb.add_sheet("总体日报表", cell_overwrite_ok=True)
    #style = xlwt.easyxf('font: bold on')
    style_top = xlwt.easyxf('font: bold on; align: wrap on, vert centre, horiz center')
    style_mul = xlwt.easyxf('font: bold no; align: wrap on')
    for i in range(len(topic)):
        sheet.write(0, i, topic[i], style_top)
        for j in range(len(data)):    
            sheet.write(j+1, i, data[j][i], style_mul)
    wb.save(excel_name)


if __name__ == '__main__':
    yesterday , day = get_timestamp()
    remove_dir_file('./excel')
    data = query_pay('user_package_order','order_time', yesterday, day, 'pay_status=1 limit 3')
    init_data(data)
    save2excel("./excel/excel.xls", data)
    rename_file('./excel', day)
