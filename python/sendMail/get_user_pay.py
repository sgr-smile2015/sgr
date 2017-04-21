#!/usr/bin/python
# -*- coding: utf-8 -*-

import pymongo
import time
import datetime
import sys
#sys.setdefaultencoding("utf-8")

from jinja2 import Environment, PackageLoader
env = Environment(loader=PackageLoader('get_user_pay', '.'))


mongo_uri = "mongodb://usercenter:usercenter@db1,db2,db3/usercenter" 
#mongo_uri = "mongodb://usercenter:usercenter@192.168.1.83,192.168.1.82,192.168.1.81/usercenter"

def get_timestamp(date_str):
    timestamp = time.mktime(datetime.datetime.strptime(date_str, "%Y-%m-%d %H:%M:%S").timetuple())
    return timestamp * 1000

"""
def query_mongo(start, end, category=[3,4,5,6]):
    client = pymongo.MongoClient(host=mongo_uri)
    usercenter_db = client["usercenter"]
    user_info_collection = usercenter_db["user_info"]
    count = user_info_collection.find({
                                       "registerTime":{"$gt":start,"$lt":end}, "registerChannel":{"$in": category}}).count()
    return count
"""

from pgsql_utils import query as query_test

if __name__ == "__main__":
    start_str = sys.argv[1] + " 00:00:00"
    start_timestamp = get_timestamp(start_str)
    start_sec = start_timestamp / 1000
#    start_timestamp = (sys.argv[1])

    end_str = sys.argv[2] + " 00:00:00"
    end_timestamp = get_timestamp(end_str)
    end_sec = end_timestamp / 1000
#    end_timestamp = int(sys.argv[2])
    start_time = 1469980800 #begin time 2016-08-01
    start_time_user = get_timestamp('2016-08-01 00:00:00')

    # android
    pay_total = []
    pay = []
    total = 0
    for i in [3, 5, 7]:
        pay_data = query_test('user_package_order', 'order_time', start_time, end_sec, 'buy_platform', [i],'and pay_status=1')
        pay_total.append(pay_data)
        data = query_test('user_package_order', 'order_time', start_sec, end_sec, 'buy_platform', [i],'and pay_status=1')
        pay.append(data)
        total += pay_data

##########
    # IOS
    user_total = []
    user = []
    total_user = 0
    for i in [3, 4, 6]:
        user_data = query_test('user_account', 'ts_create', start_time_user, end_timestamp, 'register_channel',[i])
        user_total.append(user_data)
        data = query_test('user_account', 'ts_create', start_timestamp, end_timestamp, 'register_channel',[i])
        user.append(data)
        total_user += user_data

    #实体卡
    card_total = []
    card = []
    total_card = 0
    for i in [1, 2]:
        card_data = query_test('card_info', 'active_time', start_time, end_sec, 'card_type',[i])
        card_total.append(card_data)
        data = query_test('card_info', 'active_time', start_sec, end_sec, 'card_type',[i])
        card.append(data)
        total_card += card_data

    table_list = [{ "name":"ios", "value":[pay_total[1], pay[1]] },
                  { "name":"android", "value":[pay_total[0], pay[0]] },
                  { "name":"web", "value":[pay_total[2], pay[2]] },
                  { "name":"total", "value":[total] },
		  ]

    user_list = [
                  { "name":"ios", "value":[user_total[0], user[0]] },
                  { "name":"android", "value":[user_total[1], user[1]] },
                  { "name":"web", "value":[user_total[2], user[2]] },
                  { "name":"total", "value":[total_user] },
		]

    card_list = [
		 {"name":"official","value":[card_total[0], card[0]]},
		 {"name":"experience","value":[card_total[1], card[1]]},
                ]
#    print table_list

    tmp = env.get_template("mail.html")
    with open('att/result.html', 'w') as f:
        f.write(tmp.render(table_list=table_list, user_list=user_list, card_list=card_list).encode('utf8'))

    tmp = env.get_template("mail.txt")
    with open('att/result.txt', 'wb') as f:
        f.write(tmp.render(table_list=table_list).encode('utf8'))
