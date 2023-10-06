import pandas as pd
import matplotlib.pyplot as plt


def wheel_engine():
    # read the year 2015 csv
    data_2015 = pd.read_csv('2015 - Dataset(Assessment).csv')
    # checking the figures on each column
    # print(data_2015[[column for index, column in enumerate(data_2015.columns) if index not in [0, 1, 2, 3]]])

    # Selecting 2WD and 4WD car
    carline_2_4_wd = data_2015['Carline Class Desc'].str.contains('2WD|4WD', case=False, na=False)

    # Plus engine power is more than 3.5
    selected_car = data_2015[carline_2_4_wd & (data_2015['Engine Displacement'] > 3.5)]

    # Showing the data that met with the criteria
    print('All the 2WD and 4WD cars with engine power greater than 3.5 in year 2015: ')
    print(selected_car[['Model Year', 'Mfr Name', 'Carline Class Desc', 'Engine Displacement', 'Release Date']])

    # Plotting bar chart for the counts of selected cars based on their Mfr Name
    selected_car['Mfr Name'].value_counts().plot(kind='bar', figsize=(12, 6))
    plt.title('Count of 2WD and 4WD with Engine Power > 3.5 by Manufacturer')
    plt.xlabel('Manufacturer Name')
    plt.ylabel('Number of Cars')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()