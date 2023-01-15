#!/usr/bin/python
# -*- coding: UTF-8 -*-

quant1x_home = '~/.quant1x'
quant1x_data = quant1x_home + '/data'
quant1x_data_cn = quant1x_data + '/cn'
quant1x_data_hk = quant1x_data + '/hk'
quant1x_info = quant1x_home + '/info'
quant1x_info_cn = quant1x_info + '/cn'
quant1x_info_hk = quant1x_info + '/hk'

from quant1x.data import resources

# export
D = resources.DataHandler()
