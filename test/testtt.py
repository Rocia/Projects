#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 11 14:01:31 2017

@author: root
"""
import re
c = re.compile('<I>([^<]+)</I>', re.IGNORECASE)
d = re.compile("(\w+)",re.IGNORECASE)

listt = []

res = ('<I>Gonzalez v. El Dia, Inc.</I>', ('<XREF PUB="add" ROOT="case-cch" NORMVAL="10ADDP10-149">10 ADD &para;10&ndash;149</XREF>', '2002'))
k = res[0]
unq= c.findall(k)
uk= ''.join(d.findall(unq[0]))
'''for value in res [1]:
	v = value[0]
	yr = value[1]'''
i = res[1]
v = i[0]
yr = i[1]
listt.append((k,v,uk,yr))
print(listt)