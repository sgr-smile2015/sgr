#!/usr/bin/env python
# _*_ coding: utf-8 _*_

def get_salary():
    '''
     get you salary
    :return: int salary
    '''
    ret = raw_input('You salary is:')
    return int(ret)

def commodity_list():
    return {
        'mp3': 300 ,
        'book': 100 ,
        'phone': 5000 ,
        'kindle': 2000 ,
        'milk': 50
    }


def format_print(list):
    print '<--清单-->'
    for i in list:
        print '%s: %s' %(i, list[i])


def make_you_choose(good_list):
    ret = raw_input('make you choose:')
    if ret in good_list.keys():
        return ret, good_list[ret]
    else:
        print '没有该物品'
        return False , False

def loop_continue():
    ret = raw_input('continue? [y/n]')
    if ret == 'y':
        return True
    else :
        return False

def ret_buy_info(buy_list, good_list, key):
    if key in good_list.keys():
        buy_list.append('%s:%s' %(key, good_list[key]))
    return buy_list

def print_buy_info(good_list, balance):
    for i in good_list:
        print '<已购买>', i
    print '<余额￥>', balance
    return None

def can_buy_goods(salary, price):
    if salary < price:
        print "sorry, you can't buy this"
        return False
    else:
        return True


def main():
    buy_flag = True
    buy_info = []
    salary = get_salary()
    list = commodity_list()

    loop_flag = True
    while True:
        format_print(list)
        good_id, money = make_you_choose(list)
        buy_flag = can_buy_goods(salary, money)
        if buy_flag == False:
            print_buy_info(buy_info, salary)
            continue

        salary -= money
        buy_info = ret_buy_info(buy_info, list, good_id)
        print_buy_info(buy_info, salary)

        loop_flag = loop_continue()
        if loop_flag == False or salary == 0:
            break
    print_buy_info(buy_info, salary)


if __name__ == '__main__':
    main()
