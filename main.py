from typing import Union
from fastapi.staticfiles import StaticFiles
from fastapi import FastAPI, Response
from fastapi.responses import HTMLResponse
from starlette.responses import FileResponse
import os

app = FastAPI(openapi_url=None)
app.mount("/", StaticFiles(directory="public/docs", html=True), "public")

@app.get("/", response_class=HTMLResponse)
def read_root():
    return FileResponse("./public/docs/index.html")

