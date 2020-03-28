import matplotlib.pyplot as plt
import pandas as pd
import webget
import os
# Ex1

def data_to_panda(path, filename):
    if(os.path.isfile(filename)):
        pass
    else:
        webget.download(path, filename)
    return pd.read_csv(filename, delimiter=';')


""" 
-- 5A --
What is the change in pct of divorced danes from 2008 to 2020?
"""
def changes_divorced_dane():
    path = 'https://api.statbank.dk/v1/data/FOLK1A/CSV?delimiter=Semicolon&CIVILSTAND=F&Tid=*'
    filename = 'FOLK1A-5A.csv'

    df = data_to_panda(path, filename)
    start = df['INDHOLD'][0]
    percentage_div = {}
    for idx, row in df.iterrows():
        diff = row['INDHOLD'] - start
        perc = diff/row['INDHOLD']*100

        percentage_div[row['TID']] = perc

    return percentage_div


"""
-- 5B --
Which of the 5 biggest cities has the highest percentage of 'Never Married'?
"""
def highest_unmarried_rate():
    path = ('https://api.statbank.dk/v1/data/FOLK1A/CSV?delimiter=Semicolon&OMR%C3%85DE=851%2C101%2C561%2C461%2C751&CIVILSTAND=TOT%2CU&Tid=2020K1')
    filename = 'FOLK1A-5B.csv'

    df = data_to_panda(path, filename)
    biggest_cities = ['Aalborg', 'København', 'Esbjerg', 'Odense', 'Aarhus']
    highest = 0

    for city in biggest_cities:
        c = df.loc[df['OMRÅDE'] == city]
        unmarried = (c.loc[c['CIVILSTAND'] == 'Ugift']).iat[0,3]
        everyone = (c.loc[c['CIVILSTAND'] == 'I alt']).iat[0,3]
        percent = unmarried/everyone*100
        print(percent)
        if percent > highest:
            highest = percent
    return highest


"""
-- 5C --
Show a bar chart of changes in marrital status in Copenhagen from 2008 till now
"""
def changes_in_marrital_stat():
    path = 'https://api.statbank.dk/v1/data/FOLK1A/CSV?delimiter=Semicolon&OMR%C3%85DE=101&CIVILSTAND=U%2CG%2CF%2CE%2CTOT&Tid=*'
    filename = 'FOLK1A-5C.csv'
    df = data_to_panda(path, filename)

    # Getting groups for ugift, gift, fraskilt
    civilstand_groups = df.groupby('CIVILSTAND')
    fig, ax = plt.subplots(figsize=(8, 6))

    for name, group in civilstand_groups:
        group.plot(x='TID', y='INDHOLD', ax=ax, label=name)


"""
-- 5D --
Show a bar chart of 'Married' and 'Never Married' for all ages in DK (Hint: 2 bars of different color)
"""
def marrital_stat_all_ages():
    path = 'https://api.statbank.dk/v1/data/FOLK1A/CSV?delimiter=Semicolon&OMR%C3%85DE=000&ALDER=*&CIVILSTAND=G%2CU'
    filename = 'FOLK1A-5D.csv'

    df = data_to_panda(path, filename)

    # Remove the two rows with 'i alt'
    df = df.drop([0, 1])

    civilstand = df.groupby('CIVILSTAND')

    fig, ax = plt.subplots(figsize=(8, 6))
    for name, group in civilstand:
        group.plot(x='ALDER', y='INDHOLD', ax=ax, label=name, rot=0)