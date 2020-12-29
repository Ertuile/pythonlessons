#!/usr/bin/python
# -*- coding: utf-8 -*-
print("Введите выручку ")
v=int(input())
print("Введите издержки ")
iz=int(input())

if (iz>v):
	print ("Фирма работает в убыток")
else:
	print ("Фирма рентабельна. Рентабельность - "+str(v-iz))
	print("Введите количество сотрудников ")
	cso=int(input())
	print ("Прибыль фирмы на одного сотрудника "+str(int((v-iz)/cso)))

