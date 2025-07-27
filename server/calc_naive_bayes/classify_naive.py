import pandas as pd

class Classify:
    def __init__(self,df):
        self.df = df
    def predict(self,dataframe_dict, target, my_values):
        print(my_values)
        dict_of_res = {}
        for variable in dataframe_dict.keys():
            res = 1
            print(dataframe_dict)
            for col in dataframe_dict[variable]:
                print(col)
                if col != target:
                    res *= dataframe_dict[variable][col][my_values[col]]
            dict_of_res[variable] = res
            print(f'{res} * ({(dataframe_dict[variable][target][variable])} / {(len(self.df) + len(dataframe_dict[variable][target]))}')
            dict_of_res[variable] = res * ((dataframe_dict[variable][target][variable]) / (len(self.df) + len(dataframe_dict[variable][target])-1))
        answer = ''
        num = 0
        for item in dict_of_res.items():
            if item[1] > num:
                num = item[1]
                answer = item[0]
        # print(my_values)
        # variable_list = []
        # dict_of_res = {}
        # for i, variable in enumerate(dataframe_dict.keys()):
        #     res = 1
        #     variable_list.append(variable)
        #     print(dataframe_dict)
        #     for j,col in enumerate(dataframe_dict[variable]):
        #         for val in dataframe_dict[variable][col].items():
        #             if col != target and my_values[j] == val[0]:
        #                 res *= (val[1] / (dataframe_dict[variable][target][variable] + (
        #                             len(dataframe_dict[variable][col])-1)))
        #     dict_of_res[variable] = res * (dataframe_dict[variable][target][variable] / (self.df[target].count() + len(dataframe_dict[variable][target])))
        return answer

