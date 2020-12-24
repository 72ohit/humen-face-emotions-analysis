#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 14 14:17:34 2020

@author: rohit
"""
import pandas as pd
import matplotlib.pyplot as plt

df= pd.read_csv("c.csv")

#print(df)
#
#
#
#
#plot = df[147:-1].plot.pie(y='smile_count', figsize=(5,9))
#
smile_count = df.tail()["smile_count"]
e_act = df.tail()["e_act"]
bothe =df.tail()["bothe"]
colors = ["#1f77b4", "#ff7f0e", "#2ca02c", "#d62728", "#8c564b"]

plt.pie(smile_count,e_act,bothe, labels=smile_count,e_act,bothe,  colors=colors,
autopct='%1.1f%%', shadow=True, startangle=140)
plt.title("count")
plt.show()