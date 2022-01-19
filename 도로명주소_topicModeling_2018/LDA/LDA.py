from sklearn.feature_extraction.text import CountVectorizer
from sklearn.decomposition import LatentDirichletAllocation
from konlpy import tag
from LDA.stopwords import get_my_stop_words
import time

start_time = time.time()

# input=[]
# infile=open('txt/2016_제목.txt','r')
# for line in infile:
#     input.append(line)
# infile.close()
# # print(input)

def display_topics(file, model, feature_names, no_top_words):
    for topic_idx, topic in enumerate(model.components_):
        file.write("Topic %d:\n" % (topic_idx))
        file.write(" ".join([feature_names[i]
                        for i in topic.argsort()[:-(no_top_words + 1):-1]])+"\n")

def repeat_years(title,list_year,list_title):
    for year in list_year:
        fileTitle = "%s_%s"%(title, year)
        # fileTitle = "%s"%(year)
        repeat_titles(fileTitle,list_title)
        # repeat_combined(fileTitle)


def repeat_titles(fileTitle,list_title):
    for title in list_title:
        print(title)

        infile = open('txt/%s_%s.txt' % (fileTitle, title), 'r')
        lInfile = infile.read()
        lInfile = lInfile.split("\n")
        input = []
        lNouns = []
        for line in lInfile:
            nouns = spliter.nouns(line)
            input.append(" ".join(nouns))
            lNouns+=nouns
            # print(nouns)
        infile.close()
        len_words = len(set(lNouns))
        print(len_words)

        # infile = open('txt/%s_%s.txt' % (fileTitle, title), 'r')
        # lInfile = infile.read()
        # nouns = spliter.nouns(lInfile)
        # len_words = len(set(nouns))
        # infile.close()

        no_features = int(len_words / 5)
        no_top_words = 10
        tf_vectorizer = CountVectorizer(max_df=0.95, min_df=1, max_features=no_features, stop_words=get_my_stop_words())
        tf = tf_vectorizer.fit_transform(input)
        # tf = tf_vectorizer.fit_transform(nouns)
        tf_feature_names = tf_vectorizer.get_feature_names()

        f_t = open("txt/%s_%s_topics_s.txt" % (fileTitle, title), 'w')
        for num in [5, 10, 15, 20]:
            f_t.write("no_topic = %d\n" % num)
            print(num)
            no_topics = num
            lda = LatentDirichletAllocation(n_topics=no_topics, max_iter=5, learning_method='online',
                                            learning_offset=50., random_state=0).fit(tf)

            model = (tf_feature_names, lda.components_, lda.exp_dirichlet_component_, lda.doc_topic_prior_)
            # with open('resources/'+ "2016_제목_topicmodeling", 'wb') as fp:
            #     pickle.dump(model, fp)
            display_topics(f_t, lda, tf_feature_names, no_top_words)
        f_t.close()
        print("Done" + "txt/%s_%s_topics.txt" % (fileTitle, title))

def repeat_combined(fileTitle):
    for title in ["연간"]:
        print(title)

        infile1 =open('txt/%s_답변.txt'%(fileTitle),'r')
        infile2 = open('txt/%s_제목.txt' % (fileTitle), 'r')
        infile3 = open('txt/%s_질의내용.txt' % (fileTitle), 'r')
        lInfile1 = infile1.read()
        lInfile1 = lInfile1.split("\n")
        lInfile2 = infile2.read()
        lInfile2 = lInfile2.split("\n")
        lInfile3 = infile3.read()
        lInfile3= lInfile3.split("\n")
        lInfile = lInfile1+lInfile2+lInfile3
        input = []
        lNouns = []
        for line in lInfile:
            nouns = spliter.nouns(line)
            input.append(" ".join(nouns))
            lNouns += nouns

        len_words = len(set(lNouns))

        infile1.close()
        infile2.close()
        infile3.close()

        no_features = int(len_words / 5)
        no_top_words = 10
        tf_vectorizer = CountVectorizer(max_df=0.95, min_df=1, max_features=no_features, stop_words=get_my_stop_words())
        tf = tf_vectorizer.fit_transform(input)
        # tf = tf_vectorizer.fit_transform(nouns)
        tf_feature_names = tf_vectorizer.get_feature_names()

        f_t = open("txt/%s_%s_topics_s.txt" % (fileTitle, title), 'w')
        for num in [5, 10, 15, 20]:
            f_t.write("no_topic = %d\n" % num)
            print(num)
            no_topics = num
            lda = LatentDirichletAllocation(n_topics=no_topics, max_iter=5, learning_method='online',
                                            learning_offset=50., random_state=0).fit(tf)

            model = (tf_feature_names, lda.components_, lda.exp_dirichlet_component_, lda.doc_topic_prior_)
            # with open('resources/'+ "2016_제목_topicmodeling", 'wb') as fp:
            #     pickle.dump(model, fp)
            display_topics(f_t, lda, tf_feature_names, no_top_words)
        f_t.close()
        print("Done" + "txt/%s_%s_topics.txt" % (fileTitle, title))



