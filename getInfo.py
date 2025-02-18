from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI()

@app.get("/info/")
def get_info():
    return { "Nombre": "Diego Facundo Pérez Nicolau", "Carnet": "202106538"}