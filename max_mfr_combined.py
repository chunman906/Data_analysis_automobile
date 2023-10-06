import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from df_combined_year import *


def max_mfr_combined():
    # calculating the manufacturer have most model quantity for the combined years of Y2015 to Y2023 (9 years)
    model_counts_all = df_all_years.groupby('Mfr Name')['Carline'].nunique()
    manufacturer_max_all = model_counts_all.idxmax()
    quantity_max_all = model_counts_all.max()
    print(f'The manufacturer has most car model quantity for the combined years across Y2015 to Y2023 is <{manufacturer_max_all}> with the counts of <{quantity_max_all}>. ')

    # Plotting
    model_counts_all.plot(kind='bar', stacked=True)
    plt.ylabel('Quantity')
    plt.show()

# Note:
# This result is finding out the manufacturer in multiple year (2015-2023) perspective.

