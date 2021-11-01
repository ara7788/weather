from flask import render_template
from flask_bootstrap import Bootstrap
from app import app
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter

cityname = 'Kharkov'
df = pd.read_csv("weather.csv", sep=',', encoding='utf-8')
df.style.format('{:.0f}')
df = df[(df['Year'] >= 1900)]

plt.rcParams["figure.figsize"] = (8, 5)
fig, ax = plt.subplots()


def neg_tick(x, pos):
    return '%.1f' % (-x if x else 0)


plt.bar(df['Year'].values, -df['Jan'].values, label=f'{cityname} - January Temperature, C')
plt.plot(df['Year'].values, -df['Jan'].rolling(window=20, min_periods=1).mean(), 'r-')
ax.yaxis.set_major_formatter(FuncFormatter(neg_tick))

plt.legend(loc='best')
plt.tight_layout()
#plt.show()
fig.savefig('app/static/weather.png')
plt.close(fig)

@app.route('/', methods=("POST", "GET"))
def html_table():
    return render_template('simple.html', tables=[df.to_html(classes='data', header="true")])
