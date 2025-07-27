from client.menu.UI import Menu
from client.utils.load_df import MyUtils
#from APIServer import

if __name__ == "__main__":
    util = MyUtils()
    o1 = Menu(util.load_data(r'C:\Users\HOME\PycharmProjects\Naive_Bayes\server\Data\PlayTennis.csv'))
    o1.menu()
    # df = pd.read_csv('Data/PlayTennis.csv')
    # print(df)
    #
    # print(type(df.columns))







