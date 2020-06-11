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
import seaborn

	# Setting plot asthetics

seaborn.set(font_scale=1.5)
seaborn.set_style("whitegrid")

	# set parameters so all plots are consistent

plt.rcParams['figure.figsize'] = (20,10)


	# TKINTER INTERFACE WIDGETS

root = Tk()
root.title("Houston's Stock Chart Program")
	#root.iconbitmap('stock.ico')


	#TKINTER ENTRY WIDGET

ticker = Entry(root, width=35, borderwidth= 10)

start_date = Entry(root, width=35, borderwidth= 10)

end_date = Entry(root, width=35, borderwidth= 10)

ticker.grid(row=0,column=0)

ticker.insert(END, "Enter the Ticker")

start_date.grid(row=1,column=0)

start_date.insert(END, "Enter the Start Date YYYY,M,D")

start_date.get()

end_date.grid(row=2,column=0)

end_date.insert(END, "Enter the End Date YYYY,M,D")

end_date.get()


	# Function applies SMA

def myClick():
	
	start_year, start_month, start_day = eval((start_date.get()))
	
	end_year, end_month, end_day = eval((end_date.get()))
	
	start = datetime(start_year, start_month, start_day)
	
	end = datetime(end_year, end_month, end_day)

	tickerSymbol = str(ticker.get())
	
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



	# Function applies bollinger bands

def myClick2():

	start_year, start_month, start_day = eval((start_date.get()))
	
	end_year, end_month, end_day = eval((end_date.get()))

	start = datetime(start_year, start_month, start_day)
	
	end = datetime(end_year, end_month, end_day)

	tickerSymbol = str(ticker.get())

	df = get_historical_data(tickerSymbol, start, end, output_format="pandas", token = 'sk_f9f8cf318ae9428f899143cde56cb6c3')

	x_axis = df.index.get_level_values(0)

	plt.plot(df.index.values,df["close"],"b", Label=tickerSymbol)

	plt.ylabel("$ Price")
	
	plt.xlabel("date")

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


 	# Function compares the 2 charts 

def myClick3():

	start_year, start_month, start_day = eval((start_date.get()))
	
	end_year, end_month, end_day = eval((end_date.get()))

	start = datetime(start_year, start_month, start_day)
	
	end = datetime(end_year, end_month, end_day)

	tickerSymbol = str(ticker.get())

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

	plt.show()

	



	


myButton = Button(root, text="Chart with SMA", command=myClick, padx=30.1,pady=20, borderwidth=4 , bg="white",fg="black")

myButton2 = Button(root, text="Chart With Bollinger Bands", command=myClick2, pady=20,borderwidth=4 , bg="white",fg="black")

myButton3 = Button(root, text="Compare Charts", command=myClick3, padx=29.2,pady=20, borderwidth=4, bg="white", fg="black")

myButton_quit = Button(root, text="quit",command=root.quit)



myButton.grid(row=3,column=0)
myButton2.grid(row=4,column=0)
myButton3.grid(row=5,column=0)
myButton_quit.grid(row=6,column=0)




root.mainloop()





