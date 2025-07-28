import random
from tarfile import data_filter

from .classify_naive import Classify
from .model_coach import Train

class Check:
    def __init__(self,df):
        self.df = df
    def check_data(self,present,target):
        classify = Classify(self.df)
        my_list = []
        index_dict = {}
        count = 0
        while count < present:
            rn = random.randint(0,len(self.df)-1)
            if not rn in my_list:
                count += 1
                my_list.append(rn)
                index_dict[rn] = self.df.iloc[rn].tolist()
        on_what = self.df.iloc[~self.df.index.isin(my_list)]
        train = Train(on_what)
        dataframe_dict = train.create_counter(target)
        is_right = 0
        for key,list_val in index_dict.items():
            dict_res = classify.calculate(dataframe_dict, target, list_val)
            maxi = ''
            for item in dict_res.items():
                if maxi == '':
                    maxi = item[0]
                if maxi in dict_res.keys():
                    if item[1] > dict_res[maxi]:
                        maxi = item[0]
            if maxi == self.df.loc[key,target]:
                is_right += 1
        print(f'{(is_right / present) * 100}%')
        return is_right / present