spliter = tag.Mecab()

# title = "만족도조사,사용자교육,현장방문"
title = "QnA"
list_year = [2016,2017,2018]
list_title = ["답변","제목","질문"]
repeat_years(title,list_year,list_title)

# infile=open('txt/만족도조사,사용자교육,현장방문_2017_상반기.txt','r')
# lInfile = infile.read()
# nouns = spliter.nouns(str(lInfile))
# print(len(set(nouns)))
# infile.close()

# for year in [5,6,7,8]:
#     fileTitle = "만족도조사,사용자교육,현장방문_201%d"%year
#     for title in ["상반기","하반기"]:
#         # if fileTitle == "2015" and title == "제목":
#         #     continue
#         print(title)
#
#         # infile1 =open('txt/%s_답변.txt'%(fileTitle),'r')
#         # infile2 = open('txt/%s_제목.txt' % (fileTitle), 'r')
#         # infile3 = open('txt/%s_질문.txt' % (fileTitle), 'r')
#         # lInfile1 = infile1.read()
#         # lInfile2 = infile2.read()
#         # lInfile3 = infile3.read()
#         # lInfile = lInfile1+lInfile2+lInfile3
#
#         infile = open('txt/%s_%s.txt' % (fileTitle,title), 'r')
#         lInfile = infile.read()
#
#         # data = []
#         # for line in lInfile:
#         #     data += list(line)
#         nouns = spliter.nouns(lInfile)
#         len_words = len(set(nouns))
#
#         # infile1.close()
#         # infile2.close()
#         # infile3.close()
#
#         infile.close()
#
#         # stopped_tokens = [i for i in nouns if not i in get_my_stop_words()]
#
#         no_features = int(len_words/5)
#         no_top_words = 10
#         tf_vectorizer = CountVectorizer(max_df=0.95, min_df=1, max_features=no_features, stop_words=get_my_stop_words())
#         # tf = tf_vectorizer.fit_transform(input)
#         tf = tf_vectorizer.fit_transform(nouns)
#         tf_feature_names = tf_vectorizer.get_feature_names()
#
#         f_t = open("txt/%s_%s_topics.txt"%(fileTitle,title), 'w')
#         for num in [5,10,15,20]:
#             f_t.write("no_topic = %d\n"%num)
#             print(num)
#             no_topics = num
#             lda = LatentDirichletAllocation(n_topics=no_topics, max_iter=5, learning_method='online', learning_offset=50.,random_state=0).fit(tf)
#
#             model = (tf_feature_names, lda.components_, lda.exp_dirichlet_component_, lda.doc_topic_prior_)
#             # with open('resources/'+ "2016_제목_topicmodeling", 'wb') as fp:
#             #     pickle.dump(model, fp)
#             display_topics(f_t, lda, tf_feature_names, no_top_words)
#         f_t.close()
#         print("Done"+"txt/%s_%s_topics.txt"%(fileTitle,title))

end_time = time.time()
print(str(end_time - start_time)+"times spended")


# tf2 = tf_vectorizer.fit_transform(data)
# predict = lda.transform(tf2)
# list_client_output = predict.tolist()
# clientTopic = []
# for j in range(0, len(list_client_output)): clientTopic.append(list_client_output[j])
#
# for row in clientTopic:
#     print(row)