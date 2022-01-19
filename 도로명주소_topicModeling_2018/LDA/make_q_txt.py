import csv

f=open("무제 폴더/sq_2018_1.csv",'r')
w = csv.reader(f)

ff = open("무제 폴더/sq_2018_1_c.txt",'w')
for l in w:
    a = "".join(l)
    b = a.split("\n")
    c = "".join(b)
    ff.write(a+"\n")