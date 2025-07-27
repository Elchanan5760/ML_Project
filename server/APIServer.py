from fastapi import FastAPI
# from utils import load_df
from pydantic import BaseModel
from server.calc_naive_bayes.model_coach import Train
from client.utils import load_df
from typing import Any
app = FastAPI()

class TrainRequest(BaseModel):
    target_col: str
    path : str

@app.post("/train")
async def post_train(req:TrainRequest):
    try:
        print(f"Loading data from: {req.path}")
        load = load_df.MyUtils()
        df = load.load_data(req.path)
        print(f"Data loaded, number of rows: {len(df)}")
        couch = Train(load.load_data(req.path),req.target_col)
        result = couch.calculate()
        print(f"Calculation result: {result}")
        return result
    except Exception as ex:
        print(ex)
        return ex

# @app.post('/classify'):
# def post_classify():
# @app.get("/train")
# def post_user():
#     try:
#         return