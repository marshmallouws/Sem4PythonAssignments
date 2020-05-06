import pandas as pd

url = "https://raw.githubusercontent.com/datsoftlyngby/dat4sem2020spring-python/e8c07d515cef1fea2adb6c41dc0342391f4e9cc8/notebooks/data/rodents.csv"

df = pd.read_csv(url, sep=";", header=1)


print(df)
