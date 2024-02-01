from typing import Union
from typing import List
from fastapi.staticfiles import StaticFiles
from fastapi import FastAPI, Response, Query
from fastapi.responses import HTMLResponse
from starlette.responses import FileResponse
import os
from model.ResultResponse import ResultResponse
from services.math_services import resolve 
from model.DemandsEnum import DemandsEnum

app = FastAPI(openapi_url=None)

@app.get("/sum")
def sum(list: List[float] = Query(True)):
    result = 0


    result = resolve(list, DemandsEnum.SUM)
    response = ResultResponse(list, result)
    
    

    return response


app.mount("/", StaticFiles(directory="public/docs", html=True), "public")

@app.get("/", response_class=HTMLResponse)
def root():
    return FileResponse("index.html")


