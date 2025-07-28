import json
class OnJson:
    def save_in_json(self,dict_model): #TODO json_name
        try:
            json_object = json.dumps(dict_model, indent=4)
            with open(f"models.json", "w") as outfile:
                outfile.write(json_object)
        except Exception as ex:
            print(f"Error: {ex}")
    def read_json(self,json_name):
        try:
            with open(f"{json_name}.json", "r") as openfile:
                json_object = json.load(openfile)
                return json_object
        except Exception as ex:
            print(f"Error: {ex}")