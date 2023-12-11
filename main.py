from fastapi import FastAPI
from pydantic import BaseModel
from transformers import pipeline

def analyze_sentiment(text):
    classifier = pipeline("sentiment-analysis", model="blanchefort/rubert-base-cased-sentiment")
    result = classifier(text)
    return {"label": result[0]["label"], "score": result[0]["score"]}

app = FastAPI()

class Item(BaseModel):
    text: str

@app.get("/")
async def root():
    return {"message": "Sentiment tonality analyzer"}

@app.post("/analyze_sentiment")
def analyze_sentiment_api(item: Item):
    result = analyze_sentiment(item.text)
    return result
