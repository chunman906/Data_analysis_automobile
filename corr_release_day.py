import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from df_combined_year import *


def corr_release_day(df_all_years):
    # data cleaning for warming msgs
    df_all_years = df_all_years.copy()

    # Merging the column for the combined years of datasets
    df_all_years.loc[:, 'Combined FE'] = df_all_years_original['Combined FE'].combine_first(df_all_years['Comb FE (Guide) - Conventional Fuel']).combine_first(df_all_years['Comb Unadj FE - Conventional Fuel'].combine_first(df_all_years['Comb Unrd Adj FE - Conventional Fuel']))

    # calculate the correlation
    corr_release_date = df_all_years.loc[:, 'Combined FE'].corr(df_all_years['Release Date'])

    print(f'The correlation between Combined Fuel Efficiency and Release Date is: {round(corr_release_date, 2)} which indiate a very weak relationship')

    # Scatter plot for Release Date vs Combined FE
    plt.figure(figsize=(12, 6))
    plt.scatter(df_all_years['Release Date'], df_all_years['Combined FE'], alpha=0.5)
    plt.title(f'Correlation between Combined FE and Release Date: {corr_release_date:.2f}')
    plt.xlabel('Release Date')
    plt.ylabel('Combined FE')
    plt.grid(True, which='both', linestyle='--', linewidth=0.5)
    plt.show()





