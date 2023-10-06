import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

def corr_fe_co2():
    # read the year 2015 csv
    data_2015 = pd.read_csv('2015 - Dataset(Assessment).csv')
    # print(data_2015[['Combined FE']+['Combined CO2']])

    # data cleaning
    data_2015 = data_2015[data_2015['Combined FE'] > 0]
    data_2015 = data_2015[data_2015['Combined CO2'] > 0]

    # calculate the correlation
    corr_combine = data_2015['Combined FE'].corr(data_2015['Combined CO2'])
    corr_engine = data_2015['Combined FE'].corr(data_2015['Engine Displacement'])
    corr_city = data_2015['Combined FE'].corr(data_2015['City CO2'])
    corr_highway = data_2015['Combined FE'].corr(data_2015['Highway CO2'])

    print('In year 2015, the correlation of combined FE with other data are: ')
    print(f'Combined CO2: {corr_combine}, Engine Power: {corr_engine}, City Co2: {corr_city}, Highway Co2: {corr_highway}')

    # calculate the correlation matrix
    correlation_matrix = np.array([
        [1, corr_combine, corr_engine, corr_city, corr_highway],
        [corr_combine, 1, np.nan, np.nan, np.nan],
        [corr_engine, np.nan, 1, np.nan, np.nan],
        [corr_city, np.nan, np.nan, 1, np.nan],
        [corr_highway, np.nan, np.nan, np.nan, 1]
    ])

    # Visualisation with Heatmap
    labels = ['Combined FE', 'Combined CO2', 'Engine Displacement', 'City CO2', 'Highway CO2']
    plt.figure(figsize=(10, 8))
    sns.heatmap(correlation_matrix, annot=True, cmap="coolwarm", xticklabels=labels, yticklabels=labels, vmin=-1, vmax=1)
    plt.title('Correlation heatmap')
    plt.show()
