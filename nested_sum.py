# -*- coding: utf-8 -*-
"""
Created on Sat Nov 26 18:34:53 2022

@author: kelme
"""

def nested_sum(x):
    integer = 0
    for i in range(0,len(x)):
        if type(x[i]) == int:
            integer = integer + x[i]
        if type(x[i]) == list:
            integer = integer + nested_sum(x[i])
    return integer

print(nested_sum([5, [4, "3"], 4, [3, [2.5, [1, 1]]]]))