#----------------------------------------------------------
#import module
#----------------------------------------------------------
import pandas as pd
import datetime
import pandas_datareader.data as web
#----------------------------------------------------------
#pathの設定
#----------------------------------------------------------
data_path = '../data/'
result_path = '../result/'
#----------------------------------------------------------
#define function
#----------------------------------------------------------
def get_stockprice(code_list, start, end):
    price_list = []
    for code in code_list:
        df_price = web.DataReader([str(code) + '.JP'], 'stooq', start, end)
        price_list.append(df_price)
        df_price.to_csv(result_path + str(code) + '_JP.csv', index=False)
    price_dic = dict(zip(code_list, price_list))
    return price_dic
#----------------------------------------------------------
#input file name
#----------------------------------------------------------
print('file name?')
filename = input('filename: ')
df_company = pd.read_csv(data_path + filename + '.csv')
code_list = list(df_company['コード'])
#----------------------------------------------------------
#input start time
#----------------------------------------------------------
print('start year?')
start_year = input('start year: ')
print('start month?')
start_month = input('start month: ')
print('start day?')
start_day = input('start day: ')
start = datetime.date(start_year,start_month,start_day)
end = datetime.date.today()
#----------------------------------------------------------
#処理の決定
#----------------------------------------------------------
answer = input('Are you sure? (y/n): ')
if (answer != 'y' and answer != 'Y'):
    sys.exit(1)
print('処理を継続します')
get_stockprice(code_list, start, end)
#----------------------------------------------------------
