import pandas as pd
import matplotlib.pyplot as plt
from df_combined_year import *


def wheel_engine_combined():
    # Selecting 2WD and 4WD car
    carline_2_4_wd = df_all_years['Carline Class Desc'].str.contains('2WD|4WD', case=False, na=False)

    # Plus engine power is more than 3.5
    selected_car = df_all_years[carline_2_4_wd & (df_all_years['Eng Displ'] > 3.5)]

    # Showing the data that met with the criteria
    print('All the 2WD and 4WD cars with engine power greater than 3.5 in year 2015: ')
    print(selected_car[['Model Year', 'Mfr Name', 'Carline Class Desc', 'Eng Displ', 'Release Date']])

    # Plotting bar chart for the counts of selected cars based on their Mfr Name
    selected_car['Mfr Name'].value_counts().plot(kind='bar', figsize=(12, 6))
    plt.title('Count of 2WD and 4WD with Engine Power > 3.5 by Manufacturer from 2015-2023')
    plt.xlabel('Manufacturer Name')
    plt.ylabel('Number of Cars')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()
