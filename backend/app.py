from fastapi import FastAPI, Request
from pydantic import BaseModel
from transformers import pipeline
import os

app = FastAPI()

MODEL_PATH = "./model"

# Load pretrained or fine-tuned model
if os.path.exists(MODEL_PATH) and len(os.listdir(MODEL_PATH)) > 0:
    sentiment_pipeline = pipeline("sentiment-analysis", model=MODEL_PATH)
else:
    sentiment_pipeline = pipeline("sentiment-analysis")  # Default model

class InputText(BaseModel):
    text: str

@app.post("/predict")
def predict(input: InputText):
    result = sentiment_pipeline(input.text)[0]
    return {
        "label": result["label"].lower(),  # 'POSITIVE' -> 'positive'
        "score": round(result["score"], 4)
    }
@app.get("/")
def home():
    return {"message": "Sentiment analysis API is running!"}
