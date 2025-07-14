from fastapi import FastAPI
from pydantic import BaseModel
from transformers import pipeline
import os
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

MODEL_PATH = "./model"

# Load fine-tuned model if present
if os.path.exists(MODEL_PATH) and len(os.listdir(MODEL_PATH)) > 0:
    print("📦 Loading fine-tuned model...")
    sentiment_pipeline = pipeline("sentiment-analysis", model=MODEL_PATH, tokenizer=MODEL_PATH)
else:
    print("⬇️ Loading default model...")
    sentiment_pipeline = pipeline("sentiment-analysis")

# Input schema
class InputText(BaseModel):
    text: str

@app.post("/predict")
def predict(input: InputText):
    result = sentiment_pipeline(input.text)[0]
    label = result["label"]

    # Handle label_0/1 conversion if needed
    if label.lower() in ["label_0", "label_1"]:
        label_map = { "label_0": "negative", "label_1": "positive" }
        label = label_map.get(label.lower(), label.lower())

    return {
        "label": label.lower(),
        "score": round(result["score"], 4)
    }

@app.get("/")
def home():
    return {"message": "Sentiment analysis API is running!"}
