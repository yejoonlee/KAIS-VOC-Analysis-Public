import csv

f= open("data/raw/raw_separated/sq_2015_1_c.txt",'r')
wr = f.read()
f2= open("data/raw/raw_separated/sq_2015_2_c.txt",'r')
wr2 = f2.read()
f3= open("data/raw/raw_separated/sq_2016_1_c.txt",'r')
wr3 = f3.read()
f4= open("data/raw/raw_separated/sq_2016_2_c.txt",'r')
wr4 = f4.read()
f5= open("data/raw/raw_separated/sq_2017_1_c.txt",'r')
wr5 = f5.read()
f6= open("data/raw/raw_separated/sq_2017_2_c.txt",'r')
wr6 = f6.read()
f7= open("data/raw/raw_separated/sq_2018_1_c.txt",'r')
wr7 = f7.read()

f8 = open("data/raw/raw_combined/by_c/sq_all.txt",'w')
f8.write(wr+wr2+wr3+wr4+wr5+wr6+wr7)