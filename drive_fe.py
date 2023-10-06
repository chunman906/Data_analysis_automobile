import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from df_combined_year import *


def drive_fe():
    # read the year 2015 csv
    data_2015 = pd.read_csv('2015 - Dataset(Assessment).csv')

    # data cleaning to drop irrelevant data
    # print(data_2015['Drive Desc'].unique())
    data_2015 = data_2015[data_2015['Drive Desc'] != 'd']

    # grouping each drive type and calculate their average combined FE
    drive_type_fe = data_2015.groupby('Drive Desc')['Combined FE'].mean().sort_values(ascending=False)

    # printing the result
    for drive, fe in drive_type_fe.items():
        print(f"Average fuel economy for {drive}: {fe:.2f} Combined FE")

    # plot the result
    color = ['coral', 'yellow', 'blue', 'green', 'pink']

    plt.figure(figsize=(10,6))
    drive_type_fe.plot(kind='bar', color=color)
    plt.title('Year 2015 Fuel Economy by Drive Type')
    plt.ylabel('Average Combined FE')
    plt.xlabel('Drive Type')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.show()


