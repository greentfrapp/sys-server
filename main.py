import json

import requests
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import PlainTextResponse

from schemas import VerificationRequest

app = FastAPI(openapi_url=None, docs_url=None, redoc_url=None)
origins = [
    "*",
    "http://0.0.0.0:8081",
    "http://localhost:8081",
    "http://127.0.0.1:8081",
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def get_index():
    return {"message": "success"}

@app.post("/", response_class=PlainTextResponse,)
def post_index(payload: VerificationRequest):
    if payload.challenge:
        return payload.challenge
    requests.post(
        "https://hooks.slack.com/services/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",
        headers={'Content-type': 'application/json'},
        json={
            "text": json.dumps(payload.event)
        },
    )
    return payload.challenge

@app.get("/ping")
def get_ping():
    return {"message": "pong"}
