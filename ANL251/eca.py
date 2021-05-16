# This is created on a ipython, so dont mind the weird flow of code

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from scipy import stats
import datetime
import matplotlib.pyplot as plt

df1 = pd.read_csv('OutputFile_hotelStats_2.csv')
df2 = pd.read_csv('OutputFile_hotelStayDays_2.csv')
df3 = pd.read_csv('OutputFile_TOURISMRECEIPTS_2.csv')
df4 = pd.read_csv('OutputFile_tourismVisitors_2.csv')

df1.head()  
# Will be useless on a py script. Will show the preview if run on a ipython notebook
#------------------------------------------------------------------------------------------------

fig, ax = plt.subplots(figsize=(15, 15))

# Add x-axis and y-axis
ax.plot(df1['Variables'],df1['Standard Average Hotel Occupancy Rate (Percent)'],color='purple', label='Average across all hotels')
ax.plot(df1['Variables'],df1['Average Hotel Occupancy Rate - Hotel With 100 Rooms And Less (Percent)'],color='red',label='100 Rooms or less')
ax.plot(df1['Variables'],df1['Average Hotel Occupancy Rate - Hotel With 101 - 299 Rooms (Percent)'],color='blue',label='101-299 Rooms')
ax.plot(df1['Variables'],df1['Average Hotel Occupancy Rate - Hotel With 300 Or More Rooms (Percent)'],color='orange',label='300 or more Rooms')

# Set title and labels for axes
ax.set(xlabel="Date",
       ylabel="Occupancy Rate",
       title="Hotel Occupancy Rate")
# Create a grid
ax.grid()
ax.legend()

plt.show()  
# Will be useless on a py script. Will show the preview if run on a ipython notebook
#------------------------------------------------------------------------------------------------

df2.head()
# Will be useless on a py script. Will show the preview if run on a ipython notebook
#------------------------------------------------------------------------------------------------

# The data is found to be in object/string format
# The following commands convert the data to be in int/float format
df2["Under 1 Day"].astype('int')
df2["1 Day"].astype('int')
df2["2 Days"].astype('int')
df2["3 Days"].astype('int')
df2["4 Days"].astype('int')
df2["5 Days"].astype('int')
df2["6 Days"].astype('int')
df2["7 Days"].astype('int')
df2["8-10 Days"].astype('int')
df2["11-14 Days"].astype('int')
df2["15 Days & Over"].astype('int')
df2["15-29 Days"].astype('int')
df2["30-59 Days"].astype('int')
df2["60 Days & Over"].astype('int')
df2["Average Length Of Stay (Days)"].astype('float')
# Will be useless on a py script. Will show the preview if run on a ipython notebook
#------------------------------------------------------------------------------------------------

fig2, ax2 = plt.subplots(figsize=(10, 20))

# Add x-axis and y-axis
ax2.plot(df2['Variables'],df2['Under 1 Day'],color='purple', label='0-14 Days')
ax2.plot(df2['Variables'],df2['1 Day'],color='purple',label='')
ax2.plot(df2['Variables'],df2['2 Days'],color='purple',label='')
ax2.plot(df2['Variables'],df2['3 Days'],color='purple',label='')
ax2.plot(df2['Variables'],df2['4 Days'],color='purple', label='')
ax2.plot(df2['Variables'],df2['5 Days'],color='purple',label='')
ax2.plot(df2['Variables'],df2['6 Days'],color='purple',label='')
ax2.plot(df2['Variables'],df2['7 Days'],color='purple',label='')
ax2.plot(df2['Variables'],df2['8-10 Days'],color='purple', label='')
ax2.plot(df2['Variables'],df2['11-14 Days'],color='purple',label='')
ax2.plot(df2['Variables'],df2['15 Days & Over'],color='blue',label='15 Days & Over')
ax2.plot(df2['Variables'],df2['15-29 Days'],color='orange',label='15-29 Days')
ax2.plot(df2['Variables'],df2['30-59 Days'],color='yellow', label='30-59 Days')
ax2.plot(df2['Variables'],df2['60 Days & Over'],color='red',label='60 Days & Over')

# Set title and labels for axes
ax2.set(xlabel="Date",
       ylabel="Occupancy Rate",
       title="Hotel Occupancy Rate")
# Create a grid
ax2.grid()
ax2.legend()

plt.show()
# Will be useless on a py script. Will show the preview if run on a ipython notebook
#------------------------------------------------------------------------------------------------

isNot_Jan = df2['Variables']!='2020 Jan' 
df_Jan = df2[isNot_Jan]
isNot_Feb = df_Jan['Variables']!='2020 Feb'
df_Feb = df_Jan[isNot_Feb]
isNot_Mar = df_Feb['Variables']!='2020 Mar'
df_Mar = df_Feb[isNot_Mar]
df_Mar
# Will be useless on a py script. Will show the preview if run on a ipython notebook
#------------------------------------------------------------------------------------------------

fig2, ax2 = plt.subplots(figsize=(10, 20))

