# Results
해당 디렉토리에 원래는 모든 데이터를 학습된 LDA 모델을 통해 Topic별로 구분한 결과 파일이 있지만  
포트폴리오를 위한 공개 레파지토리인 관계로 raw 데이터가 노출될 수 있는 파일들은 업로드하지 않았다.  
  
업로드 되어있는 feature_ex17,18은 각 feature(단어)들이 topic 수 설정에 따라 갖게되는 feature-topic 유사도 결과이고  
models_ex17,18은 topic 수 설정을 바꾸며 학습시킨 모델의 결과이다.

-----------------
원래 해당 디렉토리의 구성 형태는 다음과 같다.  
![image](https://user-images.githubusercontent.com/35551019/150095877-a0ab1966-f979-4027-bb87-ed959657d271.png)
  
sim_ex17,18 디렉토리는 topic을 5, 7, 8로 설정하여 topic별로 데이터를 구분하여 저장한 파일들로 구성된다.  
![image](https://user-images.githubusercontent.com/35551019/150094976-f9eb8012-8ee7-4cd1-b2a2-5bf192ff850a.png)
  
numTopic_6 디렉토리는 최종적으로 선택한 topic을 6개로 설정하여 학습시킨 모델과 해당 모델로 데이터를 토픽별로 구분하여 저장한 파일들로 구성된다.
![image](https://user-images.githubusercontent.com/35551019/150095966-53fc7d96-ffad-43d3-ac91-5cbd22e09007.png)
  
  
그 외 txt_topic_* 파일들은 numTopic_6 디렉토리의 파일들과 비슷한 결과물로 csv형식으로 저장되었고 2017년 하반기 데이터가 추가된 결과이다.
![image](https://user-images.githubusercontent.com/35551019/150096311-70cdac26-9e83-4a9b-983b-1d26639a29d3.png)
