from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from priority_agent import run_priority_agent


app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def home():
    return {
        "message": "Priority+ API is running"
    }


@app.post("/analyze")
def analyze_patient(patient: dict):

    result = run_priority_agent(patient)

    return result