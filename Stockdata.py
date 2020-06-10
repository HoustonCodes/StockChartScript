#!/usr/bin/env python
# coding: utf-8

from tkinter import *
#from PIL import ImageTK,Image
import numpy as np
import pandas as pd
from iexfinance.stocks import Stock
from datetime import datetime, timedelta
import matplotlib.pyplot as plt
from iexfinance.stocks import get_historical_data
import matplotlib.dates as mdates
import seaborn as sns

# Setting plot asthetics

sns.set(font_scale=1.5)
sns.set_style("whitegrid")

# set parameters so all plots are consistent

plt.rcParams['figure.figsize'] = (20,10)

#plt.style.use('fivethirtyeight')

#ax = add_subplot(111)
# TKINTER INTERFACE WIDGETS

root = Tk()
root.title("Houston's Stock Chart Program")
#root.iconbitmap('stock.ico')

#TKINTER ENTRY WIDGET

t = Entry(root, width=35, borderwidth= 10)

s = Entry(root, width=35, borderwidth= 10)

e = Entry(root, width=35, borderwidth= 10)

t.grid(row=0,column=0)

t.insert(END, "Enter the Ticker")

s.grid(row=1,column=0)

s.insert(END, "Enter the Start Date")

s.get()


e.grid(row=2,column=0)

e.insert(END, "Enter the End Date")

e.get()


def myClick2():
	
	#print("View Historical Information for the current stock():".format(tickerSymbol))
	
	

	global start

	global end 

	global tickerSymbol

	global df

	global sy

	global sm

	global sd

	global ey

	global em

	global ed


	#sy, sm, sd = eval((s.get()))
	
	#ey, em, ed = eval((e.get()))

	#start = datetime(sy, sm, sd)
	
	#end = datetime(ey, em, ed)

	#tickerSymbol = str(t.get())

	#df = get_historical_data(tickerSymbol, start, end, output_format="pandas", token = 'sk_f9f8cf318ae9428f899143cde56cb6c3')


def myClick():
	
	sy, sm, sd = eval((s.get()))
	
	ey, em, ed = eval((e.get()))
	
	start = datetime(sy, sm, sd)
	
	end = datetime(ey, em, ed)

	tickerSymbol = str(t.get())
	
	df = get_historical_data(tickerSymbol, start, end, output_format="pandas", token = 'sk_f9f8cf318ae9428f899143cde56cb6c3')

	plt.plot(df.index.values, df["close"], label=tickerSymbol)
	
	plt.ylabel("$ Price")
	
	plt.xlabel("date")

	plt.xticks(rotation=75)
	
	df["SMA1"] = df["close"].rolling(window=50).mean()
	
	df["SMA2"] = df["close"].rolling(window=100).mean()

	plt.plot(df["SMA1"], "g--", label="SMA1")
	
	plt.plot(df["SMA2"],"r--", label="SMA2")
	
	plt.legend()
	
	plt.title("Historical Stock Prices For: " + tickerSymbol)
	
	plt.show()

	#t.delete(0,END)
	#s.delete(0,END)
	#e.delete(0,END)



# Function applies bollinger bands.

def myClick2():

	sy, sm, sd = eval((s.get()))
	
	ey, em, ed = eval((e.get()))

	start = datetime(sy, sm, sd)
	
	end = datetime(ey, em, ed)

	tickerSymbol = str(t.get())

	df = get_historical_data(tickerSymbol, start, end, output_format="pandas", token = 'sk_f9f8cf318ae9428f899143cde56cb6c3')



	x_axis = df.index.get_level_values(0)


	plt.plot(df.index.values,df["close"],"b", Label=tickerSymbol)

	plt.ylabel("$ Price")
	
	plt.xlabel("date")

	#plt.xtick(75)

	df["30 Day MA"] = df["close"].rolling(window=20).mean()

	df["30 Day STD"] = df["close"].rolling(window=20).std()

	df["Upper Band"] = df["30 Day MA"] + (df["30 Day STD"] * 2)

	df["Lower Band"] = df["30 Day MA"] - (df["30 Day STD"] * 2)

	plt.plot(df[["close", "30 Day MA","Upper Band","Lower Band"]])

	plt.plot(df["30 Day MA"],"--", label="30 Day MA")

	plt.plot(df["Upper Band"],"r", label="Upper Band")

	plt.plot(df["Lower Band"],"g", label="Lower Band")

	plt.fill_between(x_axis,df["Upper Band"], df["Lower Band"],color="grey")

	plt.title(tickerSymbol+ " Chart with Bollinger Bands")

	plt.legend()

	plt.xticks(rotation=75)

	plt.ylabel("$ Price")

	plt.show()

	#t.delete(0,END)
	#s.delete(0,END)
	#e.delete(0,END)

