#!/usr/bin/env python
#_*_ coding:utf-8 _*_

import xlwt
import os
import time
import datetime

from bak import query_pay as query_pay
from bak import query_user as query_user
from bak import query_mongo as query_mongo

pronvice_dic = {
"360000000000":"江西",
"440000000000":"广东",
"370000000000":"山东",
"350000000000":"福建",
"610000000000":"陕西",
"520000000000":"贵州",
"110000000000":"北京",
"430000000000":"湖南",
"140000000000":"山西",
"420000000000":"湖北",
"130000000000":"河北",
"320000000000":"江苏",
"410000000000":"河南",
"510000000000":"四川",
"150000000000":"内蒙古",
"530000000000":"云南",
"500000000000":"重庆",
"450000000000":"广西",
"230000000000":"黑龙江",
"340000000000":"安徽",
"460000000000":"海南",
"650000000000":"新疆",
"210000000000":"辽宁",
"220000000000":"吉林",
"120000000000":"天津",
"620000000000":"甘肃",
"330000000000":"浙江",
"640000000000":"宁夏",
"540000000000":"西藏",
"630000000000":"青海",
"310000000000":"上海",
            }


topic = [
        '用户ID', 
        '订单时间',
        '订单类型',
        '购买的渠道',
        '订单来源渠道',
        '优惠码',
        '金额(元)',
        '注册类型',
        '注册平台',
        '体验卡次数',
        '创建时间',
        '有效状态',
        '省份',
        '文理',
        '分数',
        'score_type',
        'score_rank',
        'id'
        ]


def ret_pronvice_id(key):
    if key in pronvice_dic.keys():
        return pronvice_dic[key]
    else:
        return 'unknown'

def ret_wenli(num):
    if num == 1:
        return '文'
    if num == 2:
        return '理'
    if num == 0:
        return '综合'
    else:
        return 'unknown'

def ret_week_time():
    d = datetime.datetime.now()
    week = d.weekday()
    if week == 5:
        return True
    else:
        return False



def get_timestamp(days):
    t = time.localtime()
    day = int(time.mktime(t))
    t2 = list(t)
    t2[2] = t2[2] - days
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
    score_list = []
    size_list = len(user_pay_list)
    
    for i in range(size_list):
            user_id_list.append(user_pay_list[i][0]) #获取用ID列表
    
    #print user_id_list
    for id_num in user_id_list:
        one_user = query_user('user_account', 'user_id', id_num)
        user_list.extend(one_user)
        score_data = query_mongo(id_num)
        #time.sleep(0.5)
        score_list.extend(score_data)
    
    for t in range(size_list):
        user_pay_list[t].extend(user_list[t])
        user_pay_list[t].extend(score_list[t])
    

    for i in range(size_list):
            user_pay_list[i][1] = ret_local_time(user_pay_list[i][1]) #转换订单时间
            user_pay_list[i][3] = ret_buy_platform(user_pay_list[i][3])
            user_pay_list[i][7] = ret_register_platform(user_pay_list[i][7])
            user_pay_list[i][8] = ret_register_channel(user_pay_list[i][8])
            user_pay_list[i][10] = ret_local_time(user_pay_list[i][10]/1000)
            user_pay_list[i][12] = ret_pronvice_id(user_pay_list[i][12])#省份转换
            user_pay_list[i][13] = ret_wenli(user_pay_list[i][13])#文理

    
#    print user_pay_list
    return user_pay_list


def save2excel(excel_name, data, weekdata):
    wb = xlwt.Workbook(encoding = 'utf-8', style_compression=0)
    sheet = wb.add_sheet("总体日报表", cell_overwrite_ok=True)
    sheet_week = wb.add_sheet("每周报表", cell_overwrite_ok=True)
    #style = xlwt.easyxf('font: bold on')
    style_top = xlwt.easyxf('font: bold on; align: wrap on, vert centre, horiz center')
    style_mul = xlwt.easyxf('font: bold no; align: wrap on')
    for i in range(len(topic)):
        sheet.write(0, i, topic[i], style_top)
        for j in range(len(data)):
            sheet.write(j+1, i, data[j][i], style_mul)
    if ret_week_time():
        for x in range(len(topic)):
            sheet_week.write(0, x, topic[x], style_top)
            for y in range(len(weekdata)):
                sheet_week.write(y+1, x, weekdata[y][x], style_mul)
    wb.save(excel_name)


if __name__ == '__main__':
    yesterday , day = get_timestamp(1)
    weekago , day = get_timestamp(7)
    remove_dir_file('./excel')
    data = query_pay('user_package_order','order_time', yesterday, day, 'pay_status=1')
    weekdata = query_pay('user_package_order','order_time', weekago, day, 'pay_status=1')
    init_data(data)
    init_data(weekdata)
    save2excel("./excel/excel.xls", data, weekdata)
    rename_file('./excel', day)
