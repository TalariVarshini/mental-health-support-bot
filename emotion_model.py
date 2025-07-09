from transformers import pipeline

emotion_classifier = pipeline("text-classification", 
                               model="j-hartmann/emotion-english-distilroberta-base", 
                               return_all_scores=True)

def get_emotion(text):
    result = emotion_classifier(text)[0]
    top_emotion = sorted(result, key=lambda x: x['score'], reverse=True)[0]
    return top_emotion['label'], round(top_emotion['score'], 2)