def myClick3():

	sy, sm, sd = eval((s.get()))
	
	ey, em, ed = eval((e.get()))

	start = datetime(sy, sm, sd)
	
	end = datetime(ey, em, ed)

	tickerSymbol = str(t.get())

	df = get_historical_data(tickerSymbol, start, end, output_format="pandas", token = 'sk_f9f8cf318ae9428f899143cde56cb6c3')


	plt.subplot(1, 2, 1)

	plt.plot(df.index.values, df["close"], label=tickerSymbol)
	
	plt.ylabel("$ Price")
	
	plt.xlabel("date")

	plt.xticks(rotation=75)
	
	df["SMA1"] = df["close"].rolling(window=50).mean()
	
	df["SMA2"] = df["close"].rolling(window=100).mean()

	plt.plot(df["SMA1"], "g--", label="SMA1")
	
	plt.plot(df["SMA2"],"r--", label="SMA2")
	
	plt.legend()
	
	plt.title("Historical Stock Prices For: " + tickerSymbol)
	

	plt.subplot(1, 2, 2)


	df["30 Day MA"] = df["close"].rolling(window=20).mean()

	df["30 Day STD"] = df["close"].rolling(window=20).std()

	df["Upper Band"] = df["30 Day MA"] + (df["30 Day STD"] * 2)

	df["Lower Band"] = df["30 Day MA"] - (df["30 Day STD"] * 2)

	plt.plot(df[["close", "30 Day MA","Upper Band","Lower Band"]])

	plt.plot(df["30 Day MA"],"--", label="30 Day MA")

	plt.plot(df["Upper Band"],"r", label="Upper Band")

	plt.plot(df["Lower Band"],"g", label="Lower Band")

	x_axis = df.index.get_level_values(0)
	
	plt.fill_between(x_axis,df["Upper Band"], df["Lower Band"],color="grey")

	plt.title(tickerSymbol+ " Chart with Bollinger Bands")

	plt.legend()

	plt.ylabel("$ Price")

	plt.xticks(rotation = 75)

	graph1 = plt.show()

	

	graph1.pack()

	


myButton = Button(root, text="Chart with SMA", command=myClick, padx=30.1,pady=20, borderwidth=4 , bg="white",fg="black")

myButton2 = Button(root, text="Chart With Bollinger Bands", command=myClick2, pady=20,borderwidth=4 , bg="white",fg="black")

myButton3 = Button(root, text="Compare Charts", command=myClick3, padx=29.2,pady=20, borderwidth=4, bg="white", fg="black")

myButton_quit = Button(root, text="quit",command=root.quit)



myButton.grid(row=3,column=0)
myButton2.grid(row=4,column=0)
myButton3.grid(row=5,column=0)
myButton_quit.grid(row=6,column=0)


#root.geometry("500x500")

root.mainloop()



#root.minsize(width=1920, height=1080)

#tickerSymbol = input("Ticker Symbol: ")
#companyInfo = Stock(tickerSymbol, token ='sk_f9f8cf318ae9428f899143cde56cb6c3')
#stockPrice = companyInfo.get_price()


# In[3]:


#print("Current Stock Price:", stockPrice,"\n")
#print("View Historical Information for the current stock():".format(tickerSymbol))
#sy, sm, sd = eval(input("input start date as yyyy,m,d: "))
#ey, em, ed = eval(input("end date as yyyy,m,d:"  ))


#stockPrice = companyInfo.get_price()

#start = datetime(sy, sm , sd)
#end = datetime(ey, em, ed)

#df = get_historical_data(tickerSymbol, start, end, output_format='pandas', token = 'sk_f9f8cf318ae9428f899143cde56cb6c3')


#plt.plot(df.index.values, df.close,'-p')
#plt.ylabel('$ Price')
#plt.xlabel('date')
#df["SMA1"] = df.close.rolling(window=50).mean()
#df["SMA2"] = df.close.rolling(window=200).mean()
#plt.plot(df['SMA1'], 'g--', label="SMA1")
#plt.plot(df['SMA2'],'r--', label="SMA2")
#plt.legend()
#plt.title("Historical Stock Prices For: " + tickerSymbol)

#plt.show()


# In[ ]:




