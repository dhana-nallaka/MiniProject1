###CREATING CRYPTOCURRENCY PORFOLIO MANAGER WITH COINMARKETCAP API AND SQLUTE3 DATABASE
# 1. requests-->send requests and get the data
# 2.json-->pass the data
import requests
import json

#tkinter is used for GUI here there are 3 steps
# 1.Create instance of tkinter
# 2.Add all the widgets
# 3.Close the mainloop
import sqlite3
from tkinter import *
from tkinter import messagebox,Menu


pycrypto=Tk()#creating instance
pycrypto.title("My Crypto Portfolio")
pycrypto.iconbitmap('favicon.ico')

con=sqlite3.connect('coin.db')
cursorobj=con.cursor()

cursorobj.execute("CREATE TABLE IF NOT EXISTS coin(id INTEGER PRIMARY KEY, symbol TEXT, amount INTEGER, price REAL)")
con.commit()


def reset():

            #destroys each frame
            for frame in pycrypto.winfo_children():
                frame.destroy()

            app_navi()
            app_header()
            my_portfolio()

def app_navi():
        def clearall():
            cursorobj.execute("DELETE FROM coin")
            con.commit()

            messagebox.showinfo("Portfolio Notification","Portfolio CLeared!")
            reset()

        def closeapp():
            pycrypto.destroy()

        menu_app=Menu(pycrypto)
        fileitem=Menu(menu_app)
        fileitem.add_command(label="Clear Portfolio",command=clearall)
        fileitem.add_command(label="Close app",command=closeapp)
        menu_app.add_cascade(label="File",menu=fileitem)
        pycrypto.config(menu=menu_app)



