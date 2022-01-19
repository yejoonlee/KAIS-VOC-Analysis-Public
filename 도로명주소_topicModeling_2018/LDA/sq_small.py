# -*- coding: utf-8 -*-
f = open("data/preprocessed/by_c/pp_sq_all_s.txt",'r')
lines = f.readlines()

a = 2
f2 = open("data/preprocessed/by_c/pp_sq_all_ss.txt",'w')
for i,line in enumerate(lines):
    if i%a == 0:
        f2.write(line)
