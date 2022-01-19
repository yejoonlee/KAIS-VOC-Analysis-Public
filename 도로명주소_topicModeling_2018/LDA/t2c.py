# -*- coding: utf-8 -*-
import csv

f = open("data/raw/raw_separated/sq_2018_1_c.txt",'r',encoding= "UTF-8")
txt = f.read()
lines = txt.split("\n")

f2 = open("data/raw/raw_csv/sq_2018_1.csv",'w',encoding= "UTF-8")
w = csv.writer(f2)
for line in lines:
    w.writerow([line])
