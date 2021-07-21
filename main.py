from wiki_scrape import get_wiki_summary
from fastapi import FastAPI
import json

app = FastAPI()

@app.get("/")
async def root(query: str):
    # print(query)
    data = get_wiki_summary(query)
    json_summary = json.dumps(data)
    return {"summary": json_summary}