
from client.my_app.request.my_request import Requests


class Menu:
    def __init__(self,df):
        self.df = df
        self.request = Requests(self.df.columns[-1])
    def menu(self):
        cond = True
        while cond:
            print('=======Menu=======')
            navigation = input(f"1. Your values\n"
                               f"2. Check data\n"
                               f"0. Exit\n")
            if navigation == '1':
                self.choose_values()
            elif navigation == '2':
                self.choice_check_data()
            elif navigation == '0':
                cond = False
            else:
                print("Invalid value\n"
                      "Please try again!")
    def get_train(self):
        cond = False
        columns = self.df.columns.tolist()
        col_not_target = []
        target = ''
        while not cond:
            print("What is your target:")
            options = []
            for i,col in enumerate(columns):
                options.append(f'{i+1}')
                print(f"{i+1}. {col}")
            target = input()
            if target in options:
                cond = True
                column_to_skip = int(target)-1
                col_not_target = [feature for feature in columns if feature != columns[column_to_skip]]
            if not cond:
                print('Invalid value\n'
                      'Please try again!')
        self.request = Requests(
                                columns[int(target) - 1])
        result = self.request.req_train()
        print(result)
        return result,col_not_target

    def choose_values(self):
        train = self.get_train()
        col_not_target = train[1]
        count = 0
        values = {}
        while count < len(col_not_target):
            possible_values = self.df[col_not_target[count]].unique().tolist()
            print(f"What the {col_not_target[count]}:")
            options = []
            for i,val in enumerate(possible_values):
                print(f"{i+1}. {val}")
                options.append(f'{i+1}')
            choice = input()
            if choice in options:
                values[col_not_target[count]] = possible_values[int(choice)-1]
                count += 1
                print(values)
                print(possible_values[int(choice)-1])
                print(type(possible_values[int(choice)-1]))
            else:
                print('Invalid value\n'
                      'Please try again!')
        res = self.request.req_classify(values)
        print(res)
        print(type(res))
        maxi = 0
        answer = ''
        for k,v in res['answer'].items():
            if v > maxi:
                maxi = v
                answer = k
        print(f'The answer is {answer}')
        return answer


    # def choice_check_data(self,target):
    #     cond = True
    #     while cond:
    #         print('What percentage do you want to check?')
    #         present = input()
    #         if present.isdigit():
    #             present = float(present)
    #             if present > 0 and present < 100:
    #                 cond = False
    #             else:
    #                 print('Invalid value\n'
    #                       'Please try again!')
    #         else:
    #             print('Invalid value\n'
    #                  'Please try again!')
    #     check = Check(self.df)
    #     accuracy = check.check_data(present, target)
        # check = Check(self.df)
        # cond = True
        # from_data = ''
        # target = ''
        # while cond:
        #     print(f"What is your target line:")
        #     for i,col in enumerate(self.df.columns):
        #         print(f'{i+1}. {col}')
        #     target = input()
        #     from_data = input(f"How many from {len(self.df)} do you want to check:\n")
        #     if target.isdigit() and from_data.isdigit():
        #         from_data = int(from_data)
        #         target = int(target)
        #         if from_data < len(self.df) and target <= len(self.df.columns):
        #             cond = False
        #         else:
        #             print('Invalid value\n'
        #                   'Please try again!')
        #     else:
        #         print('Invalid value\n'
        #               'Please try again!')
        # check.check_data(from_data,self.df.columns.tolist()[target-1])

# o1 = Check(pd.read_csv('phishing.csv'))
# o1.check_data(3300,'class')