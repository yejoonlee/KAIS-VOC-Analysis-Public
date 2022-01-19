# -*- coding: utf-8 -*-
from sklearn.feature_extraction.text import CountVectorizer
# from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.decomposition import LatentDirichletAllocation
from konlpy import tag
from LDA.stopwords import get_my_stop_words
import pickle
import time
import csv

def display_topics(csvfile, model, feature_names, no_top_words):
    for topic_idx, topic in enumerate(model.components_):
        print("Topic %d" % (topic_idx))
        csvfile.writerow(["Topic %d:" % (topic_idx)])
        # print([feature_names,topic])
        # file.write(" ".join([feature_names[i]
        #                 for i in topic.argsort()[:-(no_top_words + 1):-1]])+"\n")
        lTopic = topic.argsort()[:-(no_top_words + 1):-1]
        for i in lTopic:
            csvfile.writerow([str(feature_names[i]),str(topic[i])])

start_time = time.time()

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
# len_words = 20

no_features = int(len_words)
print(no_features)
no_top_words = 100
# tf_vectorizer = TfidfVectorizer(max_df=0.95, min_df=1, max_features=no_features, stop_words=stop_words)
tf_vectorizer = CountVectorizer(max_df=0.95, min_df=1, max_features=no_features, stop_words=stop_words)
tf = tf_vectorizer.fit_transform(input)
# tf = tf_vectorizer.fit_transform(nouns)
tf_feature_names = tf_vectorizer.get_feature_names()

# f_t = open("topics_5,7,10,15_v5_tf.csv", 'w')
for num in [5]:
        # [5, 7, 10, 15]:
    f_t = open("results/topics_%d_final_cv.csv"%num, 'w')
    wr = csv.writer(f_t)
    wr.writerow(["no_topic = %d" % num])
    print("no_topic = %d" % num)
    no_topics = num
    lda = LatentDirichletAllocation(n_topics=no_topics, max_iter=5, learning_method='online',
                                learning_offset=50., random_state=0).fit(tf)
    model = (tf_feature_names, lda.components_, lda.exp_dirichlet_component_, lda.doc_topic_prior_)
    with open('results/'+ "topic%d_topicmodeling_cv_for_ss"%num, 'wb') as fp:
    # with open('resource/' + "topic%d_topicmodeling_tf" % num, 'wb') as fp:
        pickle.dump(model, fp)
    display_topics(wr, lda, tf_feature_names, no_top_words)
    f_t.close()
print("Complete")


end_time = time.time()
print(str(end_time - start_time)+"times spended")