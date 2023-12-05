import pandas
import matplotlib.pyplot as plt
import matplotlib.lines as line

df = pandas.read_csv("data/01_unemp.csv")

mask = df['Country Code'].isin(["AUT"])
aut_data = df[mask]

mean = aut_data.mean(axis=1, skipna=True, numeric_only=True)

data = aut_data.filter(regex='(200[6-9]|20[1-2][0-9]|202[0-2])', axis=1)

x_werte = list(data.columns)
y_werte = list(data.values[0])

plt.plot(x_werte, y_werte, marker=".", color="blue")
plt.title("Unemployment Rate", loc='center')

red_patch = plt.axvspan(x_werte.index("2020"), x_werte.index("2022"), alpha=0.5, color='red', label='Covid-19 Crisis')
yellow_patch = plt.axvspan(x_werte.index("2007"), x_werte.index("2008"), alpha=0.5, color='yellow', label='9/11')

rate = line.Line2D(x_werte, y_werte, color='blue', marker=".", label='Unemployment Rate')
plt.legend(handles=[rate, red_patch, yellow_patch])

plt.xlabel("Year")
plt.ylabel("Unemployment Rate (%)")

plt.grid(True)
plt.show()

