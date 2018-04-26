#!/bin/usr/python3
# -*- coding: utf-8 -*-

n = 0
for i in range(1, 5):
    for j in range(1, 5):
        for k in range(1, 5):
            if (i != j) and (i != k) and (j != k):
                print(i,j,k)                
                n += 1
print("There are", n, "numbers.")
print("%s%d%s"%("There are ",n," numbers."))