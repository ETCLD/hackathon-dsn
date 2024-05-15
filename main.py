from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from datetime import datetime, timedelta
import jwt

METABASE_URL = "http://10.0.0.58:3000"
METABASE_SECRET_KEY = "9b4c5bcf5ac34b459f656da44588028c36d3d6cf1a8d3b419676fcbeee17bb58"
METABASE_DURATION = 600

app = FastAPI()

origins = [
    "http://10.0.0.58",
    "http://localhost",
    "http://localhost:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class MetabaseFilter(BaseModel):
    dashboard_id: int
    filters: dict


def make_metabase_iframe_response(filter: MetabaseFilter):
    """Generate metabase iframe"""
    expiration = datetime.now() + timedelta(seconds=METABASE_DURATION)

    payload = {
        "resource": {
            "dashboard": filter.dashboard_id
        },
        "params": filter.filters,
        "exp": round(datetime.timestamp(expiration))
    }

    token = jwt.encode(payload, METABASE_SECRET_KEY, algorithm="HS256")
    base_url = METABASE_URL + "/embed/dashboard/"

    return {
        "iframe_url": base_url + token + "#bordered=false&titled=false",
        "url_expiration": expiration
    }


@app.get("/")
def root():
    return {"Hello": "World"}

@app.post("/dashboard/")
def dashboard(filter: MetabaseFilter):
    return make_metabase_iframe_response(filter)
