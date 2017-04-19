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
    ws = wb.add_sheet("学生", cell_overwrite_ok=True)
    ws = wb.add_sheet("student_one", cell_overwrite_ok=True)
    row = 0
    col = 0

    for k, v in sorted(content_dict.items(), key=lambda d:d[0]):
        ws.write(row, col, k)
        for i in v:
            col += 1
            ws.write(row, col, i)
        row += 1
        col = 0
    wb.save(excel_name)

if __name__ == '__main__':
#    read_content = read_txt(os.path.join(os.path.split(__file__)[0],'student.txt'))
    read_content = read_txt('student.txt')
    print read_content
    save2excel(read_content, 'stuent.xls')
