#!/usr/bin/python
# -*- coding: utf-8 -*-
print("Введите переменную n состоящую из чисел")
en=input()
i=0
e=0
while i<len(en):
	if int(en[i])>e:
		e=int(en[i])
	# print (en[i])
	i=i+1
print ("самое большое число "+str(e))