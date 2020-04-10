import pandas as pd
import datetime
df1 = pd.read_csv('portfolios_2.csv', index_col="id")
df2 = pd.read_csv('raw_price_data_2.csv', index_col="Date")
df30 = pd.read_csv('30_date_range.csv', index_col="Date")
df4502 = pd.read_csv('4502_date_range.csv', index_col="Date")

"""
alpha1 = df1["x_1"].loc[30]
print(df2[alpha1].loc["31/12/2015"])

print(df4502.index)
date_list = (df4502.index.tolist())
print(date_list)
print(len(date_list)-1)

p = [df1["x_1"].loc[30],df1["x_2"].loc[30],df1["x_3"].loc[30],df1["x_4"].loc[30],df1["x_5"].loc[30]]


p[] = df1["x_1"].loc[30]
p[] = df1["x_2"].loc[30]
p[] = df1["x_3"].loc[30]
p[] = df1["x_4"].loc[30]
p[] = df1["x_5"].loc[30]

q[0] = df1["x_1"].loc[4502]
q[1] = df1["x_2"].loc[4502]
q[2] = df1["x_3"].loc[4502]
q[3] = df1["x_4"].loc[4502]
q[4] = df1["x_5"].loc[4502]

date_list = (df30.index.tolist())
print(date_list)
"""
start30date = "4/11/2008"
start4502date = "30/4/2009"

sum = 0
sum1 = 0
sum2 = 0
sum3 = 0
sum4 = 0
sum5 = 0
sum6 = 0
sum7 = 0
sum8 = 0
sum9 = 0


for i in range(len(df30.index)):
    date_list = (df30.index.tolist())
    aa = df1["monthly_invt"].loc[30] * df1["w_1"].loc[30]
    aaa = aa / (df2[df1["x_1"].loc[30]].loc[date_list[i]])
    sum = sum+aaa
print(sum)

bb = df1["initial_invt"].loc[30] * df1["w_1"].loc[30]
bbb = bb / (df2[df1["x_1"].loc[30]].loc[start30date])
print(sum+bbb)

for i in range(len(df30.index)):
    date_list = (df30.index.tolist())
    aa = df1["monthly_invt"].loc[30] * df1["w_2"].loc[30]
    aaa = aa / (df2[df1["x_2"].loc[30]].loc[date_list[i]])
    sum1 = sum1+aaa
#print(sum1)

for i in range(len(df30.index)):
    date_list = (df30.index.tolist())
    aa = df1["monthly_invt"].loc[30] * df1["w_3"].loc[30]
    aaa = aa / (df2[df1["x_3"].loc[30]].loc[date_list[i]])
    sum2 = sum2+aaa
#print(sum2)

for i in range(len(df30.index)):
    date_list = (df30.index.tolist())
    aa = df1["monthly_invt"].loc[30] * df1["w_4"].loc[30]
    aaa = aa / (df2[df1["x_4"].loc[30]].loc[date_list[i]])
    sum3 = sum3+aaa
#print(sum3)

for i in range(len(df30.index)):
    date_list = (df30.index.tolist())
    aa = df1["monthly_invt"].loc[30] * df1["w_5"].loc[30]
    aaa = aa / (df2[df1["x_5"].loc[30]].loc[date_list[i]])
    sum4 = sum4+aaa
#print(sum4)



for i in range(len(df4502.index)):
    date_list = (df4502.index.tolist())
    aa = df1["monthly_invt"].loc[4502] * df1["w_1"].loc[4502]
    aaa = aa / (df2[df1["x_1"].loc[4502]].loc[date_list[i]])
    sum5 = sum5+aaa
#print(sum5)

for i in range(len(df4502.index)):
    date_list = (df4502.index.tolist())
    aa = df1["monthly_invt"].loc[4502] * df1["w_2"].loc[4502]
    aaa = aa / (df2[df1["x_2"].loc[4502]].loc[date_list[i]])
    sum6 = sum6+aaa
#print(sum6)

for i in range(len(df4502.index)):
    date_list = (df4502.index.tolist())
    aa = df1["monthly_invt"].loc[4502] * df1["w_3"].loc[4502]
    aaa = aa / (df2[df1["x_3"].loc[4502]].loc[date_list[i]])
    sum7 = sum7+aaa
#print(sum7)

for i in range(len(df30.index)):
    date_list = (df30.index.tolist())
    aa = df1["monthly_invt"].loc[30] * df1["w_4"].loc[30]
    aaa = aa / (df2[df1["x_4"].loc[30]].loc[date_list[i]])
    sum8 = sum8+aaa
#print(sum8)

for i in range(len(df30.index)):
    date_list = (df30.index.tolist())
    aa = df1["monthly_invt"].loc[30] * df1["w_5"].loc[30]
    aaa = aa / (df2[df1["x_4"].loc[30]].loc[date_list[i]])
    sum9 = sum9+aaa
#print(sum9)
    

