import json
import os

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
    webhook = os.environ.get("GENERAL_WEBHOOK")
    if webhook:
        requests.post(
            webhook,
            headers={'Content-type': 'application/json'},
            json={
                "text": json.dumps(payload.event).replace("@", "") # Remove @ to prevent feedback loop
            },
        )
    return payload.challenge

@app.get("/ping")
def get_ping():
    return {"message": "pong"}
