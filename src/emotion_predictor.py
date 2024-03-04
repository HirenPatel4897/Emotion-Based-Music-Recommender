from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch

model_path = "../emotion_detection_model"
model = AutoModelForSequenceClassification.from_pretrained(model_path)
tokenizer = AutoTokenizer.from_pretrained(model_path)

def predict_emotion(text):
    inputs = tokenizer(text, return_tensors="pt", padding=True, truncation=True, max_length=128)
    with torch.no_grad():
        logits = model(**inputs).logits
    prediction = torch.argmax(logits, dim=-1)
    class_names = ['sadness', 'joy', 'love', 'anger', 'fear', 'surprise']  # Update with your actual class names
    return class_names[prediction.item()]
