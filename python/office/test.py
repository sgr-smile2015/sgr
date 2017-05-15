#!/usr/bin/env python
#_*_ coding:utf-8 _*_

import xlwt
import json
import os


def read_txt(txtfile):
    with open(txtfile, 'r') as f:
        text = f.read().decode('utf-8')
        #text = f.read()
        text_json = json.loads(text)
    return text_json

def save2excel(content_dict, excel_name):
    wb = xlwt.Workbook(encoding = 'utf-8', style_compression=0)
    sheet = wb.add_sheet("总体日报", cell_overwrite_ok=True)
    style = xlwt.easyxf('font:bold 1')
    sheet.write(0,0,"于娜",style)
    row = 0
    col = 0

    for k, v in sorted(content_dict.items(), key=lambda d:d[0]):
        sheet.write(row, col, k)
        for i in v:
            col += 1
            sheet.write(row, col, i)
        row += 1
        col = 0
    wb.save(excel_name)

if __name__ == '__main__':
    content = read_txt('student.txt')
    #print read_content
    save2excel(content, 'student.xls')
