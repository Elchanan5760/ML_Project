import requests

class Requests:
    def __init__(self,target_col):
        self.target_col = target_col
    def req_train(self):
        url = "http://localhost:8000/train"
        try:
            #print(self.path,self.target_col)
            response = requests.post(url=url,params={ "target_col": self.target_col})
            print(type(response))
            print('-')
            print(response.text)
            result = {'status':response.status_code,'answer':response.json()}
            print(response.json())
            print(response.status_code)
            return result
        except requests.exceptions.RequestException as e:
            print("Error", e)
            return e

    def req_classify(self,values):
        url = "http://localhost:8000/classify"
        try:
            #print(self.path, self.target_col)
            response = requests.post(
                url=url,
                json={
                        "target_col": self.target_col,
                        "my_values": values
                        }
            )

            print(type(response))
            print('-')
            print(response.json())
            result = {'status':response.status_code,'answer':response.json()}
            print(response.status_code)
            return result
        except requests.exceptions.RequestException as e:
            print("Error", e)
            return e
