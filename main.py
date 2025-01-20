from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from routes.domain import domain_app
from routes.user import user
from routes.answer import ans_app
from routes.slots import slot_app
from routes.quiz_progress import quiz_app
from config import initialize

resources = initialize()
firebase_app = resources['firebase_app']
user_table = resources['user_table']
quiz_table = resources['quiz_table']
interview_table = resources['interview_table']
origins = [
    "http://localhost:5173",  
    "https://yourfrontenddomain.com",  
]

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins, 
    allow_credentials=True,
    allow_methods=["*"], 
    allow_headers=["*"],
)

app.mount("/user", user)
app.mount("/domain", domain_app)
app.mount("/answer", ans_app)
app.mount("/slots", slot_app)
app.mount("/quiz", quiz_app)

