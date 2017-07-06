#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright © Sgr
# CreateTime: 2017-07-04 16:48:29

import pandas as pd

big = pd.read_csv('data0.csv')

litter = pd.read_csv('user_score.csv')

data  = pd.merge(big, litter, how='left', on='user_id')

data.to_csv('register.csv', encoding='utf-8')