def my_portfolio():
        api_request=requests.get("https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest?start=1&limit=30&convert=USD&CMC_PRO_API_KEY=0c69614a-ec8c-46a3-92b0-8e994f3f5a26")
        api=json.loads(api_request.content) #to deliver the content of API request
        cursorobj.execute("SELECT * from coin")
        coins=cursorobj.fetchall()

        def font_color(amount):
                    if amount>0:
                        return "green"
                    else:
                        return "red"


        def insert_coin():
                    cursorobj.execute("INSERT INTO coin(symbol,price,amount) VALUES(?,?,?)",(symbol_txt.get(), price_txt.get(), amount_txt.get()))
                    con.commit()

                    messagebox.showinfo("Portfolio Notification","Coin Added Successfully")#title,notification
                    reset()


        def update_coin():
                    cursorobj.execute("UPDATE coin set symbol=?, price=?, amount=? WHERE id=?",(symbol_update.get(),price_update.get(),amount_update.get(),portfolio_id_update.get()))
                    con.commit()

                    messagebox.showinfo("Portfolio Notification","Coin Updated Successfully")
                    reset()


        def delete_coin():
                    cursorobj.execute("DELETE FROM coin where id=?",(id_delete.get()))
                    con.commit()

                    messagebox.showinfo("Portfolio Notification","Coin Deleted Successfully")
                    reset()




        ro=0
        total_pl=0
        total_curval=0
        total_amount_paid=0
        for i in range(0,5):
            #to get only coins that I invested
            for coin in coins:
                if api["data"][i]["symbol"]==coin[1]:
                    total_amount=coin[2]*coin[3]
                    current_value=coin[2]*api["data"][i]["quote"]["USD"]["price"]
                    #profit or loss per coin
                    pl_coin=api["data"][i]["quote"]["USD"]["price"]-coin[3]
                    #total profit or LOSS for each coin
                    total_pl_coin=pl_coin*coin[2]
                    #total profit or loss for all coins
                    total_pl+=total_pl_coin
                    total_curval+=current_value
                    total_amount_paid+=total_amount

                    ro+=1

                    pofid=Label(pycrypto,text=coin[0],bg="#F3F4F6",fg="black",font="Lato 12",padx="5",pady="5",borderwidth=2,relief="groove") #creating label
                    pofid.grid(row=ro,column=0,sticky=N+S+E+W)#placing label at 0,0

                    name=Label(pycrypto,text=api["data"][i]["symbol"],bg="#F3F4F6",fg="black",font="Lato 12",padx="5",pady="5",borderwidth=2,relief="groove") #creating label
                    name.grid(row=ro,column=1,sticky=N+S+E+W)#placing label at 0,1

                    price=Label(pycrypto,text="${0:.2f}".format(api["data"][i]["quote"]["USD"]["price"]),bg="#F3F4F6",fg="black",font="Lato 12",padx="5",pady="5",borderwidth=2,relief="groove") #creating label
                    price.grid(row=ro,column=2,sticky=N+S+E+W)#placing label at 0,2

                    no_coins=Label(pycrypto,text=coin[2],bg="#F3F4F6",fg="black",font="Lato 12",padx="5",pady="5",borderwidth=2,relief="groove") #creating label
                    no_coins.grid(row=ro,column=3,sticky=N+S+E+W)#placing label at 0,3

                    amount_paid=Label(pycrypto,text="${0:.2f}".format(total_amount),bg="#F3F4F6",fg="black",font="Lato 12",padx="5",pady="5",borderwidth=2,relief="groove") #creating label
                    amount_paid.grid(row=ro,column=4,sticky=N+S+E+W)#placing label at 0,4

                    cur_val=Label(pycrypto,text="${0:.2f}".format(current_value),bg="#F3F4F6",fg="black",font="Lato 12",padx="5",pady="5",borderwidth=2,relief="groove") #creating label
                    cur_val.grid(row=ro,column=5,sticky=N+S+E+W)#placing label at 0,5

                    pl_coin=Label(pycrypto,text="${0:.2f}".format(pl_coin),bg="#F3F4F6",fg=font_color(float("{0:.2f}".format(pl_coin))),font="Lato 12",padx="5",pady="5",borderwidth=2,relief="groove") #creating label
                    pl_coin.grid(row=ro,column=6,sticky=N+S+E+W)#placing label at 0,6

                    total_prl=Label(pycrypto,text="${0:.2f}".format(total_pl_coin),bg="#F3F4F6",fg=font_color(float("{0:.2f}".format(total_pl_coin))),font="Lato 12",padx="5",pady="5",borderwidth=2,relief="groove") #creating label
                    total_prl.grid(row=ro,column=7,sticky=N+S+E+W)#placing label at 0,7

        #Printing final profit or loss
        ro+=1

        #to take input we have method Entry

        ###################Insert a Coin######################

        symbol_txt=Entry(pycrypto, borderwidth=2, relief="groove")
        symbol_txt.grid(row=ro+1,column=1)

        price_txt=Entry(pycrypto, borderwidth=2, relief="groove")
        price_txt.grid(row=ro+1,column=2)

        amount_txt=Entry(pycrypto, borderwidth=2, relief="groove")
        amount_txt.grid(row=ro+1,column=3)

        addcoin_button=Button(pycrypto,text="ADD COIN",bg="#142E54",command=insert_coin, fg="white",font="Lato 12",padx="5",pady="5",borderwidth=2,relief="groove") #creating label
        addcoin_button.grid(row=ro+1,column=4,sticky=N+S+E+W)


        #############Update a COIN#############


        portfolio_id_update=Entry(pycrypto, borderwidth=2, relief="groove")
        portfolio_id_update.grid(row=ro+2,column=0)

        symbol_update=Entry(pycrypto, borderwidth=2, relief="groove")
        symbol_update.grid(row=ro+2,column=1)

        price_update=Entry(pycrypto, borderwidth=2, relief="groove")
        price_update.grid(row=ro+2,column=2)

        amount_update=Entry(pycrypto, borderwidth=2, relief="groove")
        amount_update.grid(row=ro+2,column=3)

        updatecoin_button=Button(pycrypto,text="UPDATE COIN",bg="#142E54",command=update_coin, fg="white",font="Lato 12",padx="5",pady="5",borderwidth=2,relief="groove") #creating label
        updatecoin_button.grid(row=ro+2,column=4,sticky=N+S+E+W)


      ###############Delete a COIN###############
        id_delete=Entry(pycrypto, borderwidth=2, relief="groove")
        id_delete.grid(row=ro+3,column=0)

        deletecoin_button=Button(pycrypto,text="DELETE COIN",bg="#142E54",command=delete_coin, fg="white",font="Lato 12",padx="5",pady="5",borderwidth=2,relief="groove") #creating label
        deletecoin_button.grid(row=ro+3,column=4,sticky=N+S+E+W)


        ###total amounts display###

        total_amount_paid=Label(pycrypto,text="${0:.2f}".format(total_amount_paid),bg="#F3F4F6",fg="black",font="Lato 12",padx="5",pady="5",borderwidth=2,relief="groove") #creating label
        total_amount_paid.grid(row=ro,column=4,sticky=N+S+E+W)

        total_prl=Label(pycrypto,text="${0:.2f}".format(total_pl),bg="#F3F4F6",fg=font_color(float("{0:.2f}".format(total_pl))),font="Lato 12",padx="5",pady="5",borderwidth=2,relief="groove") #creating label
        total_prl.grid(row=ro,column=7,sticky=N+S+E+W)#placing label at 0,6

        total_cv=Label(pycrypto,text="${0:.2f}".format(total_curval),bg="#F3F4F6",fg="black",font="Lato 12",padx="5",pady="5",borderwidth=2,relief="groove") #creating label
        total_cv.grid(row=ro,column=5,sticky=N+S+E+W)

        api=""

        #refresh Button

        update_button=Button(pycrypto,text="REFRESH",bg="#142E54",command=reset, fg="white",font="Lato 12",padx="5",pady="5",borderwidth=2,relief="groove") #creating label
        update_button.grid(row=ro+1,column=6,sticky=N+S+E+W)

