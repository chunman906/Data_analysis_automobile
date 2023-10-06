import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def max_mfr():
    # read the year 2015 csv
    data_2015 = pd.read_csv('2015 - Dataset(Assessment).csv')

    # calculating the manufacturer have max model quantity
    model_counts = data_2015.groupby('Mfr Name')['Carline'].nunique()
    manufacturer_max = model_counts.idxmax()
    quantity_max = model_counts.max()

    print(f'The manufacturer has most quantity of Y2015 car models is <{manufacturer_max}> with the counts of <{quantity_max}>. ')

    # Plotting
    model_counts.plot(kind='bar', stacked=True)

    plt.ylabel('Quantity')
    plt.show()


# Note:
# This result is finding out the manufacturer in 2015 single year perspective.


# print(data_2015['Mfr Name'])
# pivot_mfr = pd.pivot_table(data_2015,
#                values='Carline',
#                index=['Mfr Name'],
#                 aggfunc='count')
# print(pivot_mfr)





