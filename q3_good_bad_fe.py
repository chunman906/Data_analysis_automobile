import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def good_bad_fe():
    # read the year 2015 csv
    data_2015 = pd.read_csv('2015 - Dataset(Assessment).csv')

    # data cleaning
    data_2015 = data_2015[data_2015['Combined FE'] > 0]

    # Calculate the mean of two transmission
    average_fe = data_2015.groupby('Transmission')['Combined FE'].mean().sort_values(ascending=True)

    mean_average_fe = round(average_fe.mean(), 1)

    # identify good and bad average FE
    good_fe_cars = data_2015[data_2015['Combined FE'] > mean_average_fe]
    bad_fe_cars = data_2015[data_2015['Combined FE'] < mean_average_fe]


    # sorting the combined FE value by ascending orders
    top_fe_cars = good_fe_cars.sort_values(by='Combined FE', ascending=False)
    bottom_fe_cars = bad_fe_cars.sort_values(by='Combined FE', ascending=True)

    # identify the top 20 and bottom 20
    top_fe_cars = top_fe_cars.head(20)
    bottom_fe_cars = bottom_fe_cars.head(20)

    print('The top 20 good fuel economy cars are:')
    print(top_fe_cars[['Combined FE']+['Transmission']+[column for column in top_fe_cars.columns if column != 'Combined FE' and 'Transmission']])

    print('The bottom 20 bad fuel economy cars are:')
    print(bottom_fe_cars[['Combined FE']+['Transmission']+[column for column in bottom_fe_cars.columns if column != 'Combined FE' and 'Transmission']])

    # Visualisation for the transmission FE
    fig, ax = plt.subplots(figsize=(10, 6))
    data_2015.boxplot(column='Combined FE', by='Transmission', rot=90, ax=ax)
    plt.title('Fuel Economy by Transmission Type')
    plt.xlabel('Transmission Type')
    plt.ylabel('Combined FE')
    plt.suptitle('')
    plt.show()
