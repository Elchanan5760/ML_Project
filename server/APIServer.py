from fastapi import FastAPI
from json_models.into_json import OnJson
from starlette.responses import JSONResponse
from calc_naive_bayes.classify_naive import Classify
from calc_naive_bayes.model_coach import Train
from utils import load_df
from json_models.into_json import OnJson
app = FastAPI()
jsons = OnJson()


@app.post("/train")
def post_train(target_col: str):
    try:
        #print(f"Loading data from: {path}")
        load = load_df.Util()
        df = load.load_data()
        print(f"Data loaded, number of rows: {len(df)}")
        couch = Train(df,target_col)
        result = couch.calculate()
        print(f"Calculation result: {result}")
        jsons.save_in_json(result)
        return JSONResponse(content=result)
    except Exception as ex:
        print(ex)
        return ex

# @my_app.post('/classify')
# def post_classify(data:dict target_col: str,path : str,model:dict,my_values:dict):
#     try:
#         load = load_df.Util()
#         df = load.load_data(path)
#         classify = Classify(df)
#         result = classify.predict(model,target_col,my_values)
#         return JSONResponse(content=result)
#     except Exception as ex:
#         print(ex)
#         return ex

@app.post('/classify')
def post_classify(data:dict):
    # target_col: str,path : str,model:dict,my_values:dict
    try:
        load = load_df.Util()
        df = load.load_data()
        classify = Classify(df)
        result = classify.predict(jsons.read_json('models'),data["target_col"],data["my_values"])
        return result
    except Exception as ex:
        print(ex)
        return ex
# @my_app.get("/train")
# def post_user():
#     try:
#         return