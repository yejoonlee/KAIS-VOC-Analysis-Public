# # -*- coding: utf-8 -*-
# # from konlpy import tag
# # from sklearn.feature_extraction.text import CountVectorizer
# # from sklearn.decomposition import LatentDirichletAllocation
# # from stopwords import get_my_stop_words
# # import pickle
# # # import sys
# # import csv
#
# from sklearn.feature_extraction.text import CountVectorizer
# # from sklearn.feature_extraction.text import TfidfVectorizer
# # from sklearn.decomposition import LatentDirichletAllocation
# from konlpy import tag
# # from stopwords import get_my_stop_words
# # import pickle
# # import time
# # import csv
# #
# spliter = tag.Mecab()
#
# nouns = spliter.nouns("행자부가 어떻게 쓰여도 행자부로 나오는가")
# print(nouns)
#
#
#
# f = open("data/preprocessed/by_h/pp_2018_1.txt",'r')
# txts = f.readlines()
# for i,l in enumerate(txts):
#     print(i)
# # def display_topics(csvfile, model, feature_names, no_top_words):
# #     for topic_idx, topic in enumerate(model):
# #         print("Topic %d" % (topic_idx))
# #         csvfile.writerow("Topic %d:" % (topic_idx))
# #         # print([feature_names,topic])
# #         # file.write(" ".join([feature_names[i]
# #         #                 for i in topic.argsort()[:-(no_top_words + 1):-1]])+"\n")
# #         lTopic = topic.argsort()[:-(no_top_words + 1):-1]
# #         for i in lTopic:
# #             csvfile.writerow([str(feature_names[i]),str(topic[i])])
# #
# # start_time = time.time()
# #
# # lda = LatentDirichletAllocation()
# #
# # f_t = open("topics_8_final_cv.csv", 'w')
# # wr = csv.writer(f_t)
# # with open('6789/topic8_topicmodeling_cv', 'rb') as fd:
# #     (features, lda.components_, lda.exp_dirichlet_component_, lda.doc_topic_prior_) = pickle.load(fd)
# # display_topics(wr, lda.components_, features, 100)
# #
# #
# # end_time = time.time()
# # print(str(end_time - start_time)+"times spended")
#
#
# # spliter = tag.Mecab()
#
# # input=[]
# # infile=open('txt/2016_제목.txt','r')
# # for line in infile:
# #     input.append(line)
# # infile.close()
#
# # f = open("topics_5,7,10,15_v5_tf.txt", 'r')
# # text = f.read()
# # text = text.split("\n")
# # fc=open("nnnn.csv",'w')
# # w = csv.writer(fc)
# # for line in text:
# #     t = line.split(":")
# #     w.writerow([t[0]])
# # f.close()
# # fc.close()
# #
# # lFileName = ["2015_답변","2015_제목","2015_질의내용","2016_답변","2016_제목","2016_질의내용","만족도조사,사용자교육,현장방문_2015_상반기","만족도조사,사용자교육,현장방문_2015_하반기","만족도조사,사용자교육,현장방문_2016_상반기","만족도조사,사용자교육,현장방문_2016_하반기","만족도조사,사용자교육,현장방문_2017_상반기","만족도조사,사용자교육,현장방문_2017_하반기","만족도조사,사용자교육,현장방문_2018_상반기","QnA_2015_답변","QnA_2015_제목","QnA_2015_질문","QnA_2016_답변","QnA_2016_제목","QnA_2016_질문","QnA_2017_답변","QnA_2017_제목","QnA_2017_질문","QnA_2018_답변","QnA_2018_제목","QnA_2018_질문"]
# # contents = []
# # for fileName in lFileName:
# #     file = open("txt/%s.txt"%fileName,'r')
# #     text = file.read()
# #     text.replace("건물 번호","건물번호")
# #     text.replace("공인 인증서", "공인인증서")
# #     text.replace("도로명 주소", "도로명주소")
# #     text.replace("서울", "서울시")
# #     text.replace("서울시특별시", "서울시")
# #     text.replace("서울시 특별시", "서울시")
# #     text.replace("경기", "경기도")
# #     text.replace("경기도도", "경기도")
# #     text = text.split("\n")
# #     contents+=text
# #     file.close()
# # f = open("txt/combined_all.txt",'w')
# # f.write("\n".join(contents))
# # f.close()
# #
# # lFileName = ["2015_1","2015_2","2016_1","2016_2","2017_1","2017_2","2018_1"]
# # for name in lFileName:
# #     f = open("txt_q/%s.rtf"%name,'r')
# #     lines = f.read().split("\n")
# #     print("%s : "%name+str(len(lines)))
#
# # import pickle
# # import csv
# # import time
# # from sklearn.decomposition import LatentDirichletAllocation
# # from sklearn.feature_extraction.text import CountVectorizer
# # from konlpy import tag
# #
# # def display_topics(txtfile, model, feature_names, no_top_words):
# #     for topic_idx, topic in enumerate(model.components_):
# #         print("Topic %d" % (topic_idx))
# #         # csvfile.writerow("Topic %d:" % (topic_idx))
# #         txtfile.write("Topic %d:\n" % (topic_idx))
# #         # print([feature_names,topic])
# #         # file.write(" ".join([feature_names[i]
# #         #                 for i in topic.argsort()[:-(no_top_words + 1):-1]])+"\n")
# #         lTopic = topic.argsort()[:-(no_top_words + 1):-1]
# #         for i in lTopic:
# #             # csvfile.writerow([str(feature_names[i]),str(topic[i])])
# #             txtfile.write(str(feature_names[i])+" : "+str(topic[i])+"\n")
# #
# #
# #
# # start_time = time.time()
# # # spliter = tag.Mecab()
# #
# #
# # # # create a blank model
# # lda = LatentDirichletAllocation()
# #
# # f_tt=open("topics_5,7,10,15_v5_cv.txt", 'w')
# # # load parameters from file
# # for i in [5,7,10,15]:
# #     f_tt.write("no_topic = %d\n" % i)
# #     with open ('resource/topic%d_topicmodeling_cv'%i, 'rb') as fd:
# #         (features, lda.components_, lda.exp_dirichlet_component_, lda.doc_topic_prior_) = pickle.load(fd)
# #     display_topics(f_tt, lda, features, 30)
# # f_tt.close()
#
# # infile=open('txt/2015_답변.txt','r')
# # lInfile = infile.read()
# # print(type(lInfile))
# # lInfile = lInfile.split("\n")
# # input = []
# # for line in lInfile:
# #         print("!")
# #         nouns = spliter.nouns(line)
# #         input += nouns
# #         # print(nouns)
# # infile.close()
# # print(input)
#
# # stopped_tokens = [i for i in nouns if not i in get_my_stop_words()]
#
# # print(len(nouns))
#
#
# # no_features = 400
# # no_topics = 20
# # no_top_words = 10
# #
# # tf_vectorizer = CountVectorizer(max_df=0.95, min_df=1, max_features=no_features)
# # # tf = tf_vectorizer.fit_transform(input)
# # tf = tf_vectorizer.fit_transform(stopped_tokens)
# # # print(tf)
# # tf_feature_names = tf_vectorizer.get_feature_names()
# # # print(tf_feature_names)
# # lda = LatentDirichletAllocation(n_topics=no_topics, max_iter=5, learning_method='online', learning_offset=50.,random_state=0).fit(tf)
# #
# # model = (tf_feature_names, lda.components_, lda.exp_dirichlet_component_, lda.doc_topic_prior_)
# #
# # def display_topics(model, feature_names, no_top_words):
# #     for topic_idx, topic in enumerate(model.components_):
# #         print("Topic %d:" % (topic_idx))
# #         print(" ".join([feature_names[i]
# #                         for i in topic.argsort()[:-(no_top_words + 1):-1]]))
# # display_topics(lda, tf_feature_names, no_top_words)
#
#
#
#
# #사전추가...?
#
# # from customized_konlpy.ckonlpy.tag import _twitter
# # from konlpy import tag
# # from collections import Counter
# #
# # spliter = tag.Mecab()
# # # spliter.add_dictionary('도로명 주소', 'Noun')
# #
# # # f = open("2016_제목.txt", 'r')
# # # text = f.read()
# # text = "부산광역시 영도구 태종로372번길 41 행복한 요양원 -> 행복한 요양병원 건물명 수정요청한건 관련해서 민원인 정보 요청함"
# # # print(text)
# # nouns = spliter.pos(text)
# # print(nouns)
# # print(len(list(set(nouns))))
# # count = Counter(nouns)
# # # list = []
# # for n,c in count.most_common(50):
# #     print("tag : " + str(n) + ", count : " + str(c))
#
# # 요청번호
# # 접수구분
# # 업무
# # 업무상세
# # 분류
# # 분류상세
# # 요청일 6
# # 작업일시 7
# # 제목 8
# # 질의내용 9
# # 요청처
# # 자치단체
# # 요청자
# # 연락처
# # SNS수신여부
# # 답변 15
# # 인시던트_작업사유
# # 접수자
# # 담당자
# # 1,2선 처리
# # 진행상태
# # 완료일시 21
# # 이관분류
# # 장기여부
# # 장기SR처리시간(일)
# # 장기SR처리시간(분)
# # 인시던트_장애처리 대상


# -*- coding: utf-8 -*-
from konlpy import tag
from LDA.stopwords import get_my_stop_words

spliter = tag.Mecab()

lFileName = ["pp_all"]
contents = []
for fileName in lFileName:
    file = open("data/preprocessed/%s.txt"%fileName,'r')
    text = file.read()
    # text.replace("건물 번호","건물번호")
    # text.replace("공인 인증서", "공인인증서")
    # text.replace("도로명 주소", "도로명주소")
    # text.replace("서울", "서울시")
    # text.replace("서울시특별시", "서울시")
    # text.replace("서울시 특별시", "서울시")
    # text.replace("경기", "경기도")
    # text.replace("경기도도", "경기도")
    # text.replace("전화 번호", "전화번호")
    text = text.split("\n")
    contents+=text
    file.close()

input = []
lNouns = []
stop_words = get_my_stop_words()
for line in contents:
    nouns = spliter.nouns(line)
    nouns_stoped = [i for i in nouns if i not in stop_words]
    input.append(" ".join(nouns_stoped))
    lNouns += nouns
print("made data")
len_words = len(set(lNouns))

no_features = int(len_words)
print(no_features)