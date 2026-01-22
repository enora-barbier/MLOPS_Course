from typing import Union

from fastapi import FastAPI

app = FastAPI()


@app.get("/{surface}")
def read_item(surface: int):
    return {"surface": surface}

# Export the function for direct import
def get_surface_direct(surface: int):
    return {"surface": surface}
