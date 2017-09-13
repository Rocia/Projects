#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 12 11:38:29 2017

@author: root
"""

a = {1:2,3:4}
b = {1:2,5:4}
for abc in a:
	if abc in b:
		print(abc)