# Add x-axis and y-axis
ax2.plot(df_Mar['Variables'],df_Mar['Under 1 Day'],color='purple', label='0-14 Days')
ax2.plot(df_Mar['Variables'],df_Mar['1 Day'],color='purple',label='')
ax2.plot(df_Mar['Variables'],df_Mar['2 Days'],color='purple',label='')
ax2.plot(df_Mar['Variables'],df_Mar['3 Days'],color='purple',label='')
ax2.plot(df_Mar['Variables'],df_Mar['4 Days'],color='purple', label='')
ax2.plot(df_Mar['Variables'],df_Mar['5 Days'],color='purple',label='')
ax2.plot(df_Mar['Variables'],df_Mar['6 Days'],color='purple',label='')
ax2.plot(df_Mar['Variables'],df_Mar['7 Days'],color='purple',label='')
ax2.plot(df_Mar['Variables'],df_Mar['8-10 Days'],color='purple', label='')
ax2.plot(df_Mar['Variables'],df_Mar['11-14 Days'],color='purple',label='')
ax2.plot(df_Mar['Variables'],df_Mar['15 Days & Over'],color='blue',label='15 Days & Over')
ax2.plot(df_Mar['Variables'],df_Mar['15-29 Days'],color='orange',label='15-29 Days')
ax2.plot(df_Mar['Variables'],df_Mar['30-59 Days'],color='yellow', label='30-59 Days')
ax2.plot(df_Mar['Variables'],df_Mar['60 Days & Over'],color='red',label='60 Days & Over')

# Set title and labels for axes
ax2.set(xlabel="Date",
       ylabel="Occupancy Rate",
       title="Hotel Occupancy Rate")
# Create a grid
ax2.grid()
ax2.legend()

plt.show()
# Will be useless on a py script. Will show the preview if run on a ipython notebook
#------------------------------------------------------------------------------------------------

df3["Tourism Receipts"].astype('int')
df3["Accommodation"].astype('int')
df3["Food & Beverage"].astype('int')
df3["Shopping"].astype('int')
df3["Sightseeing, Entertainment & Gaming"].astype('int')
df3["Others"].astype('int')
# Will be useless on a py script. Will show the preview if run on a ipython notebook
#------------------------------------------------------------------------------------------------

is_end = (df3['Variables']=='2020 1Q')|(df3['Variables']=='2019 4Q')|(df3['Variables']=='2019 3Q')|(df3['Variables']=='2019 2Q') \
            |(df3['Variables']=='2019 1Q')

df_Receipt = df3[is_end]
df_Receipt
# Will be useless on a py script. Will show the preview if run on a ipython notebook
#------------------------------------------------------------------------------------------------

fig3, ax3 = plt.subplots(figsize=(10, 20))

# Add x-axis and y-axis
ax3.plot(df_Receipt['Variables'],df_Receipt['Tourism Receipts'],color='blue', label='Tourism Receipts')
ax3.plot(df_Receipt['Variables'],df_Receipt['Accommodation'],color='purple',label='Accommodation')
ax3.plot(df_Receipt['Variables'],df_Receipt['Food & Beverage'],color='red',label='Food & Beverage')
ax3.plot(df_Receipt['Variables'],df_Receipt['Shopping'],color='green',label='Shopping')
ax3.plot(df_Receipt['Variables'],df_Receipt['Sightseeing, Entertainment & Gaming'],color='black', label='Sightseeing, Entertainment & Gaming')
ax3.plot(df_Receipt['Variables'],df_Receipt['Others'],color='yellow', label='Others')

# Set title and labels for axes
ax3.set(xlabel="Date",
       ylabel="Million Dollars",
       title="Tourism Receipts")
# Create a grid
ax3.grid()
ax3.legend()

plt.show()
# Will be useless on a py script. Will show the preview if run on a ipython notebook
#------------------------------------------------------------------------------------------------

df4["Total International Visitor Arrivals By Inbound Tourism Markets *"].astype('int')
is_2020 = (df4['Variables']=='2020 Jan')|(df4['Variables']=='2020 Feb')|(df4['Variables']=='2020 Mar')|(df4['Variables']=='2020 Apr') \
            |(df4['Variables']=='2020 May')|(df4['Variables']=='2020 Jun')
df_Tourist = df4[is_2020]
df_Tourist
# Will be useless on a py script. Will show the preview if run on a ipython notebook
#------------------------------------------------------------------------------------------------

fig4, ax4 = plt.subplots(figsize=(10, 20))

# Add x-axis and y-axis
ax4.plot(df_Tourist['Variables'],df_Tourist['Total International Visitor Arrivals By Inbound Tourism Markets *'],color='blue', label='Tourism Arrivals')

# Set title and labels for axes
ax4.set(xlabel="Date",
       ylabel="Visitors",
       title="International Visitor Arrivals")
# Create a grid
ax4.grid()
ax4.legend()

plt.show()
# Will be useless on a py script. Will show the preview if run on a ipython notebook
#------------------------------------------------------------------------------------------------
