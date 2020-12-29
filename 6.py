#!/usr/bin/python
# -*- coding: utf-8 -*-
print("Введите переменную a ")
a=int(input())
print("Введите переменную b ")
b=int(input())

day=1
aa=a
while aa<b:
	print (str(day)+ "-й день "+str(aa))
	aa=aa+(aa/100*10)
	day=day+1;

print (str(day)+ "-й день "+str(aa))
aa=aa+(aa/100*10)
day=day+1;