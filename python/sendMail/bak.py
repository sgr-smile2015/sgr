#!/usr/bin/env python
# -*- coding: utf-8 -*-

import psycopg2
import psycopg2.extras
import pymongo

from get_user_pay import get_timestamp

#mongo_uri = "mongodb://ipin/mongo1,mongo2/wmzy"

def query_mongo(user_id):
    ret = []
    #查询失败,返回错误
    err_data = [[u'unknown', 'unknown', 'unknown', u'unknown', 'unknown', 'unknown']]

    conn = pymongo.MongoClient('mongo2')
    db = conn.wmzy
    cur = db.user_score_info.find_one(
                                       {"user_id":user_id}, 
                                       ["user_id", "score_rank", "score_type", "province_id", "score", "wenli"]
                                      )
    #cur.pop('_id')
    if cur == None:
        return err_data

    if 'province_id' in cur.keys():
        ret.append(cur['province_id'])
    if 'wenli' in cur.keys():
        ret.append(cur['wenli'])
    if 'score' in cur.keys():
        ret.append(cur['score'])
    if 'score_type' in cur.keys():
        ret.append(cur['score_type'])
    if 'score_rank' in cur.keys():
        ret.append(cur['score_rank'])
    if 'user_id' in cur.keys():
        ret.append(cur['user_id'])

    conn.close()
    des = []
    des.append(ret) #转换数据格式[[a, b]]
    return des


def query(table, condition, start, end, lable, other=''):
    #conn = psycopg2.connect(database="wmzy",user="app_wmzy" , password="fseqP44QZfc6nci",host="192.168.1.45") 
    conn = psycopg2.connect(database="wmzy", user="opsapp", password="tF6QiiMcxnJv6iYgG", host="10.27.113.186") 
    cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    #cur = conn.cursor()
    cur.execute("select count(*) from %s where %s between %d and %d group by %s %s" % (table, condition, start, end, lable, other))
    #ret = cur.fetchone()
    ret = cur.fetchall()
    return ret

def query_pay(table, condition, start, end, lable):
    #conn = psycopg2.connect(database="wmzy",user="app_wmzy" , password="fseqP44QZfc6nci",host="192.168.1.45") 
    conn = psycopg2.connect(database="wmzy", user="opsapp", password="tF6QiiMcxnJv6iYgG", host="10.27.113.186") 
    cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    cur.execute("select user_id, order_time, order_type, buy_platform, buy_channel, \
                 coupon_code, pay_count \
                 from %s where %s between %d and %d and %s" % (table, condition, start, end, lable))
    ret = cur.fetchall()
    cur.close()
    return ret

def query_user(table, condition, user_id):
    #conn = psycopg2.connect(database="wmzy",user="app_wmzy" , password="fse6nci",host="192.168.1.45") 
    conn = psycopg2.connect(database="wmzy", user="opsapp", password="BgG", host="10.27.113.186")
    cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    cur.execute("select register_platform, register_channel, \
                 bound_trial_card, ts_create, status \
                 from %s where %s = %s" % (table, condition, user_id))
    ret = cur.fetchall()
    cur.close()
    return ret

if __name__ == "__main__":
    #ret = query_pay('user_package_order','order_time', 1477929600, 1485878400, 'pay_status=1 limit 4')
    #ret = query_user('user_account','user_id', 2348905)
    ret = query_mongo(20151722)
    print ret

