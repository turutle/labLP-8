#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def converter(type):
    def fun2(string):
        if type == 'list':
            lst = list(string.split())
            return lst
        else:
            tup = tuple(string.split())
            return tup
    return fun2