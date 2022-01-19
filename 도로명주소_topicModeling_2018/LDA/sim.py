import pickle
import csv
import time
from sklearn.decomposition import LatentDirichletAllocation
from sklearn.feature_extraction.text import CountVectorizer
from konlpy import tag

start_time = time.time()
spliter = tag.Mecab()


# # create a blank model
lda = LatentDirichletAllocation()

# load parameters from file
# with open ('resource/topic7_topicmodeling_cv', 'rb') as fd:
with open('results/topic6_topicmodeling_cv', 'rb') as fd:
    (features, lda.components_, lda.exp_dirichlet_component_, lda.doc_topic_prior_) = pickle.load(fd)




# the dataset to predict on (first two samples were also in the training set so one can compare)
lFileName = ["pp_2016_2"]
# lFileName = ["2015_1sq"]
# lFileName = ["만족도조사,사용자교육,현장방문_2015_상반기"]
# lFileName = ["combined_all"]
contents = []
for fileName in lFileName:
    file = open("data/preprocessed/by_h/%s.txt"%fileName,'r')
    text = file.read()
    # text.replace("건물 번호", "건물번호")
    # text.replace("공인 인증서", "공인인증서")
    # text.replace("도로명 주소", "도로명주소")
    # text.replace("서울", "서울시")
    # text.replace("서울특별시", "서울시")
    # text.replace("서울시특별시", "서울시")
    # text.replace("서울시 특별시", "서울시")
    # text.replace("경기", "경기도")
    # text.replace("경기도도", "경기도")
    # text.replace("전화 번호", "전화번호")
    text = text.split("\n")
    contents+=text
    file.close()

print(len(contents))
# print(type(contents))


# def printExsen(t):
#     print("-------")
#     print(contents[t.index(max(t))])
#     del(t[t.index(max(t))])


input = []
for line in contents:
    # if line == '':
    #     continue
    nouns = spliter.nouns(line)
    input.append(" ".join(nouns))

# Vectorize the training set using the model features as vocabulary
tf_vectorizer = CountVectorizer(vocabulary=features)
tf = tf_vectorizer.fit_transform(input)

# transform method returns a matrix with one line per document, columns being topics weight
predict = lda.transform(tf)
end_time = time.time()
print(str(end_time - start_time) + 's, text predict')

# output array를 list로 변환
list_client_output = predict.tolist()


txtTopic = []
for j in range(0, len(list_client_output)): txtTopic.append(list_client_output[j])


# 결과를 csv파일에 한줄씩 입력
# f = open('../resources/titleTopic_mdpi'+'.csv', 'w', encoding='utf-8', newline="")
# wr = csv.writer(f)
t1 = []
t2 = []
t3 = []
t4 = []
t5 = []
t6 = []
# t7 = []
# t8 = []
# t9 = []
# t10 = []
# t11 = []
# t12 = []
# t13 = []
# t14 = []
# t15 = []
for row in txtTopic:
    t1.append(row[0])
    t2.append(row[1])
    t3.append(row[2])
    t4.append(row[3])
    t5.append(row[4])
    t6.append(row[5])
    # t7.append(row[6])
    # t8.append(row[7])
    # t9.append(row[8])
    # t10.append(row[9])
    # t11.append(row[10])
    # t12.append(row[11])
    # t13.append(row[12])
    # t14.append(row[13])
    # t15.append(row[14])

# l = [t1,t2,t3,t4,t5,t6]
#
# for i,t in enumerate(l):
#     print(i)
#     for i in range(11):
#         printExsen(t)


#
# f = open("ff.csv",'w')
# w = csv.writer(f)
# w.writerow(t1)
# w.writerow(t2)
# w.writerow(t3)
# w.writerow(t4)
# w.writerow(t5)
# w.writerow(t6)
# w.writerow(t7)
# w.writerow(t8)


ffff = open("results/txt_topic_2016_2_n6.csv",'w')
# # # ffff = open("final/txt_topic_2018_1_sq.csv",'w')
# # # ffff = open("final/txt_topic_2015_1_a.csv",'w')
#
w = csv.writer(ffff)
for i,row in enumerate(txtTopic):
    if row.index(max(row)) == row.index(min(row)):
        w.writerow([contents[i].replace(",",""),"Same"])
    if row.index(max(row)) == 0:
        w.writerow([contents[i].replace(",",""),0])
    if row.index(max(row)) == 1:
        w.writerow([contents[i].replace(",",""), 1])
    if row.index(max(row)) == 2:
        w.writerow([contents[i].replace(",",""), 2])
    if row.index(max(row)) == 3:
        w.writerow([contents[i].replace(",",""), 3])
    if row.index(max(row)) == 4:
        w.writerow([contents[i].replace(",",""), 4])
    if row.index(max(row)) == 5:
        w.writerow([contents[i], 5])
    # if row.index(max(row)) == 6:
    #     w.writerow([contents[i], 6])
    # if row.index(max(row)) == 7:
    #     w.writerow([contents[i], 7])
    # if row.index(max(row)) == 8:
    #     w.writerow([contents[i], 8])
    # if row.index(max(row)) == 9:
    #     w.writerow([contents[i], 9])
    print(i)
    i+=1
#
# print(s0,s1,s2,s3,s4,s5,s6,s7)
#
# print("-------")
# print(contents[t1.index(max(t1))])
# del(t1[t1.index(max(t1))])
# print(contents[t1.index(max(t1))])
# print("-------")
# print(contents[t9.index(max(t9))])
# print(contents[t10.index(max(t10))])
# print(contents[t11.index(max(t11))])
# print(contents[t12.index(max(t12))])
# print(contents[t13.index(max(t13))])
# print(contents[t14.index(max(t14))])
# print(contents[t15.index(max(t15))])





# f.close()

end_time = time.time()
print(str(end_time - start_time) + 's, print')


