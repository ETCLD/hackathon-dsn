from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Union

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Tests for later
class MetabaseFilter(BaseModel):
    departement: Union[str, None] = None
    siren: Union[str, None] = None
    year: Union[int, None] = None


@app.get("/")
def root():
    return {"Hello": "World"}

@app.post("/dashboard/")
def dashboard(filter: MetabaseFilter):
    return filter