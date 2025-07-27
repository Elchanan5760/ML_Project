from fastapi import FastAPI
# from utils import load_df
from pydantic import BaseModel
from starlette.responses import JSONResponse
from calc_naive_bayes.classify_naive import Classify
from server.calc_naive_bayes.model_coach import Train
from client.utils import load_df
from typing import Any
app = FastAPI()

class TrainRequest(BaseModel):
    target_col: str
    path : str

@app.post("/train")
def post_train(req:TrainRequest):
    print(req.target_col)
    try:
        print(f"Loading data from: {req.path}")
        load = load_df.MyUtils()
        df = load.load_data(req.path)
        print(f"Data loaded, number of rows: {len(df)}")
        couch = Train(df,req.target_col)
        result = couch.calculate()
        print(f"Calculation result: {result}")
        return JSONResponse(content=result)
    except Exception as ex:
        print(ex)
        return ex

@app.post('/classify')
def post_classify(req:TrainRequest,model:dict,my_values:dict):
    try:
        load = load_df.MyUtils()
        df = load.load_data(req.path)
        classify = Classify(df)
        result = classify.predict(model,req.target_col,my_values)
        return JSONResponse(content=result)
    except Exception as ex:
        print(ex)
        return ex
# @app.get("/train")
# def post_user():
#     try:
#         return