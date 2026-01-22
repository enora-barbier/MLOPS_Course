from typing import Union

from fastapi import FastAPI

app = FastAPI()


@app.get("/{surface}")
def read_item(surface: int):
    return {"surface": surface}
