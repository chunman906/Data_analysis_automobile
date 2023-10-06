import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from df_combined_year import *


def good_bad_fe_combined(df_all_years):
    # Merging the column for the combined years of datasets
    df_all_years['Combined FE'] = df_all_years_original['Combined FE'].combine_first(df_all_years['Comb FE (Guide) - Conventional Fuel']).combine_first(df_all_years['Comb Unadj FE - Conventional Fuel'].combine_first(df_all_years['Comb Unrd Adj FE - Conventional Fuel']))


    # data cleaning for all years cars
    df_all_years = df_all_years[df_all_years['Combined FE'] > 0]


    # Calculate the mean of two transmission
    average_fe = df_all_years.groupby('Transmission')['Combined FE'].mean().sort_values(ascending=True)

    mean_average_fe = round(average_fe.mean(), 1)

    # identify good and bad average FE
    good_fe_cars = df_all_years[df_all_years['Combined FE'] > mean_average_fe]
    bad_fe_cars = df_all_years[df_all_years['Combined FE'] < mean_average_fe]


    # sorting the combined FE value by ascending orders
    top_fe_cars = good_fe_cars.sort_values(by='Combined FE', ascending=False)
    bottom_fe_cars = bad_fe_cars.sort_values(by='Combined FE', ascending=True)

    # identify the top 20 and bottom 20
    top_fe_cars = top_fe_cars.head(20)
    bottom_fe_cars = bottom_fe_cars.head(20)

    print('The top 20 good fuel economy cars of all previous years are:')
    print(top_fe_cars[['Combined FE']+['Transmission']+['Model Year']+['Mfr Name']+['Division']+['Carline']])

    print('The bottom 20 bad fuel economy cars of all previous years are:')
    print(bottom_fe_cars[['Combined FE']+['Transmission']+['Model Year']+['Mfr Name']+['Division']+['Carline']])


    # Visualisation for the transmission FE
    fig, ax = plt.subplots(figsize=(10, 6))
    df_all_years.boxplot(column='Combined FE', by='Model Year', rot=90, ax=ax)
    plt.title('Fuel Economy by Transmission Type in the past 8 years')
    plt.xlabel('Model Year')
    plt.ylabel('Combined FE')
    plt.suptitle('')
    plt.show()
