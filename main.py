from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI()

class Song(BaseModel):
    name: str
    author: str
    genre: str

songs = []

@app.post("/songs/")
def create_song(song: Song):
    songs.append(song)
    return {  "message": "Song created successfully", "song": song.dict() }

