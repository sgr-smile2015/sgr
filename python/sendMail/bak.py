#!/usr/bin/env python
# -*- coding: utf-8 -*-

import psycopg2
import psycopg2.extras

from get_user_pay import get_timestamp


def query(table, condition, start, end, lable, other=''):
    conn = psycopg2.connect(database="wmzy",user="app_wmzy" , password="7qP4",host="192.168.1.45") 
    #conn = psycopg2.connect(database="wmzy", user="opsapp", password="pZtv6iYgG", host="10.10.13.86")
    cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    #cur = conn.cursor()
    cur.execute("select count(*) from %s where %s between %d and %d group by %s %s" % (table, condition, start, end, lable, other))
    #ret = cur.fetchone()
    ret = cur.fetchall()
    return ret

def query_pay(table, condition, start, end, lable):
    conn = psycopg2.connect(database="wmzy",user="app_wmzy" , password="70yLi",host="192.168.1.45") 
    #conn = psycopg2.connect(database="wmzy", user="opsapp", password="pZtv6iYgG", host="10.10.13.86")
    cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    cur.execute("select user_id, order_time, order_type, buy_platform, buy_channel, \
                 coupon_code, pay_count \
                 from %s where %s between %d and %d and %s" % (table, condition, start, end, lable))
    ret = cur.fetchall()
    cur.close()
    return ret

def query_user(table, condition, user_id):
    conn = psycopg2.connect(database="wmzy",user="app_wmzy" , password="7d0bOfseqPnci",host="192.168.1.45") 
    #conn = psycopg2.connect(database="wmzy", user="opsapp", password="pZtv6iYgG", host="10.10.13.86")
    cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    cur.execute("select user_id, register_platform, register_channel, \
                 bound_trial_card, ts_create, status \
                 from %s where %s = %s" % (table, condition, user_id))
    ret = cur.fetchall()
    cur.close()
    return ret

if __name__ == "__main__":
    #ret = query_pay('user_package_order','order_time', 1477929600, 1485878400, 'pay_status=1 limit 4')
    ret = query_user('user_account','user_id', 10004162)
    #ret = query('user_account','ts_create', 1477929600, 1485878400,'register_channel','')
    #ret = query('card_info','active_time', 1490976000, 1492569426,'card_type',[2])
#    ret = query_pg(0, get_timestamp("2017-03-12 00:00:00"), [4])
    print ret
    #print ret[1]

