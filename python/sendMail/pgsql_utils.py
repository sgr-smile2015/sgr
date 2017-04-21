#!/usr/bin/env python
# -*- coding: utf-8 -*-

import psycopg2

from get_user_pay import get_timestamp


def query(table, condition, start, end, lable, category=[], other=''):
     conn = psycopg2.connect(database="wmzy", user="opsapp", password="pZtv6iYgG", host="10.10.13.86")
     cur = conn.cursor()
     cur.execute("select count(*) from %s where %s between %d and %d and %s = %d %s" % (table, condition, start, end, lable, category[0], other))
#     cur.execute("select count(*) from wmzy.user_account where ts_create between %d and %d and register_channel = %d" % (start, end, category[0]))
     ret = cur.fetchone()
     return ret[0]

if __name__ == "__main__":
     ret = query('user_package_order','order_time', 1477929600, 1485878400,'buy_platform',[6],'and pay_status=1')
     #ret = query('user_account','ts_create', 1477929600, 1485878400,'register_channel',[6])
     #ret = query('card_info','active_time', 1490976000, 1492569426,'card_type',[2])
#     ret = query_pg(0, get_timestamp("2017-03-12 00:00:00"), [4])
     print ret

