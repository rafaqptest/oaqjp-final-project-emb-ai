import requests
import json

def emotion_detector(text_to_analyze): 
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    myobj = { "raw_document": { "text": text_to_analyze } }
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
	response = requests.post(url, json = myobj, headers=header)
    formatted_response = response.json()
    if response.status_code == 400:
	    return {'Dominant emotion': None, 'Score': None}
	else:
        emotions = formatted_response['emotionPredictions'][0]['emotion']
        dominant_emotion = max (emotions, key=emotions.get)
        dominant_score = emotions[dominant_emotion]
        return {'Dominant emotion': dominant_emotion, 'Score': dominant_score}
