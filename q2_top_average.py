import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def top_average():
    # read the year 2015 csv
    data_2015 = pd.read_csv('2015 - Dataset(Assessment).csv')

    # data cleaning
    data_2015 = data_2015[data_2015['City FE'] > 0]
    data_2015 = data_2015[data_2015['Highway FE'] > 0]

    # group by car model
    selected_data = data_2015[['City FE', 'Highway FE', 'Mfr Name', 'Carline']]
    grouped_car_city = selected_data.groupby(['Mfr Name', 'Carline']).agg({
        'City FE': 'mean'
    })

    grouped_car_highway = selected_data.groupby(['Mfr Name', 'Carline']).agg({
        'Highway FE': 'mean'
    })

    # sort the list
    sorted_car_city = grouped_car_city.sort_values('City FE', ascending=False)
    sorted_car_highway = grouped_car_highway.sort_values('Highway FE', ascending=False)

    # Display the top average FE car
    top_car_city = sorted_car_city.head()
    top_car_highway = sorted_car_highway.head()

    print(f'The top average fuel economy car model for the city is : \n')
    print(f'{top_car_city} \n \n')
    print(f'The top average fuel economy car model for the Highway is : \n')
    print(f'{top_car_highway}')






