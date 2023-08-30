import numpy as np
import tensorflow as tf
import pandas as pd
import numpy as np
from keras.models import load_model
from keras.callbacks import EarlyStopping, ModelCheckpoint
import random

# 예측 모델 불러오기
best_model = tf.keras.models.load_model('C:\\Users\\samsung\\Desktop\\test\\mbti\\best_model.h5')

def Mbti_predict(gerneList) :
    # 예측
    new_data = np.array(gerneList)
    predicted_probs = best_model.predict(new_data)
    predicted_mbti_index = np.argmax(predicted_probs)
    predicted_mbti_prob = predicted_probs[0, predicted_mbti_index] * 100  # 확률을 백분율로 변환

    # 예측된 MBTI 유형 인덱스를 실제 MBTI 유형으로 변환
    mbti_types = ['ENTJ', 'INTJ', 'ENTP', 'INTP', 'ENFJ', 'INFJ', 'ENFP', 'INFP', 'ESTJ', 'ISTJ', 'ESFJ', 'ISFJ', 'ESTP', 'ISTP', 'ESFP', 'ISFP']
    predicted_mbti = mbti_types[predicted_mbti_index]

    return predicted_mbti, predicted_mbti_prob

