import requests


def req(path,target_col):
    url = "http://localhost:8000/train"
    try:
        print(path,target_col)
        response = requests.post(url=url,json={"path": path, "target_col": target_col})
        print(type(response))
        print('-')
        print(response.text)
        # return {'status':response.status_code,'answer':response.json()}
        print(response.json())
        print(response.status_code)
        return {'status' : response.status_code , 'answer' : response.json()}
    except requests.exceptions.RequestException as e:
        print("Error", e)
        return e
