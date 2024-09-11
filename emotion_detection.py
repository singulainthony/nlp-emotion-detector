import requests
import json


def emotion_detector(text_to_analyze: str) -> str:
    """ 
    Run emotion detection using Watson NLP library.

    NOTE: Currently, this code only works with IBM Cloud IDE! 
          Otherwise, ConnectionError occurs.
    """

    # Get emotion analysis using Watson NLP Library
    response = requests.post(url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict', 
                             headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"},
                             json = { "raw_document": { "text": text_to_analyze} })
    

    # Example Output HTTP-Request:
    # Input: text_to_analyze = "I love technology"
    # Output: response.text = '{ 
    #                             "emotionPredictions": [{ 
    #                                                      "emotion": { 
    #                                                                    "anger": 0.01364663, 
    #                                                                    "disgust": 0.0017160787, 
    #                                                                    "fear": 0.008986978, 
    #                                                                    "joy": 0.9719017, 
    #                                                                    "sadness": 0.055187024 
    #                                                                 }, 
    #                                                      "target": "", 
    #                                                      "emotionMentions": [{ 
    #                                                                             "span": { 
    #                                                                                        "begin": 0, 
    #                                                                                        "end": 18, 
    #                                                                                        "text": "I love technology." 
    #                                                                                     }, 
    #                                                                             "emotion": { 
    #                                                                                           "anger": 0.01364663, 
    #                                                                                           "disgust": 0.0017160787, 
    #                                                                                           "fear": 0.008986978, 
    #                                                                                           "joy": 0.9719017, 
    #                                                                                           "sadness":0.055187024 
    #                                                                                        } 
    #                                                                         }]
    #                                                   }], 
    #                             "producerId": { 
    #                                             "name": "Ensemble Aggregated Emotion Workflow", 
    #                                             "version":"0.0.1" 
    #                                           }
    #                         }'


    # Mockup-Attribute of response.text (should be used later in unit test):
    # text ='{"emotionPredictions":[{"emotion":{"anger":0.01364663, "disgust":0.0017160787, "fear":0.008986978, "joy":0.9719017, "sadness":0.055187024}, "target":"", "emotionMentions":[{"span":{"begin":0, "end":18, "text":"I love technology."}, "emotion":{"anger":0.01364663, "disgust":0.0017160787, "fear":0.008986978, "joy":0.9719017, "sadness":0.055187024}}]}], "producerId":{"name":"Ensemble Aggregated Emotion Workflow", "version":"0.0.1"}}'
    
    
    # Convert JSON to Dictionary
    responseTextDict = json.loads(response.text)
    
    # Extract set of emotions
    emotions = responseTextDict["emotionPredictions"][0]["emotion"]

    # Get Emotion-Key with highest score
    keyMaxScore = max(emotions, key = emotions.get)

    analysisResult = {
        'anger': emotions["anger"],
        'disgust': emotions["disgust"],
        'fear': emotions["fear"],
        'joy': emotions["joy"],
        'sadness': emotions["sadness"],
        'dominant_emotion': keyMaxScore
    }

    return analysisResult



# Uncomment to see result
# result = emotion_detector("I love technology!")
# print(result)
# print(type(result))