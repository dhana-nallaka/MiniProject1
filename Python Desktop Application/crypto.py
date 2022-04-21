import requests
import json
api_request=requests.get("https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest?start=1&limit=5&convert=USD&CMC_PRO_API_KEY=0c69614a-ec8c-46a3-92b0-8e994f3f5a26")
#using free API
#api_request=requests.get("https://api.coinmarketcap.com/v1/ticker/")

#use json to get parsable data

api=json.loads(api_request.content) #to deliver the content of API request



# #printing symbol
# print(api["data"][0]["symbol"])
# #printing price
# #print(api["data"][0]["quote"]["USD"]["price"])
# #formatting 2 decimals
# print("{0:.2f}".format(api["data"][0]["quote"]["USD"]["price"]))
print()
print("--------------------------------------------------------------------------------")
print("------------------PROFIT OR LOSS ESTIMATION USING COINMARKETCAP API-------------")
coins=[
  {
     "symbol":'BTC',
     "amount_owned":2,
     "price":3200.42
  },
  {
   "symbol":'ETH',
   "amount_owned":6,
   "price":3300.32
  }
]

#to fetch the 5 details
total_pl=0
for i in range(0,5):
    #to get only coins that I invested
    for coin in coins:
        if api["data"][i]["symbol"]==coin["symbol"]:
            total_amount=coin["amount_owned"]*coin["price"]
            current_value=coin["amount_owned"]*api["data"][i]["quote"]["USD"]["price"]
            #profit or loss per coin
            pl_coin=api["data"][i]["quote"]["USD"]["price"]-coin["price"]
            #total profit or LOSS for each coin
            total_pl_coin=pl_coin*coin["amount_owned"]
            #total profit or loss for all coins
            total_pl+=total_pl_coin

            #formatting Printing
            print()
            print()
            #to the name and symbol from the json data
            print(api["data"][i]["name"] + "-" +api["data"][i]["symbol"])
            #to get the price of each coin on the top 5
            print("Price -  ${0:.2f}".format(api["data"][i]["quote"]["USD"]["price"]))
            #number of coins we have
            print("Number of Coins owned -  ",coin["amount_owned"])
            #total amount for each coin that is invested
            print("Total Amount Paid -  ${0:.2f}".format(total_amount))
            #Current value
            print("Current Value -   ${0:.2f}".format(current_value))
            print("Profit or Loss per coin -  ${0:.2f}".format(pl_coin))
            print("Total Profit or Loss for each coin -  ${0:.2f}".format(total_pl_coin))

#Printing final profit or loss
print()
print("--------------------------------------------------------------")
print()
print("Total Profit or Loss for all coins -  ${0:.2f}".format(total_pl))
