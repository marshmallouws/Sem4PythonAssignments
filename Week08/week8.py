# Blushing unit's assignment
import pymysql
from bs4 import BeautifulSoup
from selenium import webdriver
import requests
import datetime
from flask import Flask

"""
Get data from countries. If all = false, get top 5 countries
"""
url = "https://www.worldometers.info/coronavirus/"
r = requests.get(url)
soup = BeautifulSoup(r.text, "html.parser")
header = [
    "country",
    "tot_cases",
    "new_cases",
    "tot_deaths",
    "new_deaths",
    "tot_recovered",
    "active_cases",
    "serious_critical",
    "cases_per_1m_pop",
    "death_per_1m_pop",
]
res = []  # list of single rows

# get rows in table
table = soup.find(id="main_table_countries_today")
rows = table.findChildren("tr")[:6]

for row in rows:
    data = []
    for r in row.select("td"):
        data.append(r.text)

    if len(data) == 10:
        res.append(dict(zip(header, data)))


def save_data(data):
    """
    Saves the data to a mysql database
    """
    cnx = pymysql.connect(
        user="dev", password="ax2", host="127.0.0.1", port=3307, db="sem4python_week8",
    )
    cursor = cnx.cursor()

    cursor.executemany(
        """
        INSERT INTO corona(country, tot_cases, new_cases, tot_deaths, new_deaths, tot_recovered, active_cases, serious_critical, cases_per_1m_pop, death_per_1m_pop)
        VALUES (%(country)s, %(tot_cases)s, %(new_cases)s, %(tot_deaths)s, %(new_deaths)s, %(tot_recovered)s, %(active_cases)s, %(serious_critical)s, %(cases_per_1m_pop)s, %(death_per_1m_pop)s)
        """,
        data,
    )
    cnx.commit()


# 3 "Lav en webservice API som har en GET metode således du kan få alt dataen ud.
# Ekstra opgave hvis du har tid: Lav et bar chart over de 5 lande, hvoraf man kan se
# ud fra hvert land deres smittetal, antal døde og antal raske. "

app = Flask(__name__)


@app.route("/")
def show_data():
    header = ", ".join(res[0].keys())
    data = [", ".join(d.values()) for d in res]
    data_string = "</br>".join(data)

    return header + "</br>" + data_string


save_data(res)
