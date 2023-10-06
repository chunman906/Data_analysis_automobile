import pandas as pd

# ETL operations
# combining all the years excels
df_2015 = pd.read_excel('2015 - Dataset(Assessment).xls')
df_2016 = pd.read_excel('Other years/2016 FEGuide for DOE-OK to release-no-sales-5-8-2019_Mercedes_public.xlsx')
df_2017 = pd.read_excel('Other years/2017 FE Guide for DOE-release dates before 3-25-2019-no sales-9-19-2019McLarenforpublic.xlsx')
df_2018 = pd.read_excel('Other years/2018 FE Guide for DOE3 -all rel dates-no-sales-3-25-2019McLarenforpublic.xlsx')
df_2019 = pd.read_excel('Other years/2019 FE Guide-for DOE-release dates before 12-19-2019-no-sales- 12_17_2019Koenigseggpublic.xlsx')
df_2020 = pd.read_excel('Other years/2020 FE Guide-adds and corrections for DOE-OK for release-no-sales- 4-7-2021Koenigseggpublic.xlsx')
df_2021 = pd.read_excel('Other years/2021 FE Guide-release dates before 11-23-2021-no-sales -11-22-2021 for DOE_Karmapublic.xlsx')
df_2022 = pd.read_excel('Other years/2022 FE Guide for DOE-release dates before 1-12-2023-no-sales -1-11-2023public.xlsx')
df_2023 = pd.read_excel('Other years/2016 FEGuide for DOE-OK to release-no-sales-5-8-2019_Mercedes_public.xlsx')


df_2015['Year'] = 2015
df_2016['Year'] = 2016
df_2017['Year'] = 2017
df_2018['Year'] = 2018
df_2019['Year'] = 2019
df_2020['Year'] = 2020
df_2021['Year'] = 2021
df_2022['Year'] = 2022
df_2023['Year'] = 2023

# Concatenate the dataframes
df_all_years_original = pd.concat([df_2015, df_2016, df_2017, df_2018, df_2019, df_2020, df_2021, df_2022, df_2023], ignore_index=True)

# Data cleaning - remove column with 90% Nan value
thresh_value = int(len(df_all_years_original) * 0.9)
df_all_years = df_all_years_original.dropna(axis=1, thresh=thresh_value)