####HEADER#####
def  app_header():

    portfolio_id=Label(pycrypto,text="Portfolio ID",bg="#142E54",fg="white",font="Lato 12 bold",padx="5",pady="5",borderwidth=2,relief="groove") #creating label
    portfolio_id.grid(row=0,column=0,sticky=N+S+E+W)#placing label at 0,0

    name=Label(pycrypto,text="Coin Name",bg="#142E54",fg="white",font="Lato 12 bold",padx="5",pady="5",borderwidth=2,relief="groove") #creating label
    name.grid(row=0,column=1,sticky=N+S+E+W)#placing label at 0,1

    price=Label(pycrypto,text="Price",bg="#142E54",fg="white",font="Lato 12 bold",padx="5",pady="5",borderwidth=2,relief="groove") #creating label
    price.grid(row=0,column=2,sticky=N+S+E+W)#placing label at 0,2

    no_coins=Label(pycrypto,text="Coins Owned",bg="#142E54",fg="white",font="Lato 12 bold",padx="5",pady="5",borderwidth=2,relief="groove") #creating label
    no_coins.grid(row=0,column=3,sticky=N+S+E+W)#placing label at 0,3

    amount_paid=Label(pycrypto,text="Total Amount Paid",bg="#142E54",fg="white",font="Lato 12 bold",padx="5",pady="5",borderwidth=2,relief="groove") #creating label
    amount_paid.grid(row=0,column=4,sticky=N+S+E+W)#placing label at 0,4

    cur_val=Label(pycrypto,text="Current Value",bg="#142E54",fg="white",font="Lato 12 bold",padx="5",pady="5",borderwidth=2,relief="groove") #creating label
    cur_val.grid(row=0,column=5,sticky=N+S+E+W)#placing label at 0,5

    pl_coin=Label(pycrypto,text="Profit or Loss per coin",bg="#142E54",fg="white",font="Lato 12 bold",padx="5",pady="5",borderwidth=2,relief="groove") #creating label
    pl_coin.grid(row=0,column=6,sticky=N+S+E+W)#placing label at 0,6

    total_prl=Label(pycrypto,text="Total P/L with Coin",bg="#142E54",fg="white",font="Lato 12 bold",padx="5",pady="5",borderwidth=2,relief="groove") #creating label
    total_prl.grid(row=0,column=7,sticky=N+S+E+W)#placing label at 0,7



app_navi()
app_header()
my_portfolio()
pycrypto.mainloop()#creating mainloop
cursorobj.close()
con.close()
