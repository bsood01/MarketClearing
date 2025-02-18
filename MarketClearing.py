import pandas as pd 
import csv
import os

def get_market_dict(combi_df,schedule_df):
    dict={"Day":[],"Schedule":[],"Price":[],"Quantity":[]}

    for index, row in combi_df.iterrows():
        if type(row["Number"])==int and type(row["Schedule"])==int :
            try:
                price_list=schedule_df.loc[:,row["Schedule"]]["Price"].to_list()
                quantity_list=schedule_df.loc[:,row["Schedule"]]["Quantity"].to_list()
                length=len(price_list)
                if len(quantity_list)==length:
                    day_list= [row["Number"]]*length
                    schedule_list=[row["Schedule"]]*length
                    dict["Day"]=dict["Day"]+day_list
                    dict["Schedule"]=dict["Schedule"] + schedule_list
                    dict["Price"]=dict["Price"] + price_list
                    dict["Quantity"]=dict["Quantity"] + quantity_list
                    
                else: 
                    print(f'Price and Quantity curve don\'t match on schedule {row["Schedule"]}. Day {row["Number"]} skipped.')
            except KeyError as e:
                print(f'Invalid KeyError on schedule {row["Schedule"]} ({e}). Day {row["Number"]} skipped.')
                continue
    return dict


def main():
    combi_df= pd.read_excel('MarketSchedule.xlsx', sheet_name='Combinations')
    for i in combi_df.iterrows():
        print(i[0])
    #schedule_df = pd.read_excel('MarketSchedule.xlsx', header=[0, 1], sheet_name='Schedules')
    #res=get_market_dict(combi_df,schedule_df)
    #result_df = pd.DataFrame.from_dict(res,orient='index').transpose()
    #result_df.to_csv("result.csv", encoding='utf-8',index=False)


if __name__ == '__main__':
    main()
