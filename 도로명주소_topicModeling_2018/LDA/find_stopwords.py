# from customized_konlpy.ckonlpy.tag import Twitter
from konlpy import tag
from collections import Counter


spliter = tag.Mecab()

# f = open("txt/2015_제목.txt", 'r')
f = open("txt/만족도조사,사용자교육,현장방문_2017_상반기.txt", 'r')
# f = open("txt/2015_질의내용.txt", 'r')

# text = f1.read()+f2.read()+f3.read()
text = f.read()
# print(text)

nouns = spliter.nouns(text)
print(nouns)
print(len(list(set(nouns))))
count = Counter(nouns)

for n,c in count.most_common(1000):
    print("tag : " + str(n) + ", count : " + str(c))