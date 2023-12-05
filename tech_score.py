import pandas
import matplotlib.pyplot as plt
import matplotlib.patches as patch

df_unemp = pandas.read_csv("data/01_unemp.csv")
df_tech = pandas.read_csv("data/03_techScore.csv")

df = pandas.merge(df_unemp, df_tech, how='inner', on=["Country Name"])

df = df.filter(regex='Country Code|2022|Score', axis=1)

x_werte = list(df['Score'])
y_werte = list(df['2022'])
names = list(df['Country Code'])

plt.scatter(x_werte, y_werte, 10, 'blue', 's')
plt.title("Country Rating", loc='center')

for i, txt in enumerate(names):
    plt.annotate(txt, (x_werte[i], y_werte[i]), size=6)

b_patch = patch.Patch(color='blue', label='Enemployment Rate / TechScore')
plt.legend(handles=[b_patch])

plt.xlabel("Unemployment Rate (%)")
plt.ylabel("Tech Score")

plt.grid(True)
plt.show()

