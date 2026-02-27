from menu.UI import Menu
import pandas as pd


if __name__ == "__main__":
    o1 = Menu(pd.read_csv(r'C:\Users\HOME\PycharmProjects\Naive_Bayes\server\Data\PlayTennis.csv'))
    o1.menu()
    # df = pd.read_csv('Data/PlayTennis.csv')
    # print(df)
    #
    # print(type(df.columns))